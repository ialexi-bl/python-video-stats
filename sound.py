import wave
from pydub import AudioSegment
import subprocess


def get_length(source):
    wav = wave.open(source, mode="rb")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    return nframes / framerate


def bad_sound(source):
    command = '''ffmpeg -i /test.avi -ab 160k -ac 2 -ar 44100 -vn audio.wav'''
    subprocess.call(command, shell=True)
    song = AudioSegment.from_wav(source)
    for i in range(len(song) - 1):
        if abs(song[i] - song[i + 1]) > 15:
            return 'bad'
    return 'good'
