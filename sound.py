import wave
from pydub import AudioSegment
from moviepy.editor import VideoFileClip
from os import system


def get_wav(source, thread):
    VideoFileClip(source).audio.write_audiofile(f'{thread}.mp3')


def get_length(source, thread):
    get_wav(source, thread)
    AudioSegment.from_mp3(f'{thread}.mp3').export(f'{thread}.wav', format="wav")
    wav = wave.open(f'{thread}.wav', mode="rb")
    nchannels, sampwidth, framerate, nframes, comptype, compname = wav.getparams()
    return nframes / framerate


def bad_sound(source, thread):
    get_wav(source, thread)
    song = AudioSegment.from_mp3(f'{thread}.wav')
    for i in range(len(song) - 1):
        if abs(song[i] - song[i + 1]) > 15:
            return 'bad'
    return 'good'


print(get_length('GH012651.MP4', 0))
