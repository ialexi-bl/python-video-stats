from videoprops import get_video_properties, get_audio_properties
from moviepy.video.io.VideoFileClip import VideoFileClip
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
    time = VideoFileClip(path).duration

    audio = AudioFileClip(path)
    bitdepth = audio.reader.nbytes * 8
    channels = audio.nchannels
    frequency = audio.fps
    # in Kbit
    print(frequency, channels, bitdepth)
    bitrate = frequency * 1000 * channels * bitdepth / 1024

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
        "channels": channels,
        "created": created,
        "size": size,
        "frequency": frequency,
        "bitrate": bitrate,
    }
