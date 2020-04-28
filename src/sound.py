from moviepy.editor import AudioFileClip
from os.path import join, dirname
from pydub import AudioSegment
from .config import TEMP_FOLDER


def bad_sound(path: str, thread):
    audio = AudioFileClip(path)
    temp_file = join(TEMP_FOLDER, f"{thread}.mp3")

    try:
        audio.write_audiofile(temp_file)
    except IndexError:
        return "нет"

    song = AudioSegment.from_mp3(temp_file)
    for i in range(len(song) - 1):
        if abs(song[i] - song[i + 1]) > 15:
            return "да"
    return "нет"
