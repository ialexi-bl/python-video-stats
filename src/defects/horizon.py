# from ..config import HORIZON_THRESHOLD
import numpy as np
import cv2

HORIZON_THRESHOLD = 97


def get_rotation(frame: np.array) -> float:
    img = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY).astype(np.float32)
    dft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)
    dft = np.fft.fftshift(dft)
    dft = 20 * np.log(cv2.magnitude(dft[:, :, 0], dft[:, :, 1]))
    dft = dft / np.max(dft) * 255
    gray = 255 - dft.astype(np.uint8)

    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 13, 3
    )
    thresh = 255 - thresh

    kernel = np.ones((3, 3), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    kernel = np.ones((1, 9), np.uint8)
    morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)

    edges = cv2.Canny(morph, 150, 200)
    result = dft.copy()
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)

    thetas = lines[:5, 0, 1] / np.pi * 180
    return thetas


def is_horizon_rotated(frame: np.array) -> bool:
    thetas = get_rotation(frame)

    thetas = thetas[thetas < 170]
    thetas = thetas[thetas > 10]

    if len(thetas) == 0:
        return True

    for theta in thetas:
        if 10 < theta % 90 < 80:
            return True

    return False


def check_rotation_deffects(source):
    video = cv2.VideoCapture(source)
    mn, mx = 1000000000, 0
    prev = get_rotation(video.read()[1])[0]
    rotated = 0
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        cur = get_rotation(frame)[0]
        if is_horizon_rotated(frame):
            rotated = 1
        if abs(prev - cur) < 30:  # if more, it must be some stupid bug
            mn = min(mn, cur)
            mx = max(mx, cur)
        prev = cur
    return (
        mx - mn > 20,
        rotated,
    )  # при тряске будет очень большое значени еиз-за погрешности
