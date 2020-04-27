from ..blur import get_blur, is_blurred
from os.path import join, dirname
import cv2


images = [
    ["blur-1.png", True],
    ["blur-5.png", True],
    ["blur-6.png", True],
    ["blur-2.png", False],
    ["blur-3.png", False],
    ["blur-4.png", False],
    ["blur-7.png", False],
    ["blur-8.png", False],
    ["blur-9.png", False],
]


print("Blur test results:")
for [filename, expected] in images:
    print
    image = cv2.imread(join(dirname(__file__), "media", filename))
    score = get_blur(image)
    result = is_blurred(image)

    print(
        f"""Image "{filename}" — score: {score:6.3f}% clarity; \
expected: {'True, ' if expected else 'False,'} predicted: {result}"""
    )
