from pydub import AudioSegment
from moviepy.editor import AudioFileClip


def bad_sound(source, thread):
    try:
        AudioFileClip(f"./{source}").write_audiofile(f"./{thread}.mp3")
    except IndexError:
        return "no audio"
    song = AudioSegment.from_mp3(f"{thread}.wav")
    for i in range(len(song) - 1):
        if abs(song[i] - song[i + 1]) > 15:
            return "bad"
    return "good"
