from math import floor, ceil
import numpy as np
import cv2


def apply_mask(matrix, mask, fill_value):
    masked = np.ma.array(matrix, mask=mask, fill_value=fill_value)
    return masked.filled()


def apply_threshold(matrix, low_value, high_value):
    low_mask = matrix < low_value
    matrix = apply_mask(matrix, low_mask, low_value)

    high_mask = matrix > high_value
    matrix = apply_mask(matrix, high_mask, high_value)

    return matrix


def get_means(frame):
    half_percent = 1 / 200
    channels = cv2.split(frame)

    out_channels = []
    for channel in channels:
        height, width = channel.shape
        flat = channel.reshape(width * height)
        flat = np.sort(flat)

        n_cols = flat.shape[0]

        low_val = flat[floor(n_cols * half_percent)]
        high_val = flat[ceil(n_cols * (1.0 - half_percent))]

        print("Lowval: ", low_val)
        print("Highval: ", high_val)

        # saturate below the low percentile and above the high percentile
        thresholded = apply_threshold(channel, low_val, high_val)
        # scale the channel
        normalized = cv2.normalize(
            thresholded, thresholded.copy(), 0, 255, cv2.NORM_MINMAX
        )

        low_val = normalized.reshape(n_cols)[floor(n_cols * half_percent)]
        high_val = normalized.reshape(n_cols)[ceil(n_cols * (1.0 - half_percent))]

        print("Lowval: ", low_val)
        print("Highval: ", high_val)
        print("-------")

        out_channels.append(normalized)
    print("-------\n")
    cv2.imshow("after", cv2.merge(out_channels))
    cv2.waitKey(0)
