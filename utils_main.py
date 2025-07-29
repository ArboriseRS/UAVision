import os
from PySide6.QtGui import QPixmap, QImage
os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%
from modules import *
from PySide6.QtCore import Signal, Qt, QThread, QMutex
from PySide6 import QtCore, QtGui, QtWidgets
import csv
from pathlib import Path
import cv2
import numpy as np
import torch
import lightglue.utils
from lightglue import LightGlue, SuperPoint, DISK, ALIKED, SIFT, DoGHardNet, viz2d
import numpy as np
import math as m
# py生成pyc文件
import py_compile
def wgs84_to_gauss_kruger(lon, lat):
    a = 6378137.0  # 地球长半轴
    f = 1 / 298.257223563  # 扁率
    zone_width = 6  # 分带宽度为6度
    lon0 = (int(lon / zone_width) * zone_width + zone_width / 2)  # 中央经线

    e2 = 2 * f - f ** 2  # 第一偏心率的平方
    e2s = e2 / (1 - e2)  # 第二偏心率的平方
    N = a / m.sqrt(1 - e2 * m.sin(m.radians(lat)) ** 2)  # 卯酉圈半径

    t = m.tan(m.radians(lat))  # 赤纬的正切
    eta2 = e2s * m.cos(m.radians(lat)) ** 2  # 第二偏心率的平方

    l = m.radians(lon - lon0)  # 经度差

    # 计算X坐标（北方向）
    x = (
            111134.8611 * lat
            + (32005.7799 - 133.6938 * lat ** 2 + 0.6976 * lat ** 4) * m.sin(m.radians(2 * lat))
            + (0.3967 - 0.0004 * lat ** 2) * m.sin(m.radians(4 * lat))
    )

    # 计算Y坐标（东方向）
    y = N * (
            l * m.cos(m.radians(lat))
            + (1 - t ** 2 + eta2) * (l ** 3 * m.cos(m.radians(lat)) ** 3) / 6
            + (5 - 18 * t ** 2 + t ** 4 + 14 * eta2 - 58 * eta2 * t ** 2) * (l ** 5 * m.cos(m.radians(lat)) ** 5) / 120
    )

    return x, y

    # 计算中央经
#子线程1：实现无人机定位
def convert_cv_to_qimage(cv_image):
    """
    将 OpenCV 图像转换为 QImage。

    Args:
        cv_image: OpenCV 图像 (NumPy 数组，BGR 格式)

    Returns:
        QImage: 转换后的 QImage 对象
    """
    # 将 BGR 格式转换为 RGB 格式
    result_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

    # 获取图像的高度、宽度和通道数
    h, w, c = result_image.shape

    # 创建 QImage 对象
    # 注意：这里使用 QImage.Format_RGB888 格式
    qimage = QImage(result_image.data, w, h, c * w, QImage.Format_RGB888)
    return qimage
class WorkThread(QThread):
    #自定义信号
    setimage = QtCore.Signal(QtGui.QPixmap)
    listdata = Signal(list)  # 传递一个包含数字和字符串的列表
    updatamap=Signal(list) #更新地图的信号
    finished = Signal()  # 线程结束信号
    task_main_signal = Signal(bool, bool, str, str, str, bool, str)  # 实现
    message=Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mutex = QMutex()
        self.condition = QWaitCondition()
        self.show_keypoints = None
        self.display = None
        self.map_path = None
        self.query_path = None
        self.output_dir = None
        self.WRITE_RESULT = None
        self.feature_type = None
        self.is_running=None

    def run(self):
        # print(111)
        import haversine as hs
        from haversine import Unit
        while True:
            torch.cuda.empty_cache()
            self.mutex.lock()
            while self.show_keypoints is None or self.display is None or self.map_path is None or \
                    self.query_path is None  or self.WRITE_RESULT is None or \
                    self.feature_type is None:
                self.condition.wait(self.mutex)

            show_keypoints = self.show_keypoints
            display = self.display
            map_path = self.map_path
            query_path = self.query_path
            output_dir = self.output_dir
            WRITE_RESULT = self.WRITE_RESULT
            feature_type = self.feature_type
            self.mutex.unlock()
            self.is_running = True
            map_path = map_path + "/"
            query_path = query_path + "/"
            output_dir = output_dir + "/"
            map_filename = map_path + "map.csv"
            drone_photos_filename = query_path + "photo_metadata.csv"
            max_num_keypoints = 10000  # 最大关键点数
            if os.path.exists(map_filename) and os.path.exists(drone_photos_filename) and feature_type != "" :
                geo_images_list = csv_read_sat_map(map_filename, map_path)
                drone_images_list = csv_read_drone_images(drone_photos_filename, query_path)

                # 真实经纬度和计算的经纬度
                latitude_truth = []
                longitude_truth = []
                latitude_calculated = []
                longitude_calculated = []
                print(str(len(drone_images_list)) + " drone photos were loaded.")

                # 处理所有无人机影像
                for drone_image in drone_images_list:
                    if self.is_running:
                        torch.cuda.empty_cache()
                        latitude_truth.append(drone_image.latitude)  # 从无人机图像元数据中获取地面实况，以便日后进行比较
                        longitude_truth.append(drone_image.longitude)
                        photo = cv2.imread(drone_image.filename)  # 读无人机图像

                        max_features = 0  # 跟踪最佳匹配，更多特征 = 更好匹配
                        located = False  # 标志，用于指示无人机图像是否位于地图中
                        center = None  # 无人机图像在地图中的中心位置

                        rotations = [20]  # list of rotations to try可尝试的轮换列表
                        # GNSS 元数据可能有错误的旋转角度，因此，我们尝试用不同的（手动建立的）旋转来匹配图像
                        # 迭代所有旋转，本例中只迭代一次旋转
                        for rot in rotations:
                            # 将查询照片写入地图文件夹
                            cv2.imwrite(map_path + "1_query_image.png", photo)
                            #############替换函数################################# #############替换函数#################################
                            # 输入：input,output_dir,show_keypoints,display,color,feature_type, max_num_keypoints
                            image_glob = ['*.png', '*.jpg', '*.jpeg', '*.JPG']  # 图像文件格式
                            center_new = None
                            skip = 1  # 跳过的帧数
                            max_length = 1000000  # 最大处理长度
                            # 如果要改进特征匹配性能，请修改以下重要参数 #清理缓存
                            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # 'mps', 'cpu'
                            message1=str('正在设备 "{}" 上运行推断'.format(device))
                            self.message.emit(message1)
                            print('正在设备 \"{}\" 上运行推断'.format(device))
                            # feature_type = 'SuperPoint'  #
                            # max_num_keypoints = 2048  # 最大关键点数
                            # 加载特征提取器和匹配器
                            extractor, matcher = load_extractor_matcher(feature_type, device, max_num_keypoints)
                            vs = VideoStreamer(map_path, skip, image_glob, max_length)

                            frame_uav, ret = vs.next_frame()  # 第一张，待匹配的无人机影像
                            assert ret, '读取第一帧时出错（尝试不同的 --input？）'

                            frame_uav_tensor = lightglue.utils.numpy_image_to_torch(frame_uav)
                            #####last_frame是无人机影像
                            last_data = extractor.extract(frame_uav_tensor.to(device))  # 提取特征点
                            # 600 800 3
                            query_image_new = frame_uav
                            last_image_id = 0

                            if output_dir is not None:
                                print('==> 将输出写入到 {}'.format(output_dir))
                                message2 = str('将输出写入到 {}'.format(output_dir))
                                self.message.emit(message2)
                                Path(output_dir).mkdir(exist_ok=True)

                            satellite_map_index_new = None  # must 最佳匹配的卫星图像在地图中的索引
                            index = 0  # 如果找到匹配，则卫星图像的索引
                            feature_number = -1  # 最大匹配数，用于跟踪最佳匹配
                            located_image_new = None  # must 找到最佳匹配的卫星图像
                            features_mean_new = [0, 0]  # must特征像素坐标的平均值

                            while True:
                                # 当前要匹配的卫星影像
                                frame, ret = vs.next_frame()  # 下一张影像，从这里开始就是卫星影像

                                if not ret:
                                    print('完成 demo_superglue.py')
                                    message3 = '完成 demo_superglue.py'
                                    self.message.emit(message3)
                                    break
                                stem0, stem1 = last_image_id, vs.i - 1  # 记录id
                                frame_tensor = lightglue.utils.numpy_image_to_torch(frame)

                                pred = extractor.extract(frame_tensor.to(device))  # 张量
                                matches01 = matcher({"image0": last_data, "image1": pred})  # 输入张量

                                last_data_low, pred_low, matches01 = [
                                    lightglue.utils.rbd(x) for x in [last_data, pred, matches01]
                                ]  # remove batch dimension降维
                                kpts0, kpts1, matches = last_data_low["keypoints"], pred_low["keypoints"], matches01["matches"]
                                mkpts0, mkpts1 = kpts0[matches[..., 0]], kpts1[matches[..., 1]]
                                # 转化成np数组
                                kpts0 = kpts0.cpu().numpy()
                                kpts1 = kpts1.cpu().numpy()
                                mkpts0 = mkpts0.cpu().numpy()
                                mkpts1 = mkpts1.cpu().numpy()

                                """
                                       使用 findHomography 找到在卫星地图中的图像
                                """

                                # 需要至少 4 个匹配特征来计算单应性变换

                                MATCHED = False
                                print("找到的匹配数:", len(mkpts1))
                                message4= "找到的匹配数:"+str(len(mkpts1))
                                self.message.emit(message4)
                                # 需要至少 4 个匹配特征来计算单应性变换
                                if len(mkpts1) >= 4:
                                    perspective_tranform_error = False
                                    M, mask = cv2.findHomography(mkpts0, mkpts1, cv2.RANSAC, 5.0)
                                    h, w, _ = query_image_new.shape
                                    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
                                    try:
                                        dst = cv2.perspectiveTransform(pts, M)
                                    except:
                                        message5 = "透视变换错误。终止匹配。"
                                        self.message.emit(message5)
                                        print("透视变换错误。终止匹配。")
                                        perspective_tranform_error = True

                                    if (len(mkpts1) > feature_number) and not perspective_tranform_error:
                                        frame = cv2.polylines(frame, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
                                        moments = cv2.moments(dst)
                                        cX = int(moments["m10"] / moments["m00"])
                                        cY = int(moments["m01"] / moments["m00"])
                                        center_new = (cX, cY)  # shape[0] 是 Y 坐标，shape[1] 是 X 坐标
                                        # 使用比率而不是像素，因为图像在 superglue 中被重塑了
                                        features_mean_new = np.mean(mkpts0, axis=0)

                                        # 绘制匹配区域的中心
                                        cv2.circle(frame, center_new, radius=10, color=(255, 0, 255), thickness=5)
                                        cv2.circle(query_image_new, (int(features_mean_new[0]), int(features_mean_new[1])),
                                                   radius=10,
                                                   color=(255, 0, 0),
                                                   thickness=2)
                                        center_new = (cX / frame.shape[1], cY / frame.shape[0])
                                        satellite_map_index_new = index
                                        feature_number = len(mkpts1)
                                        MATCHED = True
                                else:
                                    message6 = "未找到匹配的照片"
                                    self.message.emit(message6)
                                    print("未找到匹配的照片")

                                ####绘图可视化#######

                                small_text = [
                                    'Match Threshold: {:.2f}'.format(len(mkpts1)),
                                    'Image Pair: {:06}:{:06}'.format(stem0, stem1)]
                                color = (255, 0, 0)
                                ###这里可以控制是否显示特征点标记
                                out = viz2d.make_matching_plot_fast(
                                    query_image_new, frame, kpts0, kpts1, mkpts0, mkpts1, color, text='',
                                    path=None, show_keypoints=show_keypoints, small_text='')

                                if MATCHED:
                                    located_image_new = out
                                ##显示弹窗
                                if display:
                                    # 将 OpenCV 的 numpy 数组转换为 QImage
                                    # qimage = QtGui.QImage(out.data, out.shape[1], out.shape[0],QtGui.QImage.Format_RGB888)
                                    out = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
                                    h, w, c = out.shape
                                    qimage = QPixmap.fromImage(QImage(out.data, w, h, c * w, QImage.Format_RGB888))
                                    # 信号.emit(值）
                                    self.setimage.emit(qimage)


                                index += 1

                            #############替换函数################################# #############替换函数#################################
                            torch.cuda.empty_cache()
                            # 如果无人机图像位于地图中，且特征数量多于之前的最佳匹配值，则更新最佳匹配值
                            # 有时，透视变换返回的像素中心点会超过 1，在这种情况下，请放弃结果
                            if (feature_number > max_features and center_new[0] < 1 and center_new[1] < 1):
                                satellite_map_index = satellite_map_index_new
                                center = center_new
                                located_image = located_image_new
                                features_mean = features_mean_new
                                query_image = query_image_new
                                max_features = feature_number
                                located = True
                        photo_name = drone_image.filename.split("/")[-1]
                        torch.cuda.empty_cache()
                        # 如果无人机图像位于地图中，则计算无人机图像的地理位置
                        if center != None and located:
                            current_location = calculate_geo_pose(geo_images_list[satellite_map_index], center, features_mean,
                                                                  query_image.shape)

                            # Write the results to the image result file with the best match
                            cv2.putText(located_image, "Calculated: " + str(current_location), org=(10, 1330),
                                        fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.8, color=(0, 0, 0))
                            cv2.putText(located_image,
                                        "Ground truth: " + str(drone_image.latitude) + ", " + str(drone_image.longitude),
                                        org=(10, 1360), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.8, color=(0, 0, 255))
                            cv2.imwrite(output_dir + photo_name + "_located.png", located_image)

                            print("Image " + str(photo_name) + " was successfully located in the map")
                            print("Calculated location: ", str(current_location[0:2]))
                            print("Ground Truth: ", drone_image.latitude, drone_image.longitude)

                            message7 = "Image " + str(photo_name) + " was successfully located in the map"
                            self.message.emit(message7)
                            message8="纬度：  "+str(current_location[0])+"     经度：  "+ str(current_location[1])
                            self.message.emit(message8)
                            # 发射更新列表的信号
                            # 转化成11带高斯克吕格投影坐标


                            # 进行坐标转换wgs84_to_gauss_kruger( current_location[0], current_location[1])
                            x, y = wgs84_to_gauss_kruger( current_location[1], current_location[0])
                            ########################################
                            result_data = [str(photo_name), str(current_location[1]), str(current_location[0]), x,y]  # 获取您的结果数据
                            self.listdata.emit(result_data)  # 发射信号，传递结果数据
                            # 发射更新map的信号
                            updata_map = [current_location[1], current_location[0]]
                            self.updatamap.emit(updata_map)
                            # Save the calculated location for later comparison with the ground truth
                            drone_image.matched = True
                            drone_image.latitude_calculated = current_location[0]
                            drone_image.longitude_calculated = current_location[1]

                            latitude_calculated.append(drone_image.latitude_calculated)
                            longitude_calculated.append(drone_image.longitude_calculated)

                        else:
                            print("NOT MATCHED:", photo_name)
                            message9 = "NOT MATCHED:"+photo_name
                            self.message.emit(message9)
                            # 发射更新列表的信号

                        # 是否将结果写入output_dir输出文件夹
                        if WRITE_RESULT:
                            header = ['Filename', 'Latitude', 'Longitude', 'Calculated_Latitude', 'Calculated_Longitude',
                                      'Latitude_Error',
                                      'Longitude_Error', 'Meters_Error', 'Corrected', 'Matched']
                            path = output_dir + "calculated_coordinates.csv"
                            # 检查文件是否存在
                            file_exists = os.path.isfile(path)
                            with open(path, 'a', encoding='UTF8',newline="") as f:
                                writer = csv.writer(f)
                                # 如果文件不存在或者是空的，写入表头
                                if not file_exists or os.stat(path).st_size == 0:
                                    writer.writerow(header)
                                photo_name = drone_image.filename.split("/")[-1]
                                loc1 = (drone_image.latitude, drone_image.longitude)
                                loc2 = (drone_image.latitude_calculated, drone_image.longitude_calculated)
                                dist_error = hs.haversine(loc1, loc2, unit=Unit.METERS)
                                lat_error = drone_image.latitude - drone_image.latitude_calculated
                                lon_error = drone_image.longitude - drone_image.longitude_calculated
                                line = [photo_name, str(drone_image.latitude), str(drone_image.longitude),
                                        str(drone_image.latitude_calculated),
                                        str(drone_image.longitude_calculated), str(lat_error), str(lon_error), str(dist_error),
                                        str(drone_image.corrected), str(drone_image.matched)]
                                writer.writerow(line)


                    #参数置回初始
                    self.show_keypoints = None
                    self.display = None
                    self.map_path = None
                    self.query_path = None
                    self.output_dir = None
                    self.WRITE_RESULT = None
                    self.feature_type = None
                    torch.cuda.empty_cache()
            else:
                if not os.path.exists(map_filename):
                    message10 = str("请选择正确的卫星影像路径")
                    self.message.emit(message10)
                if not os.path.exists(drone_photos_filename):
                    message11 = str("请选择正确的无人机影像路径")
                    self.message.emit(message11)
                if feature_type == "":
                    message12 = str("请选择特征提取算法")
                    self.message.emit(message12)
                # 参数置回初始
                self.show_keypoints = None
                self.display = None
                self.map_path = None
                self.query_path = None
                self.output_dir = None
                self.WRITE_RESULT = None
                self.feature_type = None
                torch.cuda.empty_cache()

        self.finished.emit()  # 发射线程结束信号

    def stop_1(self):
        self.is_running = False

    @Slot(bool, bool, str, str, str, bool, str)
    def process_signal(self, show_keypoints, display, map_path, query_path, output_dir, write_result, feature_type):
        self.mutex.lock()
        self.show_keypoints = show_keypoints
        self.display = display
        self.map_path = map_path
        self.query_path = query_path
        self.output_dir = output_dir
        self.WRITE_RESULT = write_result
        self.feature_type = feature_type
        self.condition.wakeAll()
        self.mutex.unlock()

class Fun1(QThread):
    # 自定义信号
    setimage_tiqu_result = QtCore.Signal(QtGui.QPixmap)#用来更新label的数据
    setimage_pipei_result = QtCore.Signal(QtGui.QPixmap)  # 用来更新label的数据
    setimage_video_result = QtCore.Signal(QtGui.QPixmap)  # 用来更新label的数据
    setimage_jiaozheng_result= QtCore.Signal(QtGui.QPixmap)
    setimage_jiaozheng_right = QtCore.Signal(QtGui.QPixmap)
    task_tiqu_signal = Signal(str, str,str,int,int)  #提取信号
    task_pipei_signal = Signal(str, str,str,int,int)  #匹配信号
    task_jiaozheng_signal = Signal(str, str, str, int, int)  # 匹配信号
    task_video_signal = Signal(str, str, str, int, int)
    finished = Signal()  # 线程结束信号
    # stop_video=Signal()#关闭摄像头

    def __init__(self, parent=None):
        super().__init__(parent)
        self.mutex = QMutex()
        self.condition = QWaitCondition()
        self.load_image1 = None#str 文件路径
        self.load_image2 = None
        self.type = None
        self.feature_type = None
        self.max_keypoints = None
        self.if_video_runing=True
        self.image1=None
        self.image2 = None
        self.image3 = None

    def run(self):
        while True:
            try:
                self.mutex.lock()

                while (self.feature_type is None or self.max_keypoints is None or self.load_image1 is None or
                       self.load_image2 is None or self.type is None):
                    self.condition.wait(self.mutex)

                feature_type = self.feature_type
                max_keypoints = self.max_keypoints
                load_image1 = self.load_image1
                load_image2 = self.load_image2
                type = self.type
                self.mutex.unlock()

                # 提取特征点
                if type == 1:
                    print("开始执行提取")
                    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

                    extractor, matcher = load_extractor_matcher(feature_type, device, max_keypoints)
                    image0_cv, image1_cv=lightglue.utils.load_image_fun1(load_image1,load_image2)
                    image0 = lightglue.utils.load_image_new(image0_cv)
                    image1 = lightglue.utils.load_image_new(image1_cv)
                    wide1 = image0.shape[2]#宽
                    feats0 = extractor.extract(image0.to(device))
                    feats1 = extractor.extract(image1.to(device))
                    matches01 = matcher({"image0": feats0, "image1": feats1})
                    feats0, feats1, matches01 = [
                        lightglue.utils.rbd(x) for x in [feats0, feats1, matches01]
                    ]  # remove batch dimension
                    kpts0, kpts1, matches = feats0["keypoints"], feats1["keypoints"], matches01["matches"]
                    m_kpts0, m_kpts1 = kpts0[matches[..., 0]], kpts1[matches[..., 1]]

                    #可视化
                    plot_image = viz2d.plot_images([image0, image1])#拼接图像
                    kpc0, kpc1 = viz2d.cm_prune(matches01["prune0"]), viz2d.cm_prune(matches01["prune1"])
                    #显示特征点
                    plot_image_keypoints = viz2d.plot_keypoints(plot_image, [m_kpts0, m_kpts1], wide1, colors=[kpc0, kpc1], radius=3)
                    plot_image_keypoints_cv=lightglue.utils.torch_to_numpy(plot_image_keypoints)
                    #特征点连接
                    #viz2d.plot_matches(plot_image_keypoints_cv, m_kpts0, m_kpts1, wide1, color=(0, 255, 0), lw=1)
                    self.image1=plot_image_keypoints_cv
                    plot_image_keypoints_cv0 = cv2.cvtColor(plot_image_keypoints_cv, cv2.COLOR_BGR2RGB)
                    h, w, c = plot_image_keypoints_cv0.shape
                    qimage_tiqu = QPixmap.fromImage(QImage( plot_image_keypoints_cv0.data, w, h, c * w, QImage.Format_RGB888))
                    self.setimage_tiqu_result.emit(qimage_tiqu)
                    self.reset_state()

                # 特征匹配
                elif type == 2:
                    print("开始执行匹配")
                    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

                    extractor, matcher = load_extractor_matcher(feature_type, device, max_keypoints)
                    image0_cv, image1_cv = lightglue.utils.load_image_fun1(load_image1, load_image2)
                    image0 = lightglue.utils.load_image_new(image0_cv)
                    image1 = lightglue.utils.load_image_new(image1_cv)
                    wide1 = image0.shape[2]  # 宽
                    feats0 = extractor.extract(image0.to(device))
                    feats1 = extractor.extract(image1.to(device))
                    matches01 = matcher({"image0": feats0, "image1": feats1})
                    feats0, feats1, matches01 = [
                        lightglue.utils.rbd(x) for x in [feats0, feats1, matches01]
                    ]  # remove batch dimension
                    kpts0, kpts1, matches = feats0["keypoints"], feats1["keypoints"], matches01["matches"]
                    m_kpts0, m_kpts1 = kpts0[matches[..., 0]], kpts1[matches[..., 1]]

                    # 可视化
                    plot_image = viz2d.plot_images([image0, image1])  # 拼接图像
                    kpc0, kpc1 = viz2d.cm_prune(matches01["prune0"]), viz2d.cm_prune(matches01["prune1"])
                    # 显示特征点
                    plot_image_keypoints = viz2d.plot_keypoints(plot_image, [m_kpts0, m_kpts1], wide1,
                                                                colors=[kpc0, kpc1], radius=3)
                    plot_image_keypoints_cv = lightglue.utils.torch_to_numpy(plot_image_keypoints)
                    # 特征点连接
                    viz2d.plot_matches(plot_image_keypoints_cv, m_kpts0, m_kpts1, wide1, color=(0, 255, 0), lw=1)

                    self.image2 = plot_image_keypoints_cv
                    plot_image_keypoints_cv0 = cv2.cvtColor(plot_image_keypoints_cv, cv2.COLOR_BGR2RGB)
                    h, w, c = plot_image_keypoints_cv0.shape
                    qimage_pipei = QPixmap.fromImage(
                        QImage(plot_image_keypoints_cv0.data, w, h, c * w, QImage.Format_RGB888))

                    self.setimage_pipei_result.emit(qimage_pipei)
                    self.reset_state()

                elif type == 3:
                    print("开始执行影像校正")
                    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
                    extractor, matcher = load_extractor_matcher(feature_type, device, max_keypoints)
                    image0_cv, image1_cv = lightglue.utils.load_image_fun2(load_image1, load_image2)
                    image0 = lightglue.utils.load_image_new(image0_cv)
                    image1 = lightglue.utils.load_image_new(image1_cv)

                    # extract local features
                    feats0 = extractor.extract(image0.to(device))  # auto-resize the image, disable with resize=None
                    feats1 = extractor.extract(image1.to(device))
                    # match the features
                    matches01 = matcher({'image0': feats0, 'image1': feats1})
                    feats0, feats1, matches01 = [ lightglue.utils.rbd(x) for x in [feats0, feats1, matches01]]  # remove batch dimension
                    matches = matches01['matches']  # indices with shape (K,2)
                    points0 = feats0['keypoints'][matches[..., 0]]  # coordinates in image #0, shape (K,2)
                    points1 = feats1['keypoints'][matches[..., 1]]  # coordinates in image #1, shape (K,2)
                    # Convert points to numpy arrays
                    points_left = points0.cpu().numpy().astype(np.float32)
                    points_right = points1.cpu().numpy().astype(np.float32)
                    # Compute homography matrix
                    matrix, mask = cv2.findHomography(points_right, points_left, cv2.RANSAC, 5.0)  # Using RANSAC method
                    # Save the homography matrix
                    h, w, c = image0_cv.shape
                    h3, w3, c3 = image1_cv.shape
                    warp_image_ = cv2.warpPerspective(image1_cv, matrix, (2 * w, h),  # 大小的定义
                                                      flags=cv2.INTER_LINEAR)  # Use homography matrix

                    warp_image = remove_black_border(warp_image_)
                    #发射信号
                    warp_image_0 = cv2.cvtColor(warp_image, cv2.COLOR_BGR2RGB)
                    h1, w1, c1 = warp_image_0.shape
                    qimage_warp_image = QPixmap.fromImage(QImage(warp_image_0.data, w1, h1, c1 * w1, QImage.Format_RGB888))
                    self.setimage_jiaozheng_right.emit(qimage_warp_image)

                    # 创建拼接影像
                    final_image = np.zeros([h, 2 * w, 3], dtype="uint8")
                    final_image[0:h, 0:w] = image0_cv

                    # # 开始拼接
                    # for i in range(h):
                    #     for j in range(2 * w):
                    #         if warp_image_[i][j].any() != 0:
                    #             final_image[i][j] = warp_image_[i][j]

                    # 使用布尔索引进行拼接
                    mask = (warp_image_ != 0).any(axis=2)
                    final_image[mask] = warp_image_[mask]

                    final_image0 = remove_black_border(final_image)
                    #final_image
                    self.image3 = final_image0
                    final_image_0 = cv2.cvtColor(final_image0, cv2.COLOR_BGR2RGB)
                    h2, w2, c2 = final_image_0.shape
                    qimage_final_image = QPixmap.fromImage(QImage(final_image_0.data, w2, h2, c2 * w2, QImage.Format_RGB888))
                    self.setimage_jiaozheng_result.emit(qimage_final_image)

                    self.reset_state()


                else:
                    print("开始执行视频模式")
                    torch.set_grad_enabled(False)
                    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # 'mps', 'cpu'

                    extractor1 = SuperPoint(max_num_keypoints=500).eval().to(device)  # load the extractor
                    extractor2 = SuperPoint(max_num_keypoints=10000).eval().to(device)  # load the extractor
                    matcher = LightGlue(features="superpoint").eval().to(device)

                    # plt.figure()
                    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
                    ret0, image0_cv = cap.read()  # onecv读取函数,
                    offset = image0_cv.shape[1]
                    if not ret0:
                        exit(-1)
                    image0 =lightglue.utils.load_image_new(image0_cv)
                    feats0_raw = extractor1.extract(image0.to(device))
                    n = 0
                    while self.if_video_runing:
                        n += 1
                        ret1, image1_cv = cap.read()
                        if not ret1:
                            break

                        image1 = lightglue.utils.load_image_new(image1_cv)
                        feats1_raw = extractor2.extract(image1.to(device))
                        matches01 = matcher({"image0": feats0_raw, "image1": feats1_raw})
                        feats0, feats1, matches01 = [
                            lightglue.utils.rbd(x) for x in [feats0_raw, feats1_raw, matches01]
                        ]  # remove batch dimension

                        kpts0, kpts1, matches = feats0["keypoints"], feats1["keypoints"], matches01["matches"]
                        m_kpts0, m_kpts1 = kpts0[matches[..., 0]], kpts1[matches[..., 1]]
                        #####可视化
                        plot_image = viz2d.plot_images([image0, image1])
                        # 显示特征点
                        kpc0, kpc1 = viz2d.cm_prune(matches01["prune0"]), viz2d.cm_prune(matches01["prune1"])
                        result_image = viz2d.plot_keypoints(plot_image, [m_kpts0, m_kpts1], offset, colors=[kpc0, kpc1],
                                                            radius=3)
                        result_image_new =  lightglue.utils.torch_to_numpy(result_image)  # 转换cheng cv
                        # 显示连线
                        viz2d.plot_matches(result_image_new, m_kpts0, m_kpts1, offset, color=(0, 255, 0), lw=1)
                        #显示在ui上
                        result_image_new0 = cv2.cvtColor(result_image_new, cv2.COLOR_BGR2RGB)
                        h, w, c = result_image_new0.shape
                        qimage_video = QPixmap.fromImage(QImage(result_image_new0.data, w, h, c * w, QImage.Format_RGB888))

                        self.setimage_video_result.emit(qimage_video)
                    print("jieshsu")
                    cap.release()
                    cv2.destroyAllWindows()


                    #self.setimage_video_result.emit(qimage_video)
                    self.reset_state()
            except Exception as e:
                print(f"线程运行错误：{e}")
            finally:
                self.mutex.unlock()
        self.finished.emit()  # 发射线程结束信号

    def reset_state(self):
        self.is_running = None
        self.load_image1 = None
        self.load_image2 = None
        self.type = None
        self.feature_type = None
        self.max_keypoints = None
        self.if_video_runing = True

    @Slot(str,str,str,int,int)
    def process_signal(self,feature_type,load_image1,load_image2,max_keypoints,type):
        print("成功接收参数")
        self.mutex.lock()
        self.feature_type = feature_type
        self.load_image1 = load_image1
        self.load_image2 = load_image2
        self.max_keypoints = max_keypoints
        self.type = type
        self.condition.wakeAll()
        self.mutex.unlock()

class Houfang(QThread):
    # 自定义信号
    message=Signal(list)
    hou_task_signal = Signal(list, list,list,list,list,float)  #提取信号
    finished = Signal()  # 线程结束信号

    def __init__(self, parent=None):
        super().__init__(parent)
        self.mutex = QMutex()
        self.condition = QWaitCondition()
        self.X = None
        self.Y = None
        self.Z = None
        self.x = None
        self.y = None
        self.f = None

    def run(self):
        while True:
            try:
                self.mutex.lock()

                while (self.X is None or self.Y is None or self.Z is None or
                       self.x is None or self.y is None or self.f is None):
                    self.condition.wait(self.mutex)

                X=self.X
                Y=self.Y
                Z=self.Z
                x=self.x
                y=self.y
                f=self.f

                # X = [36589.41, 37631.08, 39100.97, 40426.54]
                # Y = [25273.32, 31324.51, 24934.98, 30319.81]
                # Z = [2195.17, 728.69, 2386.50, 757.31]
                #
                # x = [-86.15, -53.40, -14.78, 10.46]
                # y = [-68.99, 82.21, -76.63, 64.43]
                # f = 153.24
                message111 = ["开始运行","后方交会"]
                self.message.emit(message111)
                # 计算 distance1
                distance1 = m.sqrt((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2)
                # 计算 distance2
                distance2 = m.sqrt((X[1] - X[0]) ** 2 + (Y[1] - Y[0]) ** 2)
                # 计算 m
                k = distance2 / distance1
                # 初始化参数
                fo = wo = ko = 0
                xo = yo = 0
                Xsum = 0
                Ysum = 0

                # 计算 X、Y 坐标的平均值
                for i in [0, 1, 2, 3]:
                    Xsum = Xsum + X[i]
                    Ysum = Ysum + Y[i]
                #初始化
                Zos = k * f
                Xos = Xsum / 4
                Yos = Ysum / 4

                # 初始化近似像点坐标数组
                x_apxm = [0, 0, 0, 0]
                y_apxm = [0, 0, 0, 0]

                # 初始化旋转矩阵 R、L 矩阵、A 矩阵
                R = np.mat(np.zeros((3, 3)))
                L = np.mat(np.zeros((8, 1)))
                A = np.mat(np.zeros((8, 6)))

                # 初始化参数改正值
                f_cor = w_cor = k_cor = 1
                # 初始化迭代次数
                flag = 0
                # 迭代计算参数
                while (abs(f_cor) > 0.000001) | (abs(w_cor) > 0.000001) | (abs(k_cor) > 0.000001):
                    # 计算旋转矩阵 R
                    R = r_mat(fo, wo, ko)
                    # 近似计算像点坐标
                    x_apxm, y_apxm = xy_approximate(X, Y, Z, x, y, Xos, Yos, Zos, R, f, xo, yo)

                    # 构建 L 矩阵
                    for i in [0, 1, 2, 3]:
                        L[2 * i] = x_apxm[i]
                        L[2 * i + 1] = y_apxm[i]

                    # 构建 A 矩阵
                    for i in [0, 1, 2, 3]:
                        A[2 * i:2 * i + 2, :] = a_parameter(X[i], Y[i], Z[i], Xos, Yos, Zos, x[i], y[i], wo, ko, R, f,
                                                            xo, yo)

                    # 计算参数改正值
                    X_mat = np.mat(np.zeros((6, 1)))
                    X_mat = (A.T * A).I * A.T * L

                    f_cor = X_mat[3, 0]
                    w_cor = X_mat[4, 0]
                    k_cor = X_mat[5, 0]

                    # 更新参数
                    Xos = Xos + X_mat[0, 0]
                    Yos = Yos + X_mat[1, 0]
                    Zos = Zos + X_mat[2, 0]
                    fo = fo + X_mat[3, 0]
                    wo = wo + X_mat[4, 0]
                    ko = ko + X_mat[5, 0]

                    # 迭代次数加 1
                    flag += 1
                    # 打印迭代信息
                    if flag <= 10000:
                        print("第 %d 次迭代：f_cor = %f,w_cor = %f,k_cor = %f" % (flag, f_cor, w_cor, k_cor))
                        message1 = [str("第 %d 次迭代"% (flag)), str("f_cor = %f,w_cor = %f,k_cor = %f"% (f_cor, w_cor, k_cor))]  # 获取您的结果数据
                        self.message.emit(message1)
                    else:
                        # message2 = str("级数不收敛，中间结果为")
                        # self.message.emit(message2)
                        print("级数不收敛，中间结果为：")
                        break

                # 打印结果
                if flag <= 100:
                    print("级数收敛，最终结果为：")

                print(" Xs=%f,\n Ys=%f,\n Zs=%f,\n f=%f,\n w=%f,\n k=%f" % (Xos, Yos, Zos, fo, wo, ko))

                message3 = ["级数收敛，最终结果为：",str("Xs="+str(Xos)+" , "+"Ys="+str(Yos)+" , "+"Zs="+str(Zos)+" , "+"f=" + str(fo) + " , " + "w=" + str(wo) + " , " + "k=" + str(ko) + " ；")]
                self.message.emit(message3)
                # message4 = "f=" + str(fo) + " , " + "w=" + str(wo) + " , " + "k=" + str(ko) + " ；"
                # self.message.emit(message4)

                print(" R = ", end='')
                print(R)

                # 计算单位权中误差
                V = np.mat(np.zeros((8, 1)))
                V = A * X_mat - L
                errorValue = m.sqrt((V.T * V).item() / (2 * 4 - 6))
                print("单位权中误差：%f" % errorValue)
                message5 = ["单位权中误差：" , str(errorValue)]
                self.message.emit(message5)
                message6 = [" ", " "]
                self.message.emit(message6)
                self.reset_state()
            except Exception as e:
                print(f"线程运行错误：{e}")
            finally:
                self.mutex.unlock()
        self.finished.emit()  # 发射线程结束信号

    def reset_state(self):
        self.X = None
        self.Y = None
        self.Z = None
        self.x = None
        self.y = None
        self.f = None

    @Slot(str,str,str,int,int)
    def process_signal(self,X,Y,Z,x,y,f):
        print("成功接收后方交会参数")
        self.mutex.lock()
        self.X = X
        self.Y = Y
        self.Z = Z
        self.x = x
        self.y = y
        self.f = f
        self.condition.wakeAll()
        self.mutex.unlock()
class Qianfang(QThread):
    # 自定义信号
    message=Signal(list)
    qian_task_signal = Signal(list, list,list,list,list,list,list,list,list)  #提取信号
    finished = Signal()  # 线程结束信号

    def __init__(self, parent=None):
        super().__init__(parent)
        self.mutex = QMutex()
        self.condition = QWaitCondition()
        self.X = None
        self.Y = None
        self.Z = None
        self.x = None
        self.y = None
        self.f = None
        self.fai=None
        self.oumiga=None
        self.k=None

    def run(self):
        while True:
            try:
                self.mutex.lock()

                while (self.X is None or self.Y is None or self.Z is None or
                       self.x is None or self.y is None or self.f is None or
                       self.fai is None or self.oumiga is None or self.k is None):
                    self.condition.wait(self.mutex)
                message111 = ["开始运行", "前方交会"]
                self.message.emit(message111)
                X=self.X
                Y=self.Y
                Z=self.Z
                x=self.x
                y=self.y
                f=self.f
                fai=self.fai
                oumiga = self.oumiga
                k = self.k

                # 两个像点坐标
                # l_point = np.array([x[0], y[0], -f[0]])
                # r_point = np.array([x[1], y[1], -f[1]])
                #这里修改ui
                deltax=[-2.9949326 ,115.30009 ]
                deltay=[98.313214 ,106.807568 ]
                l_point = np.array([x[0] + deltax[0], y[0] + deltay[0], -f[0]])
                r_point = np.array([x[1] + deltax[1], y[1] + deltay[1], -f[1]])

                # 计算空间辅助坐标
                out_ele1 = np.array([fai[0], oumiga[0], k[0]])
                out_ele2 = np.array([fai[1], oumiga[1], k[1]])

                # 旋转后的坐标点
                rotated_l_point = rotate(out_ele1) @ l_point
                rotated_r_point = rotate(out_ele2) @ r_point

                # 提取旋转后的坐标
                u1 = rotated_l_point[0]
                v1 = rotated_l_point[1]
                w1 = rotated_l_point[2]

                u2 = rotated_r_point[0]
                v2 = rotated_r_point[1]
                w2 = rotated_r_point[2]

                # 计算投影系数
                [n1, n2] = BaseLine(X, Y, Z, rotated_l_point, rotated_r_point)

                # 计算地面坐标
                gx = X[1] + n1 * u1
                gy = 0.5 * ((Y[0] + n1 * v1) + (Y[1] + n2 * v2))
                gz = Z[0] + n1 * w1

                print([gx, gy, gz])
                message = ["对应地面点坐标",str("gx: "+str(gx)+"    gy:"+str(gy)+"   gz:"+str(gz))]
                self.message.emit(message)
                message6 = [" ", " "]
                self.message.emit(message6)
                self.reset_state()
            except Exception as e:
                print(f"线程运行错误：{e}")
            finally:
                self.mutex.unlock()
        self.finished.emit()  # 发射线程结束信号

    def reset_state(self):
        self.X = None
        self.Y = None
        self.Z = None
        self.x = None
        self.y = None
        self.f = None
        self.fai = None
        self.oumiga = None
        self.k = None

    @Slot(str,str,str,int,int)
    def process_signal(self,X,Y,Z,x,y,f,fai,oumiga,k):
        print("成功接收前方交会参数")
        self.mutex.lock()
        self.X = X
        self.Y = Y
        self.Z = Z
        self.x = x
        self.y = y
        self.f = f
        self.fai = fai
        self.oumiga = oumiga
        self.k = k
        self.condition.wakeAll()
        self.mutex.unlock()


def remove_black_border(stitched_image):
    """
    去除拼接图像中的黑边

    :param stitched_image: 拼接后的图像，带有黑边
    :return: 去除黑边后的图像
    """
    # 转换为灰度图像以便进行黑色边框检测
    gray = cv2.cvtColor(stitched_image, cv2.COLOR_BGR2GRAY)

    # 使用二值化方法找到黑色区域
    _, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    # 找到黑色边框的边界
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找到最大的轮廓
    max_contour = max(contours, key=cv2.contourArea)

    # 获取边界框
    x, y, w, h = cv2.boundingRect(max_contour)

    # 裁剪图像
    cropped_image = stitched_image[y:y + h, x:x + w]

    return cropped_image
def load_extractor_matcher(feature_type, device, max_num_keypoints):
    """
    根据客户的选择加载特征提取器和匹配器
    说明：
         1.默认值在速度和准确性之间做了很好的权衡。最大限度地提高精确度，使所有关键点禁用自适应机制
         extractor = SuperPoint(max_num_keypoints=None).eval().to(device)
         matcher = LightGlue(features='superpoint', depth_confidence=-1, width_confidence=-1).eval().to(device)
         2.提高速度的同时略微降低精度，减少关键点的数量并降低自适应阈值；
         extractor = SuperPoint(max_num_keypoints=1024).eval().to(device)
         matcher = LightGlue(features='superpoint', depth_confidence=0.9, width_confidence=0.95).eval().to(device)
    Args:
    - feature_type: str, 特征类型，可选值为 'superpoint', 'disk', 'aliked', 'sift','doghardnet'
    - device: torch.device, 设备
    - max_num_keypoints: int, 最大关键点数（默认为2048）

    Returns:
    - extractor: 特征提取器
    - matcher: 匹配器
    """
    if torch.cuda.is_available():
        print(f"Using device: {device}")
        if feature_type == 'SuperPoint':
            extractor = SuperPoint(max_num_keypoints=max_num_keypoints).eval().to(device)
            matcher = LightGlue(features='superpoint', depth_confidence=-1, width_confidence=-1).eval().to(device)
        elif feature_type == 'DISK':
            extractor = DISK(max_num_keypoints=max_num_keypoints).eval().cuda()
            matcher = LightGlue(features='disk', depth_confidence=-1, width_confidence=-1).eval().cuda()
        elif feature_type == 'ALIKED':
            extractor = ALIKED(max_num_keypoints=max_num_keypoints).eval().cuda()
            matcher = LightGlue(features='aliked', depth_confidence=-1, width_confidence=-1).eval().cuda()
        elif feature_type == 'SIFT':
            extractor = SIFT(max_num_keypoints=max_num_keypoints).eval().cuda()
            matcher = LightGlue(features='sift', depth_confidence=-1, width_confidence=-1).eval().cuda()
        elif feature_type == 'DoGHardNet':
            extractor = DoGHardNet(max_num_keypoints=max_num_keypoints).eval().cuda()
            matcher = LightGlue(features='doghardnet', depth_confidence=-1, width_confidence=-1).eval().cuda()
        else:
            raise ValueError("Invalid feature type. Supported types: 'superpoint', 'disk', 'aliked', 'sift'，'doghardnet'")

        return extractor, matcher
    else:
        print(f"Using device: {device}")
class VideoStreamer:
    def __init__(self, basedir, skip, image_glob, max_length=1000000):
        self._ip_grabbed = False
        self._ip_running = False
        self._ip_camera = False
        self._ip_image = None
        self._ip_index = 0
        self.cap = []
        self.camera = True
        self.video_file = False
        self.listing = []
        self.interp = cv2.INTER_AREA
        self.i = 0
        self.skip = skip
        self.max_length = max_length
        if isinstance(basedir, int) or basedir.isdigit():
            print('==> Processing USB webcam input: {}'.format(basedir))
            self.cap = cv2.VideoCapture(int(basedir))
            self.listing = range(0, self.max_length)
        elif basedir.startswith(('http', 'rtsp')):
            print('==> Processing IP camera input: {}'.format(basedir))
            self.cap = cv2.VideoCapture(basedir)
            self.start_ip_camera_thread()
            self._ip_camera = True
            self.listing = range(0, self.max_length)
        elif Path(basedir).is_dir():
            print('==> Processing image directory input: {}'.format(basedir))
            self.listing = list(Path(basedir).glob(image_glob[0]))
            for j in range(1, len(image_glob)):
                image_path = list(Path(basedir).glob(image_glob[j]))
                self.listing = self.listing + image_path
            self.listing.sort()
            self.listing = self.listing[::self.skip]
            self.max_length = np.min([self.max_length, len(self.listing)])
            if self.max_length == 0:
                raise IOError('No images found (maybe bad \'image_glob\' ?)')
            self.listing = self.listing[:self.max_length]
            self.camera = False
        elif Path(basedir).exists():
            print('==> Processing video input: {}'.format(basedir))
            self.cap = cv2.VideoCapture(basedir)
            self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            num_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
            self.listing = range(0, num_frames)
            self.listing = self.listing[::self.skip]
            self.video_file = True
            self.max_length = np.min([self.max_length, len(self.listing)])
            self.listing = self.listing[:self.max_length]
        else:
            raise ValueError('VideoStreamer input \"{}\" not recognized.'.format(basedir))
        if self.camera and not self.cap.isOpened():
            raise IOError('Could not read camera')
    def next_frame(self):
        """ Return the next frame, and increment internal counter.
        Returns
             image: Next H x W image.
             status: True or False depending whether image was loaded.
        """

        if self.i == self.max_length:
            return (None, False)
        if self.camera:
            print("can not process video")
        else:
            image_file = str(self.listing[self.i])
            image = lightglue.utils.load_image1(image_file)
        self.i = self.i + 1
        return (image, True)
class GeoPhotoDrone:
    """Stores a drone photo together with GNSS location将无人机照片与 GNSS 定位和相机旋转参数一起存储
    and camera rotation parameters
    """

    def __init__(self, filename, photo=0, latitude=0, longitude=0, \
                 altitude=0, gimball_roll=0, gimball_yaw=0, gimball_pitch=0, flight_roll=0, flight_yaw=0,
                 flight_pitch=0):
        self.filename = filename
        self.photo = photo
        self.latitude = latitude
        self.longitude = longitude
        self.latitude_calculated = -1
        self.longitude_calculated = -1
        self.altitude = altitude
        self.gimball_roll = gimball_roll
        self.gimball_yaw = gimball_yaw
        self.gimball_pitch = gimball_pitch
        self.flight_roll = flight_roll
        self.flight_yaw = flight_yaw
        self.flight_pitch = flight_pitch
        self.corrected = False
        self.matched = False

    def __str__(self):
        return "%s; \nlatitude: %f \nlongitude: %f \naltitude: %f \ngimball_roll: %f \ngimball_yaw: %f \ngimball_pitch: %f \nflight_roll: %f \nflight_yaw: %f \nflight_pitch: %f" % (
        self.filename, self.latitude, self.longitude, self.altitude, self.gimball_roll, self.gimball_yaw,
        self.gimball_pitch, self.flight_roll, self.flight_yaw, self.flight_pitch)
class GeoPhoto:
    """Stores a satellite photo together with (latitude, longitude) for top_left and bottom_right_corner存储卫星照片以及左上角和右下角的（纬度、经度）信息
    """

    def __init__(self, filename, photo, geo_top_left, geo_bottom_right):
        self.filename = filename
        self.photo = photo
        self.top_left_coord = geo_top_left
        self.bottom_right_coord = geo_bottom_right

    def __lt__(self, other):
        return self.filename < other.filename

    def __str__(self):
        return "%s; \n\ttop_left_latitude: %f \n\ttop_left_lon: %f \n\tbottom_right_lat: %f \n\tbottom_right_lon %f " % (
        self.filename, self.top_left_coord[0], self.top_left_coord[1], self.bottom_right_coord[0],
        self.bottom_right_coord[1])
def csv_read_drone_images(filename, photo_path):
    """Builds a list with drone geo tagged photos by reading a csv file with this format:
    ""通过读取以下格式的 csv 文件，建立包含无人机地理标记照片的列表：
    文件名, 左上_平,左上_长,右下_平,右下_长
    Filename, Top_left_lat,Top_left_lon,Bottom_right_lat,Bottom_right_long
    "photo_name.png",60.506787,22.311631,60.501037,22.324467
    """
    geo_list_drone = []
    #photo_path = "./assets/query/"#无人机的文件夹路径
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # img = cv2.imread(photo_path + row[0],0)
                geo_photo = GeoPhotoDrone(photo_path + row[0], 0, float(row[1]), float(row[2]), float(row[3]),
                                          float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]),
                                          float(row[9]))
                geo_list_drone.append(geo_photo)
                line_count += 1

        print(f'Processed {line_count} lines.')
        return geo_list_drone
def csv_read_sat_map(filename,photo_path):
    """Builds a list with satellite geo tagged photos by reading a csv file with this format:
    Filename, Top_left_lat,Top_left_lon,Bottom_right_lat,Bottom_right_long
    ""通过读取以下格式的 csv 文件，建立带有卫星地理标记的照片列表：
    文件名, 左上_平,左上_长,右下_平,右下_长
    "photo_name.png",60.506787,22.311631,60.501037,22.324467
    """
    geo_list = []

    print("opening: ", filename)
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                img = cv2.imread(photo_path + row[0], 0)
                geo_photo = GeoPhoto(photo_path + row[0], img, (float(row[1]), float(row[2])),
                                     (float(row[3]), float(row[4])))
                geo_list.append(geo_photo)
                line_count += 1

        print(f'Processed {line_count} lines.')
        geo_list.sort()  # sort alphabetically by filename to ensure that the feature matcher return the right index of the matched sat image
        return geo_list
def calculate_geo_pose(geo_photo, center, features_mean, shape):
    """
    Calculates the geographical location of the drone image.
    Input: satellite geotagged image, relative pixel center of the drone image,
    (center with x = 0.5 and y = 0.5 means the located features are in the middle of the sat image)
    pixel coordinatess (horizontal and vertical) of where the features are localted in the sat image, shape of the sat image
    计算无人机图像的地理位置。
    输入：卫星地理标记图像、无人机图像的相对像素中心、
    (x = 0.5 和 y = 0.5 的中心表示所定位的地物位于卫星图像的中间）。
    卫星图像中地物定位的像素坐标（水平和垂直）、卫星图像的形状
    """
    # use ratio here instead of pixels because image is reshaped in superglue    #这里使用比例而不是像素，因为图像在superglue中会被重塑
    latitude = geo_photo.top_left_coord[0] + abs(center[1]) * (
                geo_photo.bottom_right_coord[0] - geo_photo.top_left_coord[0])
    longitude = geo_photo.top_left_coord[1] + abs(center[0]) * (
                geo_photo.bottom_right_coord[1] - geo_photo.top_left_coord[1])

    return latitude, longitude
def to_xy(image_width, image_height, top_left_lon, top_left_lat, bottom_right_lon, bottom_right_lat, lon,lat):
    # 计算经纬度变化量
    lon_per_pixel = (bottom_right_lon - top_left_lon) / image_width
    lat_per_pixel = (bottom_right_lat - top_left_lat) / image_height

    x = (lon - top_left_lon) / lon_per_pixel#列   经度
    y = (lat - top_left_lat) / lat_per_pixel#行   纬度
    geo_coordinates = [x, y]

    return geo_coordinates
#后方
def r_mat(f, w, k):
    """
    计算旋转矩阵 R

    参数:
        f: 绕 X 轴的旋转角度 (弧度)
        w: 绕 Y 轴的旋转角度 (弧度)
        k: 绕 Z 轴的旋转角度 (弧度)

    返回:
        R: 旋转矩阵
    """
    # 绕 X 轴旋转矩阵
    Rf = np.mat([[m.cos(f), 0, -m.sin(f)],
                 [0, 1, 0],
                 [m.sin(f), 0, m.cos(f)]])
    # 绕 Y 轴旋转矩阵
    Rw = np.mat([[1, 0, 0],
                 [0, m.cos(w), -m.sin(w)],
                 [0, m.sin(w), m.cos(w)]])
    # 绕 Z 轴旋转矩阵
    Rk = np.mat([[m.cos(k), -m.sin(k), 0],
                 [m.sin(k), m.cos(k), 0],
                 [0, 0, 1]])
    # 旋转矩阵 R = Rf * Rw * Rk
    R = Rf * Rw * Rk

    return R
# 定义函数 xy_approximate，用于近似计算像点坐标 x、y
def xy_approximate(X, Y, Z, x, y, Xs, Ys, Zs, R,f,xo,yo):
    """
    近似计算像点坐标 x、y

    参数:
        X: 物方点 X 坐标数组
        Y: 物方点 Y 坐标数组
        Z: 物方点 Z 坐标数组
        x: 像点 x 坐标数组
        y: 像点 y 坐标数组
        Xs: 相机投影中心 X 坐标
        Ys: 相机投影中心 Y 坐标
        Zs: 相机投影中心 Z 坐标
        R: 旋转矩阵

    返回:
        x_apxm: 近似计算的像点 x 坐标数组
        y_apxm: 近似计算的像点 y 坐标数组
    """
    x_apxm = [0, 0, 0, 0]
    y_apxm = [0, 0, 0, 0]

    # 遍历四个像点
    for i in [0, 1, 2, 3]:
        # 近似计算像点 x 坐标
        x_apxm[i] = x[i] - (xo - f * ((R[0, 0] * (X[i] - Xs) + R[1, 0] * (Y[i] - Ys) + R[2, 0] * (Z[i] - Zs))
                                      / (R[0, 2] * (X[i] - Xs) + R[1, 2] * (Y[i] - Ys) + R[2, 2] * (Z[i] - Zs))))
        # 近似计算像点 y 坐标
        y_apxm[i] = y[i] - (yo - f * ((R[0, 1] * (X[i] - Xs) + R[1, 1] * (Y[i] - Ys) + R[2, 1] * (Z[i] - Zs))
                                      / (R[0, 2] * (X[i] - Xs) + R[1, 2] * (Y[i] - Ys) + R[2, 2] * (Z[i] - Zs))))

    return x_apxm, y_apxm
# 定义函数 a_parameter，用于计算 A 矩阵参数
def a_parameter(X, Y, Z, Xs, Ys, Zs, x, y, w, k, R,f,xo,yo):
    """
    计算 A 矩阵参数

    参数:
        X: 物方点 X 坐标
        Y: 物方点 Y 坐标
        Z: 物方点 Z 坐标
        Xs: 相机投影中心 X 坐标
        Ys: 相机投影中心 Y 坐标
        Zs: 相机投影中心 Z 坐标
        x: 像点 x 坐标
        y: 像点 y 坐标
        w: 绕 Y 轴的旋转角度 (弧度)
        k: 绕 Z 轴的旋转角度 (弧度)
        R: 旋转矩阵

    返回:
        parameter: A 矩阵参数
    """
    parameter = np.zeros((2, 6))
    mean = np.zeros((3, 1))
    minus = np.zeros((3, 1))

    minus = np.array([[X - Xs],
                      [Y - Ys],
                      [Z - Zs]])
    mean = R.T * np.mat(minus)

    parameter[0][0] = (R[0, 0] * f + R[0, 2] * (x - xo)) / mean[2].item()
    parameter[0][1] = (R[1, 0] * f + R[1, 2] * (x - xo)) / mean[2].item()
    parameter[0][2] = (R[2, 0] * f + R[2, 2] * (x - xo)) / mean[2].item()
    parameter[1][0] = (R[0, 1] * f + R[0, 2] * (y - yo)) / mean[2].item()
    parameter[1][1] = (R[1, 1] * f + R[1, 2] * (y - yo)) / mean[2].item()
    parameter[1][2] = (R[2, 1] * f + R[2, 2] * (y - yo)) / mean[2].item()

    parameter[0][3] = (y - yo) * m.sin(w) - (
                ((x - xo) / f) * ((x - xo) * m.cos(k) - (y - yo) * m.sin(k)) + f * m.cos(k)) * m.cos(w)
    parameter[0][4] = -f * m.sin(k) - ((x - xo) / f) * ((x - xo) * m.sin(k) + (y - yo) * m.cos(k))
    parameter[0][5] = y - yo
    parameter[1][3] = -(x - xo) * m.sin(w) - (
                ((y - yo) / f) * ((x - xo) * m.cos(k) - (y - yo) * m.sin(k)) - f * m.cos(k)) * m.cos(w)
    parameter[1][4] = -f * m.cos(k) - ((y - yo) / f) * ((x - xo) * m.sin(k) + (y - yo) * m.cos(k))
    parameter[1][5] = -(x - xo)

    return parameter
#前方
# 计算旋转矩阵
def rotate(out_ele):
    # 计算旋转矩阵函数 out_ele 为外方位角元素的行矩阵 [fi, w, k]
    fi, w, k = out_ele[0], out_ele[1], out_ele[2]
    a1 = m.cos(fi) * m.cos(k) - m.sin(fi) * m.sin(w) * m.sin(k)
    a2 = (-1.0) * m.cos(fi) * m.sin(k) - m.sin(fi) * m.sin(w) * m.cos(k)
    a3 = (-1.0) * m.sin(fi) * m.cos(w)
    b1 = m.cos(w) * m.sin(k)
    b2 = m.cos(w) * m.cos(k)
    b3 = (-1.0) * m.sin(w)
    c1 = m.sin(fi) * m.cos(k) + m.cos(fi) * m.sin(w) * m.sin(k)
    c2 = (-1.0) * m.sin(fi) * m.sin(k) + m.cos(fi) * m.sin(w) * m.cos(k)
    c3 = m.cos(fi) * m.cos(w)
    rotate_matrix = np.array([[a1, a2, a3], [b1, b2, b3], [c1, c2, c3]])  # 使用 np.array 创建矩阵
    return rotate_matrix

# 获取投影系数
def BaseLine(X, Y, Z, rotated_l_point, rotated_r_point):
    bu = X[1] - X[0]
    bv = Y[1] - Y[0]
    bw = Z[1] - Z[0]
    n1 = (bu * rotated_r_point[2] - bw * rotated_r_point[0]) / \
         (rotated_l_point[0] * rotated_r_point[2] - rotated_r_point[0] * rotated_l_point[2])
    n2 = (bu * rotated_l_point[2] - bw * rotated_l_point[0]) / \
         (rotated_l_point[0] * rotated_r_point[2] - rotated_r_point[0] * rotated_l_point[2])
    touyingxishu = [n1, n2]
    return touyingxishu

