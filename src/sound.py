from pydub import AudioSegment
from .ffmpeg import Ffmpeg


def bad_sound(path: str, ffmpeg: Ffmpeg):
    audio_path = ffmpeg.video2audio(path)
    if audio_path is None:
        return "нет"
    song = AudioSegment.from_mp3(audio_path)
    for i in range(len(song) - 1):
        if abs(song[i] - song[i + 1]) > 15:
            ffmpeg.clean_audio(audio_path)
            return "да"

    ffmpeg.clean_audio(audio_path)
    return "нет"
