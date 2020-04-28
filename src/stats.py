from videoprops import get_video_properties, get_audio_properties
from moviepy.editor import AudioFileClip
import os, datetime, cv2


major_ver = cv2.__version__.split(".")[0]
if int(major_ver) < 3:
    CAP_PROP_FPS = cv2.cv.CV_CAP_PROP_FPS
    CAP_PROP_FRAME_HEIGHT = cv2.cv.CV_CAP_PROP_FRAME_HEIGHT
    CAP_PROP_FRAME_WIDTH = cv2.cv.CV_CAP_PROP_FRAME_WIDTH
else:
    CAP_PROP_FPS = cv2.CAP_PROP_FPS
    CAP_PROP_FRAME_HEIGHT = cv2.CAP_PROP_FRAME_HEIGHT
    CAP_PROP_FRAME_WIDTH = cv2.CAP_PROP_FRAME_WIDTH


def get_stats(path: str):
    video = cv2.VideoCapture(path)

    container = path.split(".")[-1]
    name = ".".join(path.split(".")[:-1])

    fps = round(video.get(CAP_PROP_FPS), 2)
    h, w = (
        video.get(CAP_PROP_FRAME_HEIGHT),
        video.get(CAP_PROP_FRAME_WIDTH),
    )

    print("calculating frames")
    count = 0
    # while video.isOpened():
    #     ret, frame = video.read()
    #     if ret is False:
    #         break
    #     count += 1

    time = count / fps

    # props = get_video_properties(path)
    videocodec = ""  # props["codec_name"]

    audio = AudioFileClip(path)
    channels = audio.nchannels
    rate = ""

    # ~/Videos/теш/Надводная и подводная робототехника
    # audiocodec, channels, rate = (
    #     props["codec_name"],
    #     props["channels"],
    #     props["sample_rate"],
    # )
    audiocodec = ""
    created = datetime.datetime.fromtimestamp(os.path.getctime(path))
    size = os.path.getsize(path)

    return {
        "name": name,
        "height": h,
        "width": w,
        "duration": time,
        "fps": fps,
        "container": container,
        "videocodec": videocodec,
        "audiocodec": audiocodec,
        "channels": channels,
        "rate": rate,
        "created": created,
        "size": size,
    }
