from datetime import datetime
import tempfile
import subprocess
import json
import os

FFPROBE_PATH = os.path.join(os.path.dirname(__file__), "lib\\ffprobe.exe")


def run_ffprobe(args):
    return subprocess.getoutput(f"{FFPROBE_PATH} {args}")


def get_stats(path):
    output = run_ffprobe(
        f" -v quiet -print_format json -show_streams -show_format {path}"
    )
    data = json.loads(output)

    audio, video = None, None
    for stream in data["streams"]:
        if stream["codec_type"] == "video":
            video = stream
        elif stream["codec_type"] == "audio":
            audio = stream

    result = {
        "fps": None,
        "width": None,
        "height": None,
        "duration": None,
        "channels": None,
        "frequency": None,
        "container": path.split(".")[-1].lower(),
        "duration": float(data["format"]["duration"]),
        "created": datetime.fromtimestamp(os.path.getctime(path)),
        "bitrate": int(data["format"]["bit_rate"]),
        "size": int(data["format"]["size"]),
        "name": os.path.basename(path),
    }
    if video is not None:
        framerate = video["r_frame_rate"].split("/")
        result["width"] = int(video["width"])
        result["height"] = int(video["height"])
        result["fps"] = int(framerate[0]) / int(framerate[1])
    if audio is not None:
        result["channels"] = int(audio["channels"])
        result["frequency"] = int(audio["sample_rate"])

    return result
