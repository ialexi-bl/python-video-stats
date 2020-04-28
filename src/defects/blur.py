from ..config import BLUR_THRESHOLD
import numpy as np
import cv2


def get_blur(gray_frame: np.array) -> float:
    size = gray_frame.shape[0] * gray_frame.shape[1]

    # return cv2.Laplacian(gray, cv2.CV_64F).var()
    return np.count_nonzero(cv2.Canny(gray_frame, 225, 175)) * 100 / size
    # return np.count_nonzero(cv2.Laplacian(gray, cv2.CV_64F)) / size


def is_blurred(gray_frame: np.array) -> bool:
    return get_blur(gray_frame) < BLUR_THRESHOLD


def blur_check(path):
    video = cv2.VideoCapture(path)
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        if is_blurred(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)):
            return True
    return False
