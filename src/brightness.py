import numpy as np
import cv2


def bad_brightness(path: str) -> str:
    video = cv2.VideoCapture(path)
    h, w = (
        video.get(cv2.CAP_PROP_FRAME_HEIGHT),
        video.get(cv2.CAP_PROP_FRAME_WIDTH),
    )
    prev = np.sum(video.read()[1]) / 3 * h * w
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        cur = np.sum(frame) / 3 * h * w
        if abs(cur - prev) > 40:
            return "да"
        prev = cur

    return "нет"
