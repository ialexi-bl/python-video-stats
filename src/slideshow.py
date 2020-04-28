import cv2


def check_slideshow(path):
    video = cv2.VideoCapture(path)
    prev = [[[]]]
    cnt = 0
    fps = video.get(cv2.CAP_PROP_FPS)
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        if frame == prev:
            cnt += 1
        else:
            prev = frame
            cnt = 0
        if fps / cnt < 25:
            return 'да'
    return 'нет'
