# from ..config import HORIZON_THRESHOLD
import matplotlib.pyplot as plt
import numpy as np
import cv2

HORIZON_THRESHOLD = 97


# * Accepts colored frame (not gray)
def get_rotation(frame: np.array) -> float:
    dft = cv2.dft(frame.astype(np.float32).copy(), flags=cv2.DFT_COMPLEX_OUTPUT)
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

    # for line in lines[:5]:
    #     for rho, theta in line:
    #         a = np.cos(theta)
    #         b = np.sin(theta)
    #         x0 = a * rho
    #         y0 = b * rho
    #         x1 = int(x0 + 1000 * (-b))
    #         y1 = int(y0 + 1000 * (a))
    #         x2 = int(x0 - 1000 * (-b))
    #         y2 = int(y0 - 1000 * (a))
    #         cv2.line(result, (x1, y1), (x2, y2), (0, 0, 255), 4)

    # plt.imshow(result)
    # plt.show()


def is_horizon_rotated(frame: np.array) -> bool:
    thetas = get_rotation(frame)

    # If all lines are vertical (more than 170deg) => rotated
    # If at least one is more than 8deg away from horizontal => rotate
    # (horizontal is 90deg)
    #  Otherwise fine

    thetas = thetas[thetas < 170]
    thetas = thetas[thetas > 10]

    if len(thetas) == 0:
        return True

    for theta in thetas:
        print(theta, theta % 90)
        if 10 < theta % 90 < 80:
            return True

    return False


# import os.path as p

# imgs = {
#     "bad": cv2.imread(p.abspath(__file__ + "/../../../bad.jpg"), 0),
#     "bad2": cv2.imread(p.abspath(__file__ + "/../../../bad2.jpg"), 0),
#     "bad3": cv2.imread(p.abspath(__file__ + "/../../../bad3.jpg"), 0),
#     "bad4": cv2.imread(p.abspath(__file__ + "/../../../bad4.jpg"), 0),
#     "good": cv2.imread(p.abspath(__file__ + "/../../../good.jpg"), 0),
#     "good2": cv2.imread(p.abspath(__file__ + "/../../../good2.jpg"), 0),
# }

# for name, img in imgs.items():
#     print(name, ":", is_horizon_rotated(img))
