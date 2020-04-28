from .config import BLUR_THRESHOLD
import numpy as np
import cv2


def get_blur(gray_frame: np.array) -> float:
    size = gray.shape[0] * gray.shape[1]

    # return cv2.Laplacian(gray, cv2.CV_64F).var()
    return np.count_nonzero(cv2.Canny(image, 225, 175)) * 100 / size
    # return np.count_nonzero(cv2.Laplacian(gray, cv2.CV_64F)) / size


def is_blurred(gray_frame: np.array) -> bool:
    return get_blur(gray_frame) < BLUR_THRESHOLD
