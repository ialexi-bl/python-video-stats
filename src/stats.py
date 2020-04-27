import cv2
from videoprops import get_video_properties, get_audio_properties


def stats(path):
    video = cv2.VideoCapture(path)
    fps, count, container, name = 0, 0, path.split('.')[-1], '.'.join(path.split('.')[:-1])
    major_ver, minor_ver, subminor_ver = cv2.__version__.split('.')
    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        fps = video.get(cv2.CAP_PROP_FPS)
    h, w = video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT), video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    while video.isOpened():
        ret, frame = video.read()
        if ret is False:
            break
        count += 1
    time = count / fps
    props = get_video_properties(path)
    videocodec = props['codec_name']
    props = get_audio_properties(path)
    audiocodec, channels, rate = props["codec_name"], props["channels"], props["sample_rate"]
    return name, h, w, time, fps, container, videocodec, audiocodec, channels, rate
