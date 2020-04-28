from os.path import join, dirname
from pydub import AudioSegment
from .config import TEMP_FOLDER
from .ffmpeg import Ffmpeg


def bad_sound(path: str, ffmpeg: Ffmpeg):
    audio_path = ffmpeg.video2audio(path)

    if audio_path is None:
        return "нет"

    song = AudioSegment.from_mp3(audio_file)
    for i in range(len(song) - 1):
        if abs(song[i] - song[i + 1]) > 15:
            ffmpeg.clean_audio(audio_file)
            return "да"

    ffmpeg.clean_audio(audio_file)
    return "нет"
