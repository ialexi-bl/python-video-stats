import numpy as np
import cv2


def check_slideshow(path):
    video = cv2.VideoCapture(path)
    frames = 0
    cnt = 1

    fps = video.get(cv2.CAP_PROP_FPS)
    ret, initial_frame = video.read()

    if not ret or initial_frame is None:
        return "нет", 0, 0

    width, height = (
        video.get(cv2.CAP_PROP_FRAME_WIDTH),
        video.get(cv2.CAP_PROP_FRAME_HEIGHT),
    )
    prev = initial_frame

    while video.isOpened():
        if frames > 60:
            return "нет", width, height
        frames += 1

        ret, frame = video.read()
        if not ret:
            break
        if np.equal(frame, prev).all():
            cnt += 1
        else:
            prev = frame
            cnt = 1
        if fps / cnt < 25:
            return "да", width, height
    return "нет", width, height
