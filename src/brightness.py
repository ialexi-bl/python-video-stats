import numpy as np
import cv2


def bad_brightness(path: str) -> str:
    video = cv2.VideoCapture(path)
    mn, mx = 1000000000, 0
    h, w = (
        video.get(cv2.CAP_PROP_FRAME_HEIGHT),
        video.get(cv2.CAP_PROP_FRAME_WIDTH),
    )

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        cur = np.sum(frame) / 3 * h * w
        mx = max(mx, cur)
        mn = min(mn, cur)
        if mx - mn > 50:
            return "да"

    return "нет"
