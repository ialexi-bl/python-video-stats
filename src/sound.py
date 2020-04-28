from os.path import join, dirname
from pydub import AudioSegment
from .config import TEMP_FOLDER


def bad_sound(path: str, thread):
    temp_file = join(TEMP_FOLDER, f"{thread}.mp3")

    song = AudioSegment.from_mp3(temp_file)
    for i in range(len(song) - 1):
        if abs(song[i] - song[i + 1]) > 15:
            return "да"
    return "нет"
