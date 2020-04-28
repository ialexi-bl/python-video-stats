import cv2


def check_slideshow(path):
    video = cv2.VideoCapture(path)
    prev = [[[]]]
    cnt = 1
    fps = video.get(cv2.CAP_PROP_FPS)
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        if len(frame) == len(prev) and all([all([all([frame[i][j][k] == prev[i][j][k] for k in range(3)])]
                                                for j in range(len(frame[0])))] for i in range(len(frame))):
            cnt += 1
        else:
            prev = frame
            cnt = 1
        if fps / cnt < 25:
            return 'да'
    return 'нет'
