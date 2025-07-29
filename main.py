import os
import sys
import traceback
import webbrowser
from importlib import reload
from PIL import ImageGrab
from PySide6.QtCharts import QLineSeries
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
os.environ["QT_FONT_DPI"] = "96"
from modules import *
from modules import Settings, Ui_MainWindow
from PySide6.QtCore import Qt, Slot, QUrl
from PySide6.QtWidgets import QHeaderView, QFileDialog, QMainWindow, QDialog
from PySide6 import QtGui, QtWidgets, QtCharts
import csv
import warnings
import cv2
import torch
import ui_qian
import ui_hou
warnings.filterwarnings("ignore", message="1Torch was not compiled with flash attention.*")
torch.set_grad_enabled(False)
widgets = None
import os
from PySide6.QtGui import QPixmap, QImage
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
def wgs84_to_gauss_kruger(lon, lat):
    a = 6378137.0
    f = 1 / 298.257223563
    zone_width = 6
    lon0 = (int(lon / zone_width) * zone_width + zone_width / 2)

    e2 = 2 * f - f ** 2
    e2s = e2 / (1 - e2)
    N = a / m.sqrt(1 - e2 * m.sin(m.radians(lat)) ** 2)

    t = m.tan(m.radians(lat))
    eta2 = e2s * m.cos(m.radians(lat)) ** 2

    l = m.radians(lon - lon0)  #

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



def convert_cv_to_qimage(cv_image):

    result_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

    h, w, c = result_image.shape

    qimage = QImage(result_image.data, w, h, c * w, QImage.Format_RGB888)
    return qimage
class WorkThread(QThread):
    #自定义信号
    setimage = QtCore.Signal(QtGui.QPixmap)
    listdata = Signal(list)
    updatamap=Signal(list)
    finished = Signal()
    task_main_signal = Signal(bool, bool, str, str, str, bool, str)
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
                        latitude_truth.append(drone_image.latitude)
                        longitude_truth.append(drone_image.longitude)
                        photo = cv2.imread(drone_image.filename)

                        max_features = 0
                        located = False
                        center = None

                        rotations = [20]
                        for rot in rotations:

                            cv2.imwrite(map_path + "1_query_image.png", photo)

                            image_glob = ['*.png', '*.jpg', '*.jpeg', '*.JPG']  # 图像文件格式
                            center_new = None
                            skip = 1
                            max_length = 1000000
                            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # 'mps', 'cpu'
                            message1=str('正在设备 "{}" 上运行推断'.format(device))
                            self.message.emit(message1)
                            print('正在设备 \"{}\" 上运行推断'.format(device))

                            extractor, matcher = load_extractor_matcher(feature_type, device, max_num_keypoints)
                            vs = VideoStreamer(map_path, skip, image_glob, max_length)

                            frame_uav, ret = vs.next_frame()
                            assert ret, '读取第一帧时出错（尝试不同的 --input？）'
                            frame_uav_tensor = lightglue.utils.numpy_image_to_torch(frame_uav)
                            last_data = extractor.extract(frame_uav_tensor.to(device))
                            # 600 800 3
                            query_image_new = frame_uav
                            last_image_id = 0

                            if output_dir is not None:
                                print('==> 将输出写入到 {}'.format(output_dir))
                                message2 = str('将输出写入到 {}'.format(output_dir))
                                self.message.emit(message2)
                                Path(output_dir).mkdir(exist_ok=True)

                            satellite_map_index_new = None
                            index = 0
                            feature_number = -1
                            located_image_new = None
                            features_mean_new = [0, 0]

                            while True:
                                # 当前要匹配的卫星影像
                                frame, ret = vs.next_frame()  # 下一张影像，从这里开始就是卫星影像

                                if not ret:
                                    print('完成 demo_superglue.py')
                                    message3 = '完成 demo_superglue.py'
                                    self.message.emit(message3)
                                    break
                                stem0, stem1 = last_image_id, vs.i - 1
                                frame_tensor = lightglue.utils.numpy_image_to_torch(frame)

                                pred = extractor.extract(frame_tensor.to(device))
                                matches01 = matcher({"image0": last_data, "image1": pred})

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
                                        center_new = (cX, cY)
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
                                color = (255, 0, 0)
                                ###这里可以控制是否显示特征点标记
                                out = viz2d.make_matching_plot_fast(
                                    query_image_new, frame, kpts0, kpts1, mkpts0, mkpts1, color, text='',
                                    path=None, show_keypoints=show_keypoints, small_text='')

                                if MATCHED:
                                    located_image_new = out
                                ##显示弹窗
                                if display:
                                    out = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
                                    h, w, c = out.shape
                                    qimage = QPixmap.fromImage(QImage(out.data, w, h, c * w, QImage.Format_RGB888))
                                    # 信号.emit(值）
                                    self.setimage.emit(qimage)


                                index += 1

                            torch.cuda.empty_cache()

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
                            # 转化成高斯克吕格投影坐标
                            # 进行坐标转换wgs84_to_gauss_kruger( current_location[0], current_location[1])
                            x, y = wgs84_to_gauss_kruger( current_location[1], current_location[0])
                            result_data = [str(photo_name), str(current_location[1]), str(current_location[0]), x,y]  # 获取您的结果数据
                            self.listdata.emit(result_data)  # 发射信号，传递结果数据
                            # 发射更新map的信号
                            updata_map = [current_location[1], current_location[0]]
                            self.updatamap.emit(updata_map)

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
                            file_exists = os.path.isfile(path)
                            with open(path, 'a', encoding='UTF8',newline="") as f:
                                writer = csv.writer(f)
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
    setimage_tiqu_result = QtCore.Signal(QtGui.QPixmap)
    setimage_pipei_result = QtCore.Signal(QtGui.QPixmap)
    setimage_video_result = QtCore.Signal(QtGui.QPixmap)
    setimage_jiaozheng_result= QtCore.Signal(QtGui.QPixmap)
    setimage_jiaozheng_right = QtCore.Signal(QtGui.QPixmap)
    task_tiqu_signal = Signal(str, str,str,int,int)
    task_pipei_signal = Signal(str, str,str,int,int)
    task_jiaozheng_signal = Signal(str, str, str, int, int)
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
                    ]
                    kpts0, kpts1, matches = feats0["keypoints"], feats1["keypoints"], matches01["matches"]
                    m_kpts0, m_kpts1 = kpts0[matches[..., 0]], kpts1[matches[..., 1]]
                    plot_image = viz2d.plot_images([image0, image1])#拼接图像
                    kpc0, kpc1 = viz2d.cm_prune(matches01["prune0"]), viz2d.cm_prune(matches01["prune1"])
                    plot_image_keypoints = viz2d.plot_keypoints(plot_image, [m_kpts0, m_kpts1], wide1, colors=[kpc0, kpc1], radius=3)
                    plot_image_keypoints_cv=lightglue.utils.torch_to_numpy(plot_image_keypoints)
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
                    matches01 = matcher({'image0': feats0, 'image1': feats1})
                    feats0, feats1, matches01 = [ lightglue.utils.rbd(x) for x in [feats0, feats1, matches01]]  # remove batch dimension
                    matches = matches01['matches']
                    points0 = feats0['keypoints'][matches[..., 0]]  # coordinates in image #0, shape (K,2)
                    points1 = feats1['keypoints'][matches[..., 1]]  # coordinates in image #1, shape (K,2)
                    points_left = points0.cpu().numpy().astype(np.float32)
                    points_right = points1.cpu().numpy().astype(np.float32)
                    matrix, mask = cv2.findHomography(points_right, points_left, cv2.RANSAC, 5.0)  # Using RANSAC method
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


                    # 使用布尔索引进行拼接
                    mask = (warp_image_ != 0).any(axis=2)
                    final_image[mask] = warp_image_[mask]

                    final_image0 = remove_black_border(final_image)
                    self.image3 = final_image0
                    final_image_0 = cv2.cvtColor(final_image0, cv2.COLOR_BGR2RGB)
                    h2, w2, c2 = final_image_0.shape
                    qimage_final_image = QPixmap.fromImage(QImage(final_image_0.data, w2, h2, c2 * w2, QImage.Format_RGB888))
                    self.setimage_jiaozheng_result.emit(qimage_final_image)

                    self.reset_state()


                else:
                    print("开始执行视频模式")
                    torch.set_grad_enabled(False)
                    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

                    extractor1 = SuperPoint(max_num_keypoints=500).eval().to(device)
                    extractor2 = SuperPoint(max_num_keypoints=10000).eval().to(device)
                    matcher = LightGlue(features="superpoint").eval().to(device)
                    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
                    ret0, image0_cv = cap.read()
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
                    self.reset_state()
            except Exception as e:
                print(f"线程运行错误：{e}")
            finally:
                self.mutex.unlock()
        self.finished.emit()

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

                message111 = ["开始运行","后方交会!"]
                self.message.emit(message111)
                distance1 = m.sqrt((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2)

                distance2 = m.sqrt((X[1] - X[0]) ** 2 + (Y[1] - Y[0]) ** 2)

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
                        print("级数不收敛，中间结果为：")
                        break

                # 打印结果
                if flag <= 100:
                    print("级数收敛，最终结果为：")

                print(" Xs=%f,\n Ys=%f,\n Zs=%f,\n f=%f,\n w=%f,\n k=%f" % (Xos, Yos, Zos, fo, wo, ko))

                message3 = ["级数收敛，最终结果为：",str("Xs="+str(Xos)+" , "+"Ys="+str(Yos)+" , "+"Zs="+str(Zos)+" , "+"f=" + str(fo) + " , " + "w=" + str(wo) + " , " + "k=" + str(ko) + " ；")]
                self.message.emit(message3)
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
    geo_list_drone = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                geo_photo = GeoPhotoDrone(photo_path + row[0], 0, float(row[1]), float(row[2]), float(row[3]),
                                          float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]),
                                          float(row[9]))
                geo_list_drone.append(geo_photo)
                line_count += 1

        print(f'Processed {line_count} lines.')
        return geo_list_drone
def csv_read_sat_map(filename,photo_path):
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
        geo_list.sort()
        return geo_list
def calculate_geo_pose(geo_photo, center, features_mean, shape):
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


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        # APP NAME
        title = "GNSS拒止下的无人机视觉定位"
        description = "GNSS拒止下的无人机视觉定位"
        # 添加标题（label）
        self.setWindowTitle(title)
        self.points=[]
        widgets.titleRightInfo.setText(description)
        themeFile = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '_internal', 'py_dracula_light.qss')
        UIFunctions.theme(self, themeFile, True)
        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget_result.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.btn_fun1.clicked.connect(self.buttonClick)
        widgets.pushButton_tiqu.clicked.connect(self.buttonClick)
        widgets.pushButton_pipei.clicked.connect(self.buttonClick)
        widgets.pushButton_video.clicked.connect(self.buttonClick)
        widgets.pushButton_fanhui_tiqu.clicked.connect(self.buttonClick)
        widgets.pushButton_fanhui_pipei_2.clicked.connect(self.buttonClick)
        widgets.pushButton_fanhui_pipei.clicked.connect(self.buttonClick)
        widgets.pushButton_fanhui_video.clicked.connect(self.buttonClick)
        widgets.pushButton.clicked.connect(self.buttonClick)
        widgets.btn_jingdu.clicked.connect(self.buttonClick)
        widgets.btn_help.clicked.connect(self.buttonClick)
        widgets.btn_message.clicked.connect(self.open_netease_mail)
        widgets.btn_logout.clicked.connect(self.open_survey)
        widgets.btn_print.clicked.connect(self.print_)


        #EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # 设置窗口大小
        self.resize(1500, 870)
        self.show()

        # SET HACKS
        AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        widgets.closeAppBtn.clicked.connect(self.close_application)

    ####################################################无人机定位######################################################
        #显示关键点
        self.ui.checkBox_show_keypoints.setChecked(False)
        self.ui.checkBox_show_keypoints.stateChanged.connect(self.on_show_keypoints_changed)
        #显示匹配过程
        self.ui.checkBox_display.setChecked(False)
        self.ui.checkBox_display.stateChanged.connect(self.on_display_changed)
        #导出结果
        self.ui.checkBox_WRITE_RESULT.setChecked(False)
        self.ui.checkBox_WRITE_RESULT.stateChanged.connect(self.on_write_result_changed)
        #选择地图文件
        self.ui.pushButton_map_path.clicked.connect(self.select_map_path)
        #选择无人机文件
        self.ui.pushButton_query_path.clicked.connect(self.select_query_path)
        #选择输出结果文件
        self.ui.pushButton_output_dir.clicked.connect(self.select_output_path)
        #特征提取算法
        self.ui.comboBox_feature_type.currentIndexChanged.connect(self.on_feature_type_changed)

        #保存

        self.ui.pushButton_save_tiqu.clicked.connect(self.save_image_tiqu)
        self.ui.pushButton_save_pipei.clicked.connect(self.save_image_pipei)
        self.ui.pushButton_save_pipei_2.clicked.connect(self.save_image_jiaozheng)
        self.ui.clear_tiqu.clicked.connect(self.clear_tiqu)
        self.ui.clear_pipei.clicked.connect(self.clear_pipei)
        self.ui.clear_pipei_2.clicked.connect(self.clear_jiaozheng)
        self.ui.clear_shipin.clicked.connect(self.clear_shipin)
        #初始化无人机定位参数
        self.show_keypoints = False
        self.display =  False
        self.map_path = None  # 存放卫星地图的文件夹
        self.query_path = None # 存放待匹配无人机的文件夹
        self.output_dir = None # 输出结果文件夹路径（匹配过程路径）
        self.display = False  # 是否显示弹窗
        self.WRITE_RESULT = False  # 是否生成结果excel表格
        self.feature_type = None  # 这里支持选择提起特征提取算法；SuperPoint，DISK、ALIKED、SIFT、DoGHardNet
        #创建无人机匹配子线程
        self.worker = WorkThread()
        #相关槽函数
        self.worker.start()
        self.worker.setimage.connect(self.set_image)#更新匹配过程
        self.worker.listdata.connect(self.update_table)#更新结果
        self.worker.updatamap.connect(self.updata_map)#更新大地图
        self.worker.finished.connect(self.task_finished)#子线程结束标志

        self.worker.task_main_signal.connect(self.worker.process_signal)
        self.worker.message.connect(self.set_message)

        self.ui.tableWidget_view.setStyleSheet("""
    QTableView {
        gridline-color: transparent;
    }
    QHeaderView::section {
        border: none;
    }
""")
        # self.worker.start()
        #点击运行后，开始进行无人机匹配
        widgets.run_button.clicked.connect(self.run_main)
        widgets.btn_save.clicked.connect(self.save_result)

        #点击结束后停止当前无人机匹配
        widgets.pushButton_stop.clicked.connect(self.stop_thread)
        # 读取大地图
        if sys.version_info[0] < 3:
            reload(sys)
            sys.setdefaultencoding('utf-8')

        img_path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '_internal', 'map_patch.jpg')
        self.map_image = cv2.imread(img_path)

        self.ui.btn_clear_result.clicked.connect(self.clear_result)

        ####################################################子功能模块##################################################################
        #加载影像
        self.ui.pushButton_load_image1_tiqu.clicked.connect(self.load_image1_tiqu)
        self.ui.pushButton_load_image2_tiqu.clicked.connect(self.load_image2_tiqu)
        self.ui.pushButton_load_image1_pipei.clicked.connect(self.load_image1_pipei)
        self.ui.pushButton_load_image2_pipei.clicked.connect(self.load_image2_pipei)
        self.ui.pushButton_load_image1_pipei_2.clicked.connect(self.load_image1_jiaozheng)
        self.ui.pushButton_load_image2_pipei_2.clicked.connect(self.load_image2_jiaozheng)

        #选择特征提取算法
        self.ui.comboBox_feature_type_tiqu.currentIndexChanged.connect(self.on_feature_type_changed_tiqu)
        self.ui.comboBox_feature_type_pipei.currentIndexChanged.connect(self.on_feature_type_changed_pipei)
        self.ui.comboBox_feature_type_pipei_2.currentIndexChanged.connect(self.on_feature_type_changed_jiaozheng)
        #输入最大特征点
        self.ui.lineEdit_tiqu.textChanged.connect(self.on_text_changed_tiqu)
        self.ui.lineEdit_pipei.textChanged.connect(self.on_text_changed_pipei)
        self.ui.lineEdit_pipei_2.textChanged.connect(self.on_text_changed_jiaozheng)

        #初始化参数
        self.max_keypoint=None
        self.image1=None
        self.image2 = None
        self.feature_type_fun=None
        self.type=None
        #创建线程
        self.fun1 = Fun1()
        # 相关槽函数
        self.fun1.setimage_pipei_result.connect(self.set_pipei)
        self.fun1.setimage_tiqu_result.connect(self.set_tiqu)
        self.fun1.setimage_video_result.connect(self.set_video)
        self.fun1.setimage_jiaozheng_result.connect(self.set_jiaozheng)
        self.fun1.setimage_jiaozheng_right.connect(self.set_jiaozheng_right)
        self.fun1.finished.connect(self.task_finished_fun1)  # 子线程结束标志

        self.fun1.task_tiqu_signal.connect(self.fun1.process_signal)
        self.fun1.task_pipei_signal.connect(self.fun1.process_signal)
        self.fun1.task_video_signal.connect(self.fun1.process_signal)
        self.fun1.task_jiaozheng_signal.connect(self.fun1.process_signal)
        self.fun1.start()

        # 点击后开始运行相关模块
        widgets.pushButton_run_tiqu.clicked.connect(self.run_tiqu)
        widgets.pushButton_run_pipei.clicked.connect(self.run_pipei)
        widgets.pushButton_run_pipei_2.clicked.connect(self.run_jiaozheng)
        widgets.pushButton_video_run.clicked.connect(self.run_video)


        widgets.btn_exit.clicked.connect(self.stop_video)


        #######################################对话框
        self.houfang = Houfang()
        widgets.pushButton_backward.clicked.connect(self.start_hou)
        self.dialog_hou = QDialog()
        self.ui_hou = ui_hou.Ui_Dialog()
        self.ui_hou.setupUi(self.dialog_hou)
        self.ui_hou.pushButton_run.clicked.connect(self.run_hou)
        self.houfang.hou_task_signal.connect(self.houfang.process_signal)
        self.houfang.message.connect(self.hf_set_message)
        self.ui_hou.pushButton_load_houfang.clicked.connect(self.load_hou)
        self.houfang.start()


        #######qian
        self.qianfang =Qianfang()
        widgets.pushButton_forward.clicked.connect(self.start_qian)
        self.dialog_qian = QDialog()
        self.dialog_qian.setWindowTitle("请输入前方交会参数")
        self.ui_qian = ui_qian.Ui_Dialog()
        self.ui_qian.setupUi(self.dialog_qian)
        self.ui_qian.pushButton_run.clicked.connect(self.run_qian)
        self.qianfang.qian_task_signal.connect(self.qianfang.process_signal)
        self.qianfang.message.connect(self.hf_set_message)
        self.ui_qian.pushButton_load_qianfang.clicked.connect(self.load_qian)
        self.qianfang.start()

        ##精度评定
        self.ui.pushButton_jisuan.clicked.connect(self.data_display_1)
        self.ui.pushButton_real.clicked.connect(self.data_display_2)
        self.ui.btn_clear_result_jingdu.clicked.connect(self.clear_jingdu)
        #初始化
        self.chart = QtCharts.QChart()  # 创建 Chart
        self.ui.graphicsView.setChart(self.chart)
        # 设置标题文本
        title_text = "精度评定"
        # 创建 QFont 对象并设置字体和大小
        title_font = QFont("Microsoft YaHei", 18)  # 使用微软雅黑字体，大小为12
        # 设置图表的标题
        self.chart.setTitle(title_text)
        # 将设置的字体应用到标题上
        self.chart.setTitleFont(title_font)
        self.axis_y = QtCharts.QValueAxis()  # 创建坐标轴
        self.axis_y.setRange(22.4600, 22.4690)  # 设置坐标轴的范围
        self.axis_y.setTitleText('经度')  # 设置坐标轴的标题
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)  # 添加x轴到图表底部
        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setRange(60.4012, 60.4055)
        self.axis_x.setTitleText('纬度')
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)  # 添加y轴到图表左侧

    def clear_result(self):
        row_count = self.ui.tableWidget_result.rowCount()
        # 从第二行开始，逐行删除
        for row in range(row_count - 1, 0, -1):
            self.ui.tableWidget_result.removeRow(row)
        self.ui.tableWidget_result.setRowCount(27)

    def data_display_1(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("CSV 文件 (*.csv)")  # 设置文件过滤器，仅显示 CSV 文件
        file_dialog.setFileMode(QFileDialog.ExistingFile)  # 设置文件选择模式为选择现有文件
        if file_dialog.exec():
            file_paths = file_dialog.selectedFiles()  # 获取用户选择的文件路径
            file_path = file_paths[0]  # 获取第一个文件路径
            self.series_xy = QtCharts.QScatterSeries()  # 创建散点数据序列
            self.series_xy.setName("计算结果点")  # 设置数据序列的
            # 创建一个空列表来存储读取的值
            data = []
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    # 将每行的数据以 (x, y) 元组形式添加到数据列表中
                    data.append((float(row[1]), float(row[0])))

            # 如果数据不是按照 x 值排序，可以在这里进行排序
            # data.sort()

            # 将数据添加到散点数据序列中
            for x, y in data:
                self.series_xy.append(x, y)

            self.chart.addSeries(self.series_xy)  # 图表中添加数据序列
            self.series_xy.attachAxis(self.axis_x)  # 将数据序列与x轴关联
            self.series_xy.attachAxis(self.axis_y)  # 将数据序列与y轴关联

            self.line_series = QLineSeries()  # 创建折线数据序列
            self.line_series.setName("计算结果连线")

            if self.line_series not in self.chart.series():
                points = sorted(self.series_xy.points(), key=lambda point: point.x())
                for point in points:
                    self.line_series.append(point)
                self.chart.addSeries(self.line_series)  # 图表中添加折线数据序列
                self.line_series.attachAxis(self.axis_x)  # 将折线数据序列与x轴关联
                self.line_series.attachAxis(self.axis_y)  # 将折线数据序列与y轴关联
    def data_display_2(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("CSV 文件 (*.csv)")  # 设置文件过滤器，仅显示 CSV 文件
        file_dialog.setFileMode(QFileDialog.ExistingFile)  # 设置文件选择模式为选择现有文件
        if file_dialog.exec():
            file_paths = file_dialog.selectedFiles()  # 获取用户选择的文件路径
            file_path = file_paths[0]  # 获取第一个文件路径
            self.series_xy2 = QtCharts.QScatterSeries()  # 创建散点数据序列
            self.series_xy2.setName("真实结果点")  # 设置数据序列的名
            # 创建一个空列表来存储读取的值
            data = []
            # 读取CSV文件
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    # 将每行的数据以 (x, y) 元组形式添加到数据列表中
                    data.append((float(row[1]), float(row[0])))

            # 如果数据不是按照 x 值排序，可以在这里进行排序
            # data.sort()

            # 将数据添加到散点数据序列中
            for x, y in data:
                self.series_xy2.append(x, y)

            self.chart.addSeries(self.series_xy2)  # 图表中添加数据序列
            self.series_xy2.attachAxis(self.axis_x)  # 将数据序列与x轴关联
            self.series_xy2.attachAxis(self.axis_y)  # 将数据序列与y轴关联

            self.line_series2 = QLineSeries()  # 创建折线数据序列
            self.line_series2.setName("真实结果连线")

            if self.line_series2 not in self.chart.series():
                points = sorted(self.series_xy2.points(), key=lambda point: point.x())
                for point in points:
                    self.line_series2.append(point)
                self.chart.addSeries(self.line_series2)  # 图表中添加折线数据序列
                self.line_series2.attachAxis(self.axis_x)  # 将折线数据序列与x轴关联
                self.line_series2.attachAxis(self.axis_y)  # 将折线数据序列与y轴关联
    def clear_jingdu(self):
        # self.line_series.clear()
        # self.line_series2.clear()
        # self.series_xy.clear()
        # self.series_xy2.clear()
        self.chart.removeAllSeries()

    def stop_video(self):
        self.ui.label_video_zhuangtai.setText("关闭摄像头")
        self.fun1.if_video_runing = False

    def clear_tiqu(self):
        self.ui.label_tiqu_left.clear()
        self.ui.label_tiqu_right.clear()
        self.ui.label_tiqu_result.clear()
        self.ui.label_tiqu_zhuangtai.setText("成功清空")

    def clear_pipei(self):
        self.ui.label_pipei_left.clear()
        self.ui.label_pipei_right.clear()
        self.ui.label_pipei_result.clear()
        self.ui.label_pipei_zhuangtai.setText("成功清空")

    def clear_jiaozheng(self):
        self.ui.label_pipei_left_2.clear()
        self.ui.label_pipei_right_2.clear()
        self.ui.label_pipei_result_2.clear()
        self.ui.label_pipei_zhuangtai_2.setText("成功清空")

    def clear_shipin(self):
        self.ui.label_video.clear()
        self.ui.label_video_zhuangtai.setText("成功清空")

    def run_hou(self):
        # 检查每个 LineEdit 的输入是否能转换为浮点数
        inputs = {
            "X1": self.ui_hou.lineEdit_X1.text(),
            "Y1": self.ui_hou.lineEdit_Y1.text(),
            "Z1": self.ui_hou.lineEdit_Z1.text(),
            "X2": self.ui_hou.lineEdit_X2.text(),
            "Y2": self.ui_hou.lineEdit_Y2.text(),
            "Z2": self.ui_hou.lineEdit_Z2.text(),
            "X3": self.ui_hou.lineEdit_X3.text(),
            "Y3": self.ui_hou.lineEdit_Y3.text(),
            "Z3": self.ui_hou.lineEdit_Z3.text(),
            "X4": self.ui_hou.lineEdit_X4.text(),
            "Y4": self.ui_hou.lineEdit_Y4.text(),
            "Z4": self.ui_hou.lineEdit_Z4.text(),
            "x1": self.ui_hou.lineEdit_x1.text(),
            "y1": self.ui_hou.lineEdit_y1.text(),
            "x2": self.ui_hou.lineEdit_x2.text(),
            "y2": self.ui_hou.lineEdit_y2.text(),
            "x3": self.ui_hou.lineEdit_x3.text(),
            "y3": self.ui_hou.lineEdit_y3.text(),
            "x4": self.ui_hou.lineEdit_x4.text(),
            "y4": self.ui_hou.lineEdit_y4.text(),
            "f": self.ui_hou.lineEdit_f.text(),
        }

        invalid_inputs = []
        for key, value in inputs.items():
            try:
                float(value)
            except ValueError:
                invalid_inputs.append(key)

        if invalid_inputs:
            # 构建提示消息
            message = "以下输入不正确：\n" + "\n".join(invalid_inputs)
            # 弹出提醒窗口
            QtWidgets.QMessageBox.warning(self, "警告", message)
            return

        # 如果所有输入都正确，继续执行任务
        X1 = float(self.ui_hou.lineEdit_X1.text())
        Y1 = float(self.ui_hou.lineEdit_Y1.text())
        Z1 = float(self.ui_hou.lineEdit_Z1.text())
        X2 = float(self.ui_hou.lineEdit_X2.text())
        Y2 = float(self.ui_hou.lineEdit_Y2.text())
        Z2 = float(self.ui_hou.lineEdit_Z2.text())
        X3 = float(self.ui_hou.lineEdit_X3.text())
        Y3 = float(self.ui_hou.lineEdit_Y3.text())
        Z3 = float(self.ui_hou.lineEdit_Z3.text())
        X4 = float(self.ui_hou.lineEdit_X4.text())
        Y4 = float(self.ui_hou.lineEdit_Y4.text())
        Z4 = float(self.ui_hou.lineEdit_Z4.text())
        x1 = float(self.ui_hou.lineEdit_x1.text())
        y1 = float(self.ui_hou.lineEdit_y1.text())
        x2 = float(self.ui_hou.lineEdit_x2.text())
        y2 = float(self.ui_hou.lineEdit_y2.text())
        x3 = float(self.ui_hou.lineEdit_x3.text())
        y3 = float(self.ui_hou.lineEdit_y3.text())
        x4 = float(self.ui_hou.lineEdit_x4.text())
        y4 = float(self.ui_hou.lineEdit_y4.text())
        f = float(self.ui_hou.lineEdit_f.text())

        X = [X1, X2, X3, X4]
        Y = [Y1, Y2, Y3, Y4]
        Z = [Z1, Z2, Z3, Z4]
        x = [x1, x2, x3, x4]
        y = [y1, y2, y3, y4]

        self.houfang.hou_task_signal.emit(X, Y, Z, x, y, f)
        # 关闭对话框
        self.dialog_hou.close()

    def load_hou(self):
        try:
            file_dialog = QFileDialog()
            file_dialog.setNameFilter("txt 文件 (*.txt)")  # 设置文件过滤器，仅显示 TXT 文件
            file_dialog.setFileMode(QFileDialog.ExistingFile)  # 设置文件选择模式为选择现有文件
            if file_dialog.exec():
                file_paths = file_dialog.selectedFiles()  # 获取用户选择的文件路径
                file_path = file_paths[0]  # 获取第一个文件路径

            with open(file_path, encoding="utf-8") as file:
                data_hou = file.read()

            lines_hou = data_hou.split("\n")
            hou_dic = {}
            for line_hou in lines_hou:
                list_hou = line_hou.split(",")
                hou_dic[list_hou[0]] = list_hou[1:]

            # 设置 LineEdit 的文本
            self.ui_hou.lineEdit_X1.setText(hou_dic["X"][0])
            self.ui_hou.lineEdit_Y1.setText(hou_dic["Y"][0])
            self.ui_hou.lineEdit_Z1.setText(hou_dic["Z"][0])
            self.ui_hou.lineEdit_X2.setText(hou_dic["X"][1])
            self.ui_hou.lineEdit_Y2.setText(hou_dic["Y"][1])
            self.ui_hou.lineEdit_Z2.setText(hou_dic["Z"][1])
            self.ui_hou.lineEdit_X3.setText(hou_dic["X"][2])
            self.ui_hou.lineEdit_Y3.setText(hou_dic["Y"][2])
            self.ui_hou.lineEdit_Z3.setText(hou_dic["Z"][2])
            self.ui_hou.lineEdit_X4.setText(hou_dic["X"][3])
            self.ui_hou.lineEdit_Y4.setText(hou_dic["Y"][3])
            self.ui_hou.lineEdit_Z4.setText(hou_dic["Z"][3])
            self.ui_hou.lineEdit_x1.setText(hou_dic["x"][0])
            self.ui_hou.lineEdit_y1.setText(hou_dic["y"][0])
            self.ui_hou.lineEdit_x2.setText(hou_dic["x"][1])
            self.ui_hou.lineEdit_y2.setText(hou_dic["y"][1])
            self.ui_hou.lineEdit_x3.setText(hou_dic["x"][2])
            self.ui_hou.lineEdit_y3.setText(hou_dic["y"][2])
            self.ui_hou.lineEdit_x4.setText(hou_dic["x"][3])
            self.ui_hou.lineEdit_y4.setText(hou_dic["y"][3])
            self.ui_hou.lineEdit_f.setText(hou_dic["f"][0])
        except Exception as e:
            # 获取完整的异常堆栈信息
            error_message = traceback.format_exc()
            # 弹出错误提示窗口并显示完整的异常信息
            error_dialog = QtWidgets.QMessageBox(self)
            error_dialog.setWindowTitle("错误")
            error_dialog.setText("发生异常，请查看详细信息。")
            error_dialog.setDetailedText(error_message)
            error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            error_dialog.resize(800, 600)  # 设置消息框的初始大小
            error_dialog.exec()

    def start_hou(self):
        # 显示对话框
        self.dialog_hou.setWindowTitle("请输入后方交会参数")
        self.dialog_hou.resize(880, 210)
        self.dialog_hou.exec_()

    def run_qian(self):
        # 检查每个 LineEdit 的输入是否能转换为浮点数
        inputs = {
            "X1": self.ui_qian.lineEdit_X1.text(),
            "X2": self.ui_qian.lineEdit_X2.text(),
            "Y1": self.ui_qian.lineEdit_Y1.text(),
            "Y2": self.ui_qian.lineEdit_Y2.text(),
            "Z1": self.ui_qian.lineEdit_Z1.text(),
            "Z2": self.ui_qian.lineEdit_Z2.text(),
            "x1": self.ui_qian.lineEdit_x1.text(),
            "y1": self.ui_qian.lineEdit_y1.text(),
            "f1": self.ui_qian.lineEdit_f1.text(),
            "fai1": self.ui_qian.lineEdit_fai1.text(),
            "oumiga1": self.ui_qian.lineEdit_oumiga1.text(),
            "k1": self.ui_qian.lineEdit_k1.text(),
            "x2": self.ui_qian.lineEdit_x2.text(),
            "y2": self.ui_qian.lineEdit_y2.text(),
            "f2": self.ui_qian.lineEdit_f2.text(),
            "fai2": self.ui_qian.lineEdit_fai2.text(),
            "oumiga2": self.ui_qian.lineEdit_oumiga2.text(),
            "k2": self.ui_qian.lineEdit_k2.text(),
        }

        invalid_inputs = []
        for key, value in inputs.items():
            try:
                float(value)
            except ValueError:
                invalid_inputs.append(key)

        if invalid_inputs:
            # 构建提示消息
            message = "以下输入不正确：\n" + "\n".join(invalid_inputs)
            # 弹出提醒窗口
            QtWidgets.QMessageBox.warning(self, "警告", message)
            return

        # 如果所有输入都正确，继续执行任务
        X1 = float(self.ui_qian.lineEdit_X1.text())
        X2 = float(self.ui_qian.lineEdit_X2.text())
        Y1 = float(self.ui_qian.lineEdit_Y1.text())
        Y2 = float(self.ui_qian.lineEdit_Y2.text())
        Z1 = float(self.ui_qian.lineEdit_Z1.text())
        Z2 = float(self.ui_qian.lineEdit_Z2.text())
        x1 = float(self.ui_qian.lineEdit_x1.text())
        y1 = float(self.ui_qian.lineEdit_y1.text())
        f1 = float(self.ui_qian.lineEdit_f1.text())
        fai1 = float(self.ui_qian.lineEdit_fai1.text())
        oumiga1 = float(self.ui_qian.lineEdit_oumiga1.text())
        k1 = float(self.ui_qian.lineEdit_k1.text())
        x2 = float(self.ui_qian.lineEdit_x2.text())
        y2 = float(self.ui_qian.lineEdit_y2.text())
        f2 = float(self.ui_qian.lineEdit_f2.text())
        fai2 = float(self.ui_qian.lineEdit_fai2.text())
        oumiga2 = float(self.ui_qian.lineEdit_oumiga2.text())
        k2 = float(self.ui_qian.lineEdit_k2.text())

        X = [X1, X2]
        Y = [Y1, Y2]
        Z = [Z1, Z2]
        x = [x1, x2]
        y = [y1, y2]
        f = [f1, f2]
        fai = [fai1, fai2]
        oumiga = [oumiga1, oumiga2]
        k = [k1, k2]

        self.qianfang.qian_task_signal.emit(X, Y, Z, x, y, f, fai, oumiga, k)
        # 关闭对话框
        self.dialog_qian.close()

    def load_qian(self):
        try:
            file_dialog = QFileDialog()
            file_dialog.setNameFilter("txt 文件 (*.txt)")  # 设置文件过滤器，仅显示 CSV 文件
            file_dialog.setFileMode(QFileDialog.ExistingFile)  # 设置文件选择模式为选择现有文件
            if file_dialog.exec():
                file_paths = file_dialog.selectedFiles()  # 获取用户选择的文件路径
                file_path = file_paths[0]  # 获取第一个文件路径
            with open(file_path, encoding="utf-8") as file:
                data_qian = file.read()
            lines_qian = data_qian.split("\n")
            qian_dic = {}
            for line_qian in lines_qian:
                list_qian = line_qian.split(",")
                qian_dic[list_qian[0]] = list_qian[1:]

            self.ui_qian.lineEdit_X1.setText(qian_dic["模型基线向量Xs"][0])
            self.ui_qian.lineEdit_X2.setText(qian_dic["模型基线向量Xs"][1])
            self.ui_qian.lineEdit_Y1.setText(qian_dic["模型基线向量Ys"][0])
            self.ui_qian.lineEdit_Y2.setText(qian_dic["模型基线向量Ys"][1])
            self.ui_qian.lineEdit_Z1.setText(qian_dic["模型基线向量Zs"][0])
            self.ui_qian.lineEdit_Z2.setText(qian_dic["模型基线向量Zs"][1])
            self.ui_qian.lineEdit_x1.setText(qian_dic["像点坐标x"][0])
            self.ui_qian.lineEdit_y1.setText(qian_dic["像点坐标y"][0])
            self.ui_qian.lineEdit_f1.setText(qian_dic["像片主距f"][0])
            self.ui_qian.lineEdit_fai1.setText(qian_dic["偏角(φ)"][0])
            self.ui_qian.lineEdit_oumiga1.setText(qian_dic["倾角(ω)"][0])
            self.ui_qian.lineEdit_k1.setText(qian_dic["旋角(r)"][0])
            self.ui_qian.lineEdit_x2.setText(qian_dic["像点坐标x"][1])
            self.ui_qian.lineEdit_y2.setText(qian_dic["像点坐标y"][1])
            self.ui_qian.lineEdit_f2.setText(qian_dic["像片主距f"][1])
            self.ui_qian.lineEdit_fai2.setText(qian_dic["偏角(φ)"][1])
            self.ui_qian.lineEdit_oumiga2.setText(qian_dic["倾角(ω)"][1])
            self.ui_qian.lineEdit_k2.setText(qian_dic["旋角(r)"][1])
        except Exception as e:
            # 获取完整的异常堆栈信息
            error_message = traceback.format_exc()
            # 弹出错误提示窗口并显示完整的异常信息
            error_dialog = QtWidgets.QMessageBox(self)
            error_dialog.setWindowTitle("错误")
            error_dialog.setText("发生异常，请查看详细信息。")
            error_dialog.setDetailedText(error_message)
            error_dialog.setIcon(QtWidgets.QMessageBox.Critical)
            error_dialog.resize(800, 600)  # 设置消息框的初始大小
            error_dialog.exec()
    def start_qian(self):
        # 显示对话框
        self.dialog_qian.setWindowTitle("请输入前方交会参数")
        self.dialog_qian.resize(810, 330)
        self.dialog_qian.exec_()

    def run_tiqu(self):
        print("run_tiqu")
        self.ui.label_tiqu_zhuangtai.setText("开始运行：影像特征提取！")
        self.type=1;
        self.fun1.task_tiqu_signal.emit(self.feature_type_fun,self.image1, self.image2,self.max_keypoint,self.type)
    def run_pipei(self):
        self.ui.label_pipei_zhuangtai.setText("开始运行：影像特征匹配！")
        self.type=2;
        self.fun1.task_pipei_signal.emit(self.feature_type_fun, self.image1, self.image2, self.max_keypoint,self.type)

    def run_jiaozheng(self):
        self.ui.label_pipei_zhuangtai_2.setText("开始运行：智能影像矫正！")
        self.type=3;
        self.fun1.task_jiaozheng_signal.emit(self.feature_type_fun, self.image1, self.image2, self.max_keypoint,self.type)
    def run_video(self):
        self.type=4
        print("开始打开视频")
        self.ui.label_video_zhuangtai.setText("开始摄像头")
        self.fun1.task_video_signal.emit("video","video","video",10000, self.type)

    def open_netease_mail(self):
        recipient = "y18710398356@163.com"
        subject = "意见反馈"
        mailto_url = f"mailto:{recipient}?subject={subject}"
        # 尝试打开邮箱客户端
        if not webbrowser.open(mailto_url):
            # 如果无法打开，则显示提示框
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("没有找到邮箱客户端")
            msg.setWindowTitle("提示")
            msg.exec()
        webbrowser.open(mailto_url)

    def open_survey(self):
        # 在默认浏览器中打开调查问卷网页
        url = QUrl("https://www.wjx.cn/vm/m3tysxK.aspx# ")
        QDesktopServices.openUrl(url)

    def print_(self):
        # 获取整个屏幕截图
        screenshot = ImageGrab.grab()

        # 创建一个 QPrinter 对象
        printer = QPrinter(QPrinter.HighResolution)

        # 显示打印对话框
        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec() == QPrintDialog.Accepted:  # 修改了这里
            # 创建一个 QPainter 对象
            painter = QPainter(printer)

            # 将屏幕截图绘制到 QPainter 中
            painter.drawImage(printer.pageRect(), screenshot.toImage())

            # 结束绘制
            painter.end()

    def cv_to_qimage(self,cv_image):

        height, width, channel = cv_image.shape
        bytes_per_line = channel * width
        if channel == 3:
            # OpenCV 的 BGR 格式，需要转换为 RGB
            cvt_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
            return QImage(cvt_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        elif channel == 1:
            # 灰度图像
            return QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
        else:
            raise ValueError("不支持的通道数")
    @Slot()
    def load_image1_tiqu(self):
        self.image1,_ = QFileDialog.getOpenFileName(self.ui.pushButton_load_image1_tiqu, "选择影像1", "","图像文件 (*.png *.jpg *.jpeg *.bmp)")
        cv_image = cv2.imread(self.image1 )

        # 检查图像是否有效
        if cv_image is None:
            self.ui.label_tiqu_zhuangtai.setText("无法加载图像：", self.image1)
            return

        # 将 OpenCV 图像转换为 PySide6 QImage
        qimage = self.cv_to_qimage(cv_image)

        # 将 QImage 转换为 QPixmap
        pixmap = QPixmap.fromImage(qimage)

        # 调整图片大小，以适合 label 的大小
        pixmap = pixmap.scaled(self.ui.label_tiqu_left.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 设置图片到 label
        self.ui.label_tiqu_left.setPixmap(pixmap)
        # 图片居中显示
        self.ui.label_tiqu_left.setAlignment(Qt.AlignCenter)
        self.ui.label_tiqu_zhuangtai.setText("成功加载影像一")

    @Slot()
    def load_image2_tiqu(self):
        self.image2,_  =  QFileDialog.getOpenFileName(self.ui.pushButton_load_image2_tiqu, "选择影像2", "",
                                    "图像文件 (*.png *.jpg *.jpeg *.bmp)")
        cv_image = cv2.imread(self.image2)

        # 检查图像是否有效
        if cv_image is None:
            print("无法加载图像：", self.image2)
            self.ui.label_tiqu_zhuangtai.setText("无法加载图像：", self.image2)
            return

        # 将 OpenCV 图像转换为 PySide6 QImage
        qimage = self.cv_to_qimage(cv_image)

        # 将 QImage 转换为 QPixmap
        pixmap = QPixmap.fromImage(qimage)

        # 调整图片大小，以适合 label 的大小
        pixmap = pixmap.scaled(self.ui.label_tiqu_right.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 设置图片到 label
        self.ui.label_tiqu_right.setPixmap(pixmap)
        # 图片居中显示
        self.ui.label_tiqu_right.setAlignment(Qt.AlignCenter)
        self.ui.label_tiqu_zhuangtai.setText("成功加载影像二")

    @Slot()
    def load_image1_pipei(self):
        self.image1,_  = QFileDialog.getOpenFileName(self.ui.pushButton_load_image1_pipei, "选择影像1", "",
                                    "图像文件 (*.png *.jpg *.jpeg *.bmp)")
        cv_image = cv2.imread(self.image1)

        # 检查图像是否有效
        if cv_image is None:
            print("无法加载图像：", self.image1)
            self.ui.label_pipei_zhuangtai.setText("无法加载图像：", self.image1)
            return

        # 将 OpenCV 图像转换为 PySide6 QImage
        qimage = self.cv_to_qimage(cv_image)

        # 将 QImage 转换为 QPixmap
        pixmap = QPixmap.fromImage(qimage)

        # 调整图片大小，以适合 label 的大小
        pixmap = pixmap.scaled(self.ui.label_pipei_left.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 设置图片到 label
        self.ui.label_pipei_left.setPixmap(pixmap)
        self.ui.label_pipei_left.setAlignment(Qt.AlignCenter)
        self.ui.label_pipei_zhuangtai.setText("成功加载影像一")

    @Slot()
    def load_image2_pipei(self):
        self.image2,_  = QFileDialog.getOpenFileName(self.ui.pushButton_load_image2_pipei, "选择影像2", "",
                                    "图像文件 (*.png *.jpg *.jpeg *.bmp)")
        cv_image = cv2.imread(self.image2)

        # 检查图像是否有效
        if cv_image is None:
            print("无法加载图像：", self.image2)
            self.ui.label_pipei_zhuangtai.setText("无法加载图像：", self.image2)
            return

        # 将 OpenCV 图像转换为 PySide6 QImage
        qimage = self.cv_to_qimage(cv_image)

        # 将 QImage 转换为 QPixmap
        pixmap = QPixmap.fromImage(qimage)

        # 调整图片大小，以适合 label 的大小
        pixmap = pixmap.scaled(self.ui.label_pipei_right.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 设置图片到 label
        self.ui.label_pipei_right.setPixmap(pixmap)
        self.ui.label_pipei_right.setAlignment(Qt.AlignCenter)
        self.ui.label_pipei_zhuangtai.setText("成功加载影像二")

    def load_image1_jiaozheng(self):
        self.image1,_  = QFileDialog.getOpenFileName(self.ui.pushButton_load_image1_pipei_2, "选择影像1", "",
                                    "图像文件 (*.png *.jpg *.jpeg *.bmp)")
        cv_image = cv2.imread(self.image1)

        # 检查图像是否有效
        if cv_image is None:
            print("无法加载图像：", self.image1)
            self.ui.label_pipei_zhuangtai_2.setText("无法加载图像：", self.image1)
            return

        # 将 OpenCV 图像转换为 PySide6 QImage
        qimage = self.cv_to_qimage(cv_image)

        # 将 QImage 转换为 QPixmap
        pixmap = QPixmap.fromImage(qimage)

        # 调整图片大小，以适合 label 的大小
        pixmap = pixmap.scaled(self.ui.label_pipei_left_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 设置图片到 label
        self.ui.label_pipei_left_2.setPixmap(pixmap)
        self.ui.label_pipei_left_2.setAlignment(Qt.AlignCenter)
        self.ui.label_pipei_zhuangtai_2.setText("成功加载影像一")

    @Slot()
    def load_image2_jiaozheng(self):
        self.image2,_  = QFileDialog.getOpenFileName(self.ui.pushButton_load_image2_pipei_2, "选择影像2", "",
                                    "图像文件 (*.png *.jpg *.jpeg *.bmp)")
        cv_image = cv2.imread(self.image2)

        # 检查图像是否有效
        if cv_image is None:
            print("无法加载图像：", self.image2)
            self.ui.label_pipei_zhuangtai_2.setText("无法加载图像：", self.image2)
            return

        # 将 OpenCV 图像转换为 PySide6 QImage
        qimage = self.cv_to_qimage(cv_image)

        # 将 QImage 转换为 QPixmap
        pixmap = QPixmap.fromImage(qimage)

        # 调整图片大小，以适合 label 的大小
        pixmap = pixmap.scaled(self.ui.label_pipei_right_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 设置图片到 label
        self.ui.label_pipei_right_2.setPixmap(pixmap)
        self.ui.label_pipei_right_2.setAlignment(Qt.AlignCenter)
        self.ui.label_pipei_zhuangtai_2.setText("成功加载影像二")


    @Slot()
    def on_feature_type_changed_pipei(self):
        self.feature_type_fun = self.ui.comboBox_feature_type_pipei.currentText()
        self.ui.label_pipei_zhuangtai.setText("成功选择特征提取算法：" + self.feature_type_fun)

    def on_feature_type_changed_tiqu(self):
        self.feature_type_fun = self.ui.comboBox_feature_type_tiqu.currentText()
        self.ui.label_tiqu_zhuangtai.setText("成功选择特征提取算法：" + self.feature_type_fun)

    def on_feature_type_changed_jiaozheng(self):
        self.feature_type_fun = self.ui.comboBox_feature_type_pipei_2.currentText()
        self.ui.label_pipei_zhuangtai_2.setText("成功选择特征提取算法：" + self.feature_type_fun)

    @Slot(QtGui.QPixmap)
    def set_pipei(self, image):
        # 检查图像是否有效
        if not image.isNull():
            # 调整图片大小，以适合 label 的大小
            pixmap = image.scaled(self.ui.label_pipei_result.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # 设置图片到 label
            self.ui.label_pipei_result.setPixmap(pixmap)
            self.ui.label_pipei_result.setAlignment(Qt.AlignCenter)
        else:
            # 如果图像无效，显示错误提示
            QtWidgets.QMessageBox.warning(self, "错误", "图像无效！")

    @Slot(QtGui.QPixmap)
    def set_jiaozheng(self, image):
        # 检查图像是否有效
        if not image.isNull():
            # 调整图片大小，以适合 label 的大小
            pixmap = image.scaled(self.ui.label_pipei_result_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # 设置图片到 label
            self.ui.label_pipei_result_2.setPixmap(pixmap)
            self.ui.label_pipei_result_2.setAlignment(Qt.AlignCenter)
        else:
            # 如果图像无效，显示错误提示
            QtWidgets.QMessageBox.warning(self, "错误", "图像无效！")

    def set_jiaozheng_right(self, image):
        # 检查图像是否有效
        if not image.isNull():
            # 调整图片大小，以适合 label 的大小
            pixmap = image.scaled(self.ui.label_pipei_right_2.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # 设置图片到 label
            self.ui.label_pipei_right_2.setPixmap(pixmap)
            self.ui.label_pipei_right_2.setAlignment(Qt.AlignCenter)
        else:
            # 如果图像无效，显示错误提示
            QtWidgets.QMessageBox.warning(self, "错误", "图像无效！")



    @Slot(QtGui.QPixmap)
    def set_tiqu(self, image):
        # 检查图像是否有效
        if not image.isNull():
            # 调整图片大小，以适合 label 的大小
            pixmap = image.scaled(self.ui.label_tiqu_result.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # 设置图片到 label
            self.ui.label_tiqu_result.setPixmap(pixmap)
            self.ui.label_tiqu_result.setAlignment(Qt.AlignCenter)
        else:
            # 如果图像无效，显示错误提示
            QtWidgets.QMessageBox.warning(self, "错误", "图像无效！")

    @Slot(QtGui.QPixmap)
    def set_video(self,image):
        # 检查图像是否有效
        if not image.isNull():
            # 调整图片大小，以适合 label 的大小
            pixmap = image.scaled(self.ui.label_video.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # 设置图片到 label
            self.ui.label_video.setPixmap(pixmap)
            self.ui.label_video.setAlignment(Qt.AlignCenter)
        else:
            # 如果图像无效，显示错误提示
            QtWidgets.QMessageBox.warning(self, "错误", "图像无效！")


    def task_finished_fun1(self):
        """任务完成后的操作"""
        self.ui.label_3.setText("完成:无人机定位")
        self.fun1.quit()
        print("结束线程")

    # 停止线程
    def stop_thread(self):
        print("停止子线程")
        if self.worker:
            self.worker.stop_1()

    # 开始进行无人机定位
    def run_main(self):

        self.worker.message.emit("开始进行无人机定位")
        #发射无人机匹配的相关信号
        self.worker.task_main_signal.emit(self.show_keypoints, self.display, self.map_path, self.query_path,self.output_dir, self.WRITE_RESULT, self.feature_type)

    @Slot(str)
    def on_text_changed_pipei(self, text):
        try:
            # 尝试将文本转换为整数
            self.max_keypoint = int(text)
            self.ui.label_pipei_zhuangtai.setText("选择最大特征点数为：" + str(self.max_keypoint))
            #self.label.setText(f"输入的整数：{self.integer_value}")
        except ValueError:
            # 如果转换失败，则提示用户
            #self.label.setText("请输入有效的整数")
            print("请输入有效的整数")
            self.ui.label_pipei_zhuangtai.setText("请输入有效的整数")

    def on_text_changed_jiaozheng(self, text):
        try:
            # 尝试将文本转换为整数
            self.max_keypoint = int(text)
            self.ui.label_pipei_zhuangtai_2.setText("选择最大特征点数为：" + str(self.max_keypoint))
            #self.label.setText(f"输入的整数：{self.integer_value}")
        except ValueError:
            # 如果转换失败，则提示用户
            #self.label.setText("请输入有效的整数")
            print("请输入有效的整数")
            self.ui.label_pipei_zhuangtai_2.setText("请输入有效的整数")
    def on_text_changed_tiqu(self, text):
        try:
            # 尝试将文本转换为整数
            self.max_keypoint = int(text)
            self.ui.label_tiqu_zhuangtai.setText("选择最大特征点数为：" + str(self.max_keypoint))
            #self.label.setText(f"输入的整数：{self.integer_value}")
        except ValueError:
            # 如果转换失败，则提示用户
            #self.label.setText("请输入有效的整数")
            print("请输入有效的整数")
            self.ui.label_tiqu_zhuangtai.setText("请输入有效的整数")
    @Slot()
    def task_finished(self):
        """任务完成后的操作"""
        #self.ui.label_3.setText("完成:无人机定位")
        self.worker.message.emit("完成:无人机定位")
        self.worker.quit()
        self.worker.message.emit("结束线程")
        print("结束线程")
            # self.worker = None
            # 在这里执行其他线程的创建或其他操作

    def close_application(self):
        """关闭应用程序"""
        QApplication.quit()

    @Slot()
    def on_show_keypoints_changed(self):
        self.show_keypoints =  self.ui.checkBox_show_keypoints.isChecked()
        self.worker.message.emit("是否显示关键点"+str(self.show_keypoints))

    @Slot()
    def on_write_result_changed(self):
        self.WRITE_RESULT =  self.ui.checkBox_WRITE_RESULT.isChecked()
        self.worker.message.emit("是否保存结果" + str(self.WRITE_RESULT))


    @Slot()
    def on_display_changed(self):
        self.display = self.ui.checkBox_display.isChecked()
        self.worker.message.emit("是否显示匹配过程" + str(self.display))

    @Slot()
    def select_map_path(self):
        self.map_path = QFileDialog.getExistingDirectory(self.ui.pushButton_map_path)
        self.worker.message.emit("成功选择卫星影像库路径：" + self.map_path)

    @Slot()
    def select_query_path(self):
        self.query_path = QFileDialog.getExistingDirectory(self.ui.pushButton_query_path)
        self.worker.message.emit("成功选择无人机影像库路径：" + self.query_path)

    @Slot()
    def select_output_path(self):
        self.output_dir = QFileDialog.getExistingDirectory(self.ui.pushButton_output_dir)
        self.worker.message.emit("成功选择匹配结果路径：" +self.output_dir)

    @Slot()
    def on_feature_type_changed(self):
        self.feature_type = self.ui.comboBox_feature_type.currentText()
        self.worker.message.emit("选择的特征提取算法：" +  self.feature_type)

    @Slot(QtGui.QPixmap)
    def set_image(self, image):
        # 检查图像是否有效
        if not image.isNull():
            # 调整图片大小，以适合 label 的大小
            pixmap = image.scaled(self.ui.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # 设置图片到 label
            self.ui.label.setPixmap(pixmap)
            self.ui.label.setAlignment(Qt.AlignCenter)
        else:
            # 如果图像无效，显示错误提示
            QtWidgets.QMessageBox.warning(self, "错误", "图像无效！")
    @Slot(str)
    def set_message(self, message):

        row1 = self.ui.tableWidget_view.rowCount()#当前存在的表格
        #判断有多少行被填满
        filled_row_count = 0
        for row in range(self.ui.tableWidget_view.rowCount()):
            row_filled = True
            for column in range(self.ui.tableWidget_view.columnCount()):
                item = self.ui.tableWidget_view.item(row, column)
                if item is None or item.text() == "":
                    row_filled = False
                    break
            if row_filled:
                filled_row_count += 1

        # 先加一行
        if filled_row_count>=7:
            self.ui.tableWidget_view.setRowCount(row1 + 1)

        row2=filled_row_count

        # 设置message的值
        message_item = QTableWidgetItem(str(message))  # 将数据转换为QTableWidgetItem
        self.ui.tableWidget_view.setItem(row2, 0, message_item)  # 使用1作为列索引

        if row1>7:
            self.ui.tableWidget_view.scrollToBottom()

    def hf_set_message(self, data):

        ####初始设置19行
        row0 = 19
        row = self.ui.tableWidget_.rowCount()
        row1 = row - row0 + 1
        # 先加一行
        self.ui.tableWidget_.setRowCount(row + 1)

        # 2. 更新该行数据
        for i, item in enumerate(data):
            item = QTableWidgetItem(str(item))  # 将数据转换为字符串
            self.ui.tableWidget_.setItem(row1, i, item)  # 使用 i 作为列索引

    @Slot(list)
    def update_table(self, data):
        ####初始设置27行
        #row0=27
        row0=27
        row = self.ui.tableWidget_result.rowCount()
        row1=row-row0+1
        # 先加一行
        self.ui.tableWidget_result.setRowCount(row + 1)

        # 2. 更新该行数据
        for i, item in enumerate(data):
            item = QTableWidgetItem(str(item))  # 将数据转换为字符串
            self.ui.tableWidget_result.setItem(row1, i, item)  # 使用 i 作为列索引
    #导出结果
    def save_result(self):
        # 弹出选择保存文件路径的对话框
        file_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "CSV 文件 (*.csv);;所有文件 (*)")

        if file_path:
            # 保存表格数据到指定路径
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                # 写入表头
                headers = [self.ui.tableWidget_result.horizontalHeaderItem(i).text() for i in range(self.ui.tableWidget_result.columnCount())]
                writer.writerow(headers)
                # 写入数据行
                for row in range(self.ui.tableWidget_result.rowCount()):
                    row_data = [self.ui.tableWidget_result.item(row, column).text() if self.ui.tableWidget_result.item(row, column) else "" for column in range(self.ui.tableWidget_result.columnCount())]
                    writer.writerow(row_data)

    @Slot(list)
    def updata_map(self,data):
        data1=data[0]#经度
        data2=data[1]#纬度
        image_height=self.map_image.shape[0]#高
        image_width=self.map_image.shape[1]#宽
        #大map对应的经纬度范围
        map_fangwei = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '_internal', 'map_patch.txt')
        with open(map_fangwei,"r",encoding="utf-8")as f:
            datas = f.readlines()
        dic = {}
        for data in datas:
            part = data.split(",")
            dic[part[0]] = part[1]
        top_left_lon = float(dic["top_left_lon"])
        top_left_lat = float(dic["top_left_lat"])
        bottom_right_lon = float(dic["bottom_right_lon"])
        bottom_right_lat = float(dic["bottom_right_lat"])
        #转化成像点坐标
        a=to_xy(image_width, image_height, top_left_lon, top_left_lat, bottom_right_lon, bottom_right_lat, data1,data2)
        self.points.append(a)
        #定义一个渐变的效果，颜色列表，根据points的大小/数量

        #在img上绘制点以及连线,实现渐变效果

        # 定义颜色的开始和结束值
        start_color = np.array([255, 0, 0])
        end_color = np.array([0, 255, 255])

        num_points = len(self.points)

        # 计算每个点的颜色
        colors = []
        for i in range(num_points):
            ratio = i / (num_points - 1) if num_points > 1 else 0
            color = (1 - ratio) * start_color + ratio * end_color
            colors.append(tuple(map(int, color)))

        # 在地图图像上绘制点和连线，实现渐变效果
        img = self.map_image.copy()
        for i in range(1, num_points):
            previous_point = tuple(map(int, self.points[i - 1]))
            current_point = tuple(map(int, self.points[i]))
            current_color = (0, 0, 255)
            cv2.line(img, previous_point, current_point, current_color, 10)

        # 再绘制点
        for i in range(num_points):
            current_point = tuple(map(int, self.points[i]))
            current_color = colors[i]
            # 绘制黑色边框的圆
            cv2.circle(img, current_point, 15, (0, 0, 0), 5)
            # 绘制实心圆
            cv2.circle(img, current_point, 13, current_color, -1)

        image=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        qimage = QPixmap.fromImage(QImage(image, image_width,  image_height, 3 * image_width, QImage.Format_RGB888))
        pixmap = qimage.scaled(self.ui.label_map.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 设置图片到 label
        self.ui.label_map.setPixmap(pixmap)
        self.ui.label_map.setAlignment(Qt.AlignCenter)


    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(self.ui.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(self.ui.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            UIFunctions.toggleLeftBox(self, True)
            widgets.stackedWidget.setCurrentWidget(self.ui.new_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))


            # SHOW HOME PAGE
        if btnName == "btn_fun1":
            widgets.stackedWidget.setCurrentWidget(self.ui.page_fun1)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_jingdu":
            widgets.stackedWidget.setCurrentWidget(self.ui.page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_help":
            pdf_path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '_internal', 'help.pdf')
            QDesktopServices.openUrl(QUrl.fromLocalFile(pdf_path))
            # UIFunctions.resetStyle(self, btnName)
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "pushButton_tiqu":
            widgets.stackedWidget.setCurrentWidget(self.ui.page_tiqu)

        if btnName == "pushButton_pipei":
            widgets.stackedWidget.setCurrentWidget(self.ui.page_pipei)

        if btnName == "pushButton_video":
            widgets.stackedWidget.setCurrentWidget(self.ui.page_video)

        if btnName == "pushButton_fanhui_pipei":
            widgets.stackedWidget.setCurrentWidget(self.ui.page_fun1)

        if btnName == "pushButton_fanhui_tiqu":
            widgets.stackedWidget.setCurrentWidget(self.ui.page_fun1)


        if btnName == "pushButton_fanhui_video":
            widgets.stackedWidget.setCurrentWidget(self.ui.page_fun1)

        if btnName == "pushButton_fanhui_pipei_2":
            widgets.stackedWidget.setCurrentWidget(self.ui.page_fun1)

        if btnName == "pushButton":
            widgets.stackedWidget.setCurrentWidget(self.ui.page_2)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')
    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    #鼠标活动
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')



    def save_image_tiqu(self):
        if self.fun1.image1 is not None:
            file_dialog = QFileDialog(self)
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_dialog.setNameFilter("JPEG Files (*.jpg);;PNG Files (*.png)")
            if file_dialog.exec_():
                filename = file_dialog.selectedFiles()[0]
                # 使用UTF-8编码将路径转换为字节字符串
                filename_encoded = filename.encode('utf-8')
                # 使用imdecode来写入文件
                is_success, buffer = cv2.imencode('.jpg', self.fun1.image1)
                if is_success:
                    with open(filename_encoded, 'wb') as f:
                        f.write(buffer)
    def save_image_pipei(self):
        if self.fun1.image2 is not None:
            file_dialog = QFileDialog(self)
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_dialog.setNameFilter("JPEG Files (*.jpg);;PNG Files (*.png)")
            if file_dialog.exec_():
                filename = file_dialog.selectedFiles()[0]
                # 使用UTF-8编码将路径转换为字节字符串
                filename_encoded = filename.encode('utf-8')
                # 使用imdecode来写入文件
                is_success, buffer = cv2.imencode('.jpg', self.fun1.image2)
                if is_success:
                    with open(filename_encoded, 'wb') as f:
                        f.write(buffer)

    def save_image_jiaozheng(self):
        if self.fun1.image3 is not None:
            file_dialog = QFileDialog(self)
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_dialog.setNameFilter("JPEG Files (*.jpg);;PNG Files (*.png)")
            if file_dialog.exec_():
                filename = file_dialog.selectedFiles()[0]
                # 使用UTF-8编码将路径转换为字节字符串
                filename_encoded = filename.encode('utf-8')
                # 使用imdecode来写入文件
                is_success, buffer = cv2.imencode('.jpg', self.fun1.image3)
                if is_success:
                    with open(filename_encoded, 'wb') as f:
                        f.write(buffer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
