import matplotlib.pyplot as plt
import numpy as np
import cv2


# * Accepts colored frame (not gray)
def get_rotation(frame: np.array) -> float:
    dft = cv2.dft(frame.astype(np.float32), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft = np.fft.fftshift(dft)

    spectrum = 20 * np.log(cv2.magnitude(dft[:, :, 0], dft[:, :, 1]))
    plt.imshow(spectrum, cmap="gray")
    plt.show()
    spectrum = spectrum / np.max(spectrum) * 255
    spectrum = spectrum.astype(np.uint8)

    lines = cv2.HoughLinesP(spectrum, 5, np.pi / 180, 250, minLineLength=100)

    for line in lines[:5]:
        x1, y1, x2, y2 = line[0]
        cv2.line(spectrum, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("s", spectrum)
    cv2.waitKey(3000) & ord("q") == 0xFF
    # plt.imshow(spectrum, cmap="gray")
    # plt.show()


def is_horizon_rotated(frame: np.array) -> bool:
    return get_rotation(frame) or 0 > 40


import os.path as p

good = cv2.imread(p.abspath(__file__ + "/../../../good.jpg"), 0)
bad = cv2.imread(p.abspath(__file__ + "/../../../bad.jpg"), 0)

print(is_horizon_rotated(good))
# print(is_horizon_rotated(bad))
