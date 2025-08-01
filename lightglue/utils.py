import collections.abc as collections
from pathlib import Path
from types import SimpleNamespace
from typing import Callable, List, Optional, Tuple, Union
import cv2
import kornia
import numpy as np
import torch

class ImagePreprocessor:
    default_conf = {
        "resize": None,  # target edge length, None for no resizing
        "side": "long",
        "interpolation": "bilinear",
        "align_corners": None,
        "antialias": True,
    }

    def __init__(self, **conf) -> None:
        super().__init__()
        self.conf = {**self.default_conf, **conf}
        self.conf = SimpleNamespace(**self.conf)

    def __call__(self, img: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """Resize and preprocess an image, return image and resize scale"""
        h, w = img.shape[-2:]
        if self.conf.resize is not None:
            img = kornia.geometry.transform.resize(
                img,
                self.conf.resize,
                side=self.conf.side,
                antialias=self.conf.antialias,
                align_corners=self.conf.align_corners,
            )
        scale = torch.Tensor([img.shape[-1] / w, img.shape[-2] / h]).to(img)
        return img, scale
def map_tensor(input_, func: Callable):
    string_classes = (str, bytes)
    if isinstance(input_, string_classes):
        return input_
    elif isinstance(input_, collections.Mapping):
        return {k: map_tensor(sample, func) for k, sample in input_.items()}
    elif isinstance(input_, collections.Sequence):
        return [map_tensor(sample, func) for sample in input_]
    elif isinstance(input_, torch.Tensor):
        return func(input_)
    else:
        return input_
def batch_to_device(batch: dict, device: str = "cpu", non_blocking: bool = True):
    """Move batch (dict) to device"""

    def _func(tensor):
        return tensor.to(device=device, non_blocking=non_blocking).detach()

    return map_tensor(batch, _func)
def rbd(data: dict) -> dict:
    """Remove batch dimension from elements in data"""
    return {
        k: v[0] if isinstance(v, (torch.Tensor, np.ndarray, list)) else v
        for k, v in data.items()
    }
def read_image(path: Path, grayscale: bool = False) -> np.ndarray:
    """Read an image from path as RGB or grayscale"""
    if not Path(path).exists():
        raise FileNotFoundError(f"No image at path {path}.")
    mode = cv2.IMREAD_GRAYSCALE if grayscale else cv2.IMREAD_COLOR
    image = cv2.imread(str(path), mode)
    if image is None:
        raise IOError(f"Could not read image at {path}.")
    if not grayscale:
        image = image[..., ::-1]#如果按照彩色模式读取图像，将图像的颜色空间从 BGR 转换为 RGB
    return image
def numpy_image_to_torch(image: np.ndarray) -> torch.Tensor:
    """Normalize the image tensor and reorder the dimensions."""
    if image.ndim == 3:
        image = image.transpose((2, 0, 1))  # HxWxC to CxHxW
    elif image.ndim == 2:
        image = image[None]  # add channel axis
    else:
        raise ValueError(f"Not an image: {image.shape}")
    return torch.tensor(image / 255.0, dtype=torch.float)
def resize_image( image: np.ndarray, size: Union[List[int], int], fn: str = "max", interp: Optional[str] = "area",) -> np.ndarray:
    """Resize an image to a fixed size, or according to max or min edge."""
    h, w = image.shape[:2]

    fn = {"max": max, "min": min}[fn]
    if isinstance(size, int):
        scale = size / fn(h, w)
        h_new, w_new = int(round(h * scale)), int(round(w * scale))
        scale = (w_new / w, h_new / h)
    elif isinstance(size, (tuple, list)):
        h_new, w_new = size
        scale = (w_new / w, h_new / h)
    else:
        raise ValueError(f"Incorrect new size: {size}")
    mode = {
        "linear": cv2.INTER_LINEAR,
        "cubic": cv2.INTER_CUBIC,
        "nearest": cv2.INTER_NEAREST,
        "area": cv2.INTER_AREA,
    }[interp]
    return cv2.resize(image, (w_new, h_new), interpolation=mode), scale

#返回torch
def load_image(path: Path, resize: int = None, **kwargs) -> torch.Tensor:
    image = read_image(path)
    if resize is not None:
        image, _ = resize_image(image, resize, **kwargs)
    return numpy_image_to_torch(image)

#返回 opencv图像数组
def load_image1(path: Path, resize: int = 800, **kwargs) -> torch.Tensor:
    image = read_image(path)
    if resize is not None:
        image, _ = resize_image(image, resize, **kwargs)
    return  image
class Extractor(torch.nn.Module):
    def __init__(self, **conf):
        super().__init__()
        self.conf = SimpleNamespace(**{**self.default_conf, **conf})

    @torch.no_grad()
    def extract(self, img: torch.Tensor, **conf) -> dict:
        """Perform extraction with online resizing"""
        if img.dim() == 3:
            img = img[None]  # add batch dim
        assert img.dim() == 4 and img.shape[0] == 1
        shape = img.shape[-2:][::-1]
        img, scales = ImagePreprocessor(**{**self.preprocess_conf, **conf})(img)
        feats = self.forward({"image": img})
        feats["image_size"] = torch.tensor(shape)[None].to(img).float()
        feats["keypoints"] = (feats["keypoints"] + 0.5) / scales[None] - 0.5
        return feats

#快速匹配的简单用法
def match_pair(extractor,matcher,image0: torch.Tensor,image1: torch.Tensor, device: str = "cpu",**preprocess,):
    """Match a pair of images (image0, image1) with an extractor and matcher"""
    feats0 = extractor.extract(image0, **preprocess)
    feats1 = extractor.extract(image1, **preprocess)
    matches01 = matcher({"image0": feats0, "image1": feats1})
    data = [feats0, feats1, matches01]
    # remove batch dim and move to target device
    feats0, feats1, matches01 = [batch_to_device(rbd(x), device) for x in data]
    return feats0, feats1, matches01



#使用opencv处理图像
def load_image_new(image, resize: int = None, **kwargs) -> torch.Tensor:       # 用于仿生眼
    return numpy_image_to_torch(image)
def load_image_fun1(image_path1, image_path2):
    """
        读取两张影像并将它们的高度统一为400像素。

        Args:
        image_path1 (str): 第一张影像的路径。
        image_path2 (str): 第二张影像的路径。

        Returns:
        tuple: 高度为400像素的两张影像。
        """
    # 读取影像
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # 定义统一的高度
    unified_height = 400

    # 获取影像的高度和宽度
    height1, width1 = image1.shape[:2]
    height2, width2 = image2.shape[:2]

    # 计算缩放比例
    scale1 = unified_height / height1
    scale2 = unified_height / height2

    # 缩放影像
    new_width1 = int(width1 * scale1)
    new_width2 = int(width2 * scale2)

    resized_image1 = cv2.resize(image1, (new_width1, unified_height))
    resized_image2 = cv2.resize(image2, (new_width2, unified_height))

    return resized_image1, resized_image2
def torch_to_numpy(image):
    """
    将图像的灰度值乘以255。

    Args:
    image (numpy.ndarray): OpenCV 图像数据。

    Returns:
    numpy.ndarray: 处理后的图像数据。
    """
    scaled_image = image * 255
    scaled_image = scaled_image.astype('uint8')  # 转换为 uint8 类型

    return scaled_image

def load_image_fun2(image_path1, image_path2):
    """
        读取两张影像并将它们的高度统一为400像素。

        Args:
        image_path1 (str): 第一张影像的路径。
        image_path2 (str): 第二张影像的路径。

        Returns:
        tuple: 高度为400像素的两张影像。
        """
    # 读取影像
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # 定义统一的高度
    unified_height = image1.shape[0]

    # 获取影像的高度和宽度
    height1, width1 = image1.shape[:2]
    height2, width2 = image2.shape[:2]

    # 计算缩放比例
    scale1 = unified_height / height1
    scale2 = unified_height / height2

    # 缩放影像
    new_width1 = int(width1 * scale1)
    new_width2 = int(width2 * scale2)

    resized_image1 = cv2.resize(image1, (new_width1, unified_height))
    resized_image2 = cv2.resize(image2, (new_width2, unified_height))

    return resized_image1, resized_image2

