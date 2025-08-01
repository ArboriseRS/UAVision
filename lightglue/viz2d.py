"""
2D visualization primitives based on Matplotlib.
1) Plot images with `plot_images`.
2) Call `plot_keypoints` or `plot_matches` any number of times.
3) Optionally: save a .png or .pdf plot (nice in papers!) with `save_plot`.
"""
import cv2
import numpy as np
import torch


# 颜色映射函数，用于将数值映射到红-黄-绿色的颜色空间
def cm_RdGn(x):
    """Custom colormap: red (0) -> yellow (0.5) -> green (1)."""
    x = np.clip(x, 0, 1)[..., None] * 2
    c = x * np.array([[0, 1.0, 0]]) + (2 - x) * np.array([[1.0, 0, 0]])
    return np.clip(c, 0, 1)


# 自定义颜色映射函数，与之前的 cm_RdGn 函数类似，但是在该函数中增加了蓝色到红色的映射
def cm_BlRdGn(x_):
    """Custom colormap: blue (-1) -> red (0.0) -> green (1)."""
    x = np.clip(x_, 0, 1)[..., None] * 2
    c = x * np.array([[0, 1.0, 0, 1.0]]) + (2 - x) * np.array([[1.0, 0, 0, 1.0]])   # 分别表示绿色和红色的 RGBA 值

    xn = -np.clip(x_, -1, 0)[..., None] * 2
    cn = xn * np.array([[0, 0.1, 1, 1.0]]) + (2 - xn) * np.array([[1.0, 0, 0, 1.0]])    # 分别表示蓝色和红色的 RGBA 值
    # 输入值小于 0 的部分使用蓝色映射，大于等于 0 的部分使用红-黄-绿色映射
    # 然后使用 np.clip 将颜色值限制在 0 和 1 之间
    out = np.clip(np.where(x_[..., None] < 0, cn, c), 0, 1) # [..., None] 表示在 x_ 的最后一维上添加一个新的维度
    return out


# 自定义颜色映射函数，用于可视化修剪操作, 将不同的修剪程度表示为颜色的变化
def cm_prune(x_):
    """Custom colormap to visualize pruning"""
    if isinstance(x_, torch.Tensor):            # 检查 x_ 是否为 torch.Tensor 类型，如果是，则变成 numpy 类型
        x_ = x_.cpu().numpy()
    max_i = max(x_)                             # x_ 的最大值保存到 max_i
    # 计算归一化后的 max_i 并保存到 norm_x.
    norm_x = np.where(x_ == max_i, -1, (x_ - 1) / 9)    # 将最大值对应的位置设为 -1，其余值进行线性映射到 (x_ -1, 0) 的范围内
    # 可以保证最大值对应的颜色为蓝色，其他值按照线性比例映射到红色和绿色之间
    return cm_BlRdGn(norm_x)


def plot_images(imgs, cmaps="gray", dpi=100, adaptive=True):
    """Plot a set of images horizontally.
    Args:
        imgs: list of NumPy RGB (H, W, 3) or PyTorch RGB (3, H, W) or mono (H, W).
        titles: a list of strings, as titles for each image.
        cmaps: colormaps for monochrome images.
        adaptive: whether the figure size should fit the image aspect ratios.
    """
    # conversion to (H, W, 3) for torch.Tensor
    imgs = [
        img.permute(1, 2, 0).cpu().numpy()
        if (isinstance(img, torch.Tensor) and img.dim() == 3)
        else img
        for img in imgs
    ]

    n = len(imgs)           # 实时情况下，n = 2。n 为获取图像的数量
    if adaptive:
        ratios = [i.shape[1] / i.shape[0] for i in imgs]  # W / H
    else:
        ratios = [4 / 3] * n
    # 按照 ratios 的比例进行缩放

    plot_img = cv2.hconcat(imgs)        # plot_img 为左右两个图像水平拼接后的图像
    return plot_img



def plot_keypoints(plot_img, kpts, wide1,colors=(0, 255, 0), radius=5, thickness=-1, alpha = 1):
    """Plot keypoints for existing images.
    Args:
        kpts: list of ndarrays of size (N, 2).
        colors: string, or list of tuples (one for each keypoints).
        radius: size of the keypoints.
    """
    # 初始化函数返回的图像
    points_image = plot_img.copy()

    # opencv 没有 matplotlib里面坐标轴的概念，因此对于拼接形成的图像进行画图的时候，坐标需要进行平移
    # 因此需要引入偏移量，这个里面偏移量的大小为拼接图像的宽的一半
    # 点的偏移量
    #offset = int(round(plot_img_w / 2))
    offset = int(round(wide1))
    # 点的偏移量

    if colors is None:
        colors = np.random.uniform(0, 1, (len(kpts[0]), 3)).tolist()
    elif len(colors) > 0 and not isinstance(colors[0], (tuple, list)):
        colors = [colors] * len(kpts[0])
    # print("-------------------------------------------------------------")
    # print(kpts)           # 输出左右匹配的点，确定匹配的结果是否有误
    # print("-------------------------------------------------------------")

    n = 0
    for colours, keypoints in zip(colors, kpts):
        if isinstance(keypoints, torch.Tensor):
            keypoints = keypoints.cpu().numpy()
        print(len(keypoints))
        for i in range(len(keypoints)):
            if n == 0:
                center_0 = (int(round(keypoints[i][0])), int(round(keypoints[i][1])))
            else:
                center_0 = (int(round(keypoints[i][0])) + offset, int(round(keypoints[i][1])))
            radius = radius
            color = colours[0][i]
            thickness = thickness
            alpha = alpha
            # print(center_0, radius, color, thickness)
            points_image = cv2.circle(plot_img, center_0, radius, color, thickness)
        n += 1

    return points_image


def plot_matches(plot_img, kpts0, kpts1, wide1,color=None, lw=2, ps=4, a=1.0, labels=None):
    """Plot matches for a pair of existing images.
    Args:
        kpts0, kpts1: corresponding keypoints of size (N, 2).
        colour: color of each match, string or RGB tuple. Random if not given.
        lw: width of the lines.
        ps: size of the end points (no endpoint if ps=0)
        indices: indices of the images to draw the matches on.
        a: alpha opacity of the match lines.
    """
    # opencv 没有 matplotlib里面坐标轴的概念，因此对于拼接形成的图像进行画图的时候，坐标需要进行平移
    # 因此需要引入偏移量，这个里面偏移量的大小为拼接图像的宽的一半
    #offset = int(round(plot_img_w / 2))
    offset = int(round(wide1))
    if isinstance(kpts0, torch.Tensor):
        kpts0 = kpts0.cpu().numpy()
    if isinstance(kpts1, torch.Tensor):
        kpts1 = kpts1.cpu().numpy()
    assert len(kpts0) == len(kpts1)
    # print("kpts0-----------------------------------------")
    # print(kpts0)
    # print("kpts1-----------------------------------------")
    # print(kpts1)

    if color is None:
        colors = np.random.uniform(0, 1, (len(kpts0), 3)).tolist()
    elif len(color) > 0 and not isinstance(color[0], (tuple, list)):
        colors = [color] * len(kpts0)

    if lw > 0:
        for i in range(len(kpts0)):
            x1, y1 = int(round(kpts0[i, 0])), int(round(kpts0[i, 1]))
            x2, y2 = int(round(kpts1[i, 0])) + offset, int(round(kpts1[i, 1]))
            colour = colors[i]
            cv2.line(plot_img, (x1, y1), (x2, y2), colour, thickness=lw)


def make_matching_plot_fast(image0, image1, kpts0, kpts1, mkpts0,
                            mkpts1, color, text, path=None,
                            show_keypoints=False, margin=10,
                            opencv_display=False, opencv_title='',
                            small_text=[]):
    H0, W0 = image0.shape[:2]  # 获取 image0 的高度和宽度
    H1, W1 = image1.shape[:2]
    #H, W = max(H0, H1), W0 + W1 + margin
    H, W = H0+H1+margin,max(W0,W1)
    # 创建一个三通道白色图像，形状为 (W, H, 3)
    out = np.stack([255 * np.ones((H, W), np.uint8)] * 3, axis=-1)
    image0_rgb = cv2.cvtColor(image0, cv2.COLOR_BGR2RGB)
    image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    out[:H0, :W0] = image0_rgb  # 将 image0 复制到 out 的左上角
    out[H0+margin:H0+margin+H1, :W1] = image1_rgb     #A：  从A开始 #:A  0到A

    # H0, W0 = image0.shape[:2]
    # H1, W1 = image1.shape[:2]
    # H, W = max(H0, H1), W0 + W1 + margin
    #
    # out = np.stack([255 * np.ones((H, W), np.uint8)] * 3, axis=-1)
    # image0_rgb = cv2.cvtColor(image0, cv2.COLOR_BGR2RGB)
    # image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    #
    # out[:H0, :W0] = image0_rgb
    # out[:H1, W0 + margin:] = image1_rgb




    if show_keypoints:
    #     kpts0, kpts1 = np.round(kpts0).astype(int), np.round(kpts1).astype(int)
    #     white = (255, 255, 255)
    #     black = (0, 0, 0)
    #     for x, y in kpts0:
    #         cv2.circle(out, (x, y), 2, black, -1, lineType=cv2.LINE_AA)
    #         cv2.circle(out, (x, y), 1, white, -1, lineType=cv2.LINE_AA)
    #     for x, y in kpts1:
    #         cv2.circle(out, (x + margin + W0, y), 2, black, -1,
    #                    lineType=cv2.LINE_AA)
    #         cv2.circle(out, (x + margin + W0, y), 1, white, -1,
    #                    lineType=cv2.LINE_AA)
    #
    # mkpts0, mkpts1 = np.round(mkpts0).astype(int), np.round(mkpts1).astype(int)
    # for (x0, y0), (x1, y1) in zip(mkpts0, mkpts1):
    #     cv2.line(out, (x0, y0), (x1 + margin + W0, y1),
    #              color=color, thickness=1, lineType=cv2.LINE_AA)
    #     # display line end-points as circles
    #     cv2.circle(out, (x0, y0), 2, color, -1, lineType=cv2.LINE_AA)
    #     cv2.circle(out, (x1 + margin + W0, y1), 2,color, -1,
    #                lineType=cv2.LINE_AA)
        kpts0, kpts1 = np.round(kpts0).astype(int), np.round(kpts1).astype(int)
        white = (255, 255, 255)
        black = (0, 0, 0)
        for x, y in kpts0:
            cv2.circle(out, (x, y), 2, black, -1, lineType=cv2.LINE_AA)
            cv2.circle(out, (x, y), 1, white, -1, lineType=cv2.LINE_AA)
        for x, y in kpts1:
            cv2.circle(out, (x, y+margin +H0), 2, black, -1,
                       lineType=cv2.LINE_AA)
            cv2.circle(out, (x, y+margin +H0), 1, white, -1,
                       lineType=cv2.LINE_AA)

    mkpts0, mkpts1 = np.round(mkpts0).astype(int), np.round(mkpts1).astype(int)

    for (x0, y0), (x1, y1) in zip(mkpts0, mkpts1):
        #c = c.tolist()
        cv2.line(out, (x0, y0), (x1 , y1+margin +H0),
                 color=color, thickness=1, lineType=cv2.LINE_AA)
        # display line end-points as circles
        cv2.circle(out, (x0, y0), 2, color, -1, lineType=cv2.LINE_AA)
        cv2.circle(out, (x1 , y1+margin +H0), 2, color, -1,
                   lineType=cv2.LINE_AA)


    # Scale factor for consistent visualization across scales.
    sc = min(H / 640., 2.0)

    # Big text.
    Ht = int(30 * sc)  # text height
    txt_color_fg = (255, 255, 255)
    txt_color_bg = (0, 0, 0)
    for i, t in enumerate(text):
        cv2.putText(out, t, (int(8 * sc), Ht * (i + 1)), cv2.FONT_HERSHEY_DUPLEX,
                    1.0 * sc, txt_color_bg, 2, cv2.LINE_AA)
        cv2.putText(out, t, (int(8 * sc), Ht * (i + 1)), cv2.FONT_HERSHEY_DUPLEX,
                    1.0 * sc, txt_color_fg, 1, cv2.LINE_AA)

    # Small text.
    Ht = int(18 * sc)  # text height
    for i, t in enumerate(reversed(small_text)):
        cv2.putText(out, t, (int(8 * sc), int(H - Ht * (i + .6))), cv2.FONT_HERSHEY_DUPLEX,
                    0.5 * sc, txt_color_bg, 2, cv2.LINE_AA)
        cv2.putText(out, t, (int(8 * sc), int(H - Ht * (i + .6))), cv2.FONT_HERSHEY_DUPLEX,
                    0.5 * sc, txt_color_fg, 1, cv2.LINE_AA)

    return out
