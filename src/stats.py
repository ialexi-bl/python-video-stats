from datetime import datetime
import os


def get_stats(path, ffmpeg):
    data = ffmpeg.get_data(path)

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
        "channels": None,
        "frequency": None,
        "container": path.split(".")[-1].lower(),
        "duration": float(data["format"]["duration"]),
        "created": datetime.fromtimestamp(os.path.getctime(path)),
        "bitrate": int(data["format"]["bit_rate"]),
        "size": int(data["format"]["size"]) // 1024,
        "name": os.path.basename(path),
    }
    if video is not None:
        result["width"] = int(video["width"])
        result["height"] = int(video["height"])
        if "r_frame_rate" in video:
            framerate = video["r_frame_rate"].split("/")
            if framerate is not None:
                try:
                    result["fps"] = int(framerate[0]) / int(framerate[1])
                except:
                    result["fps"] = None
    if audio is not None:
        result["channels"] = int(audio["channels"])
        result["frequency"] = int(audio["sample_rate"])
    else:
        result["channels"] = "Нет звука"
        result["sample_rate"] = "Нет звука"

    return result
