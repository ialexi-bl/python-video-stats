from os import path, unlink
import subprocess
import tempfile
import json

FFPROBE_PATH = path.join(path.dirname(__file__), "lib\\ffprobe.exe")
FFMPEG_PATH = path.join(path.dirname(__file__), "lib\\ffmpeg.exe")


class Ffmpeg:
    def __init__(self):
        self.tempfolder = tempfile.TemporaryDirectory()

    def close(self):
        self.tempfolder.cleanup()

    def run_ffprobe(self, args):
        return subprocess.getoutput(f"{FFPROBE_PATH} {args}")

    def run_ffmpeg(self, args):
        return subprocess.getoutput(f"{FFMPEG_PATH} {args}")

    def get_data(self, path):
        output = self.run_ffprobe(
            f'-v quiet -print_format json -show_streams -show_format "{path}"'
        )
        return json.loads(output)

    def video2audio(self, file):
        audio_file = path.join(self.tempfolder.name, path.basename(file) + ".mp3")
        self.run_ffmpeg(f'-i video.mp4 -f "{file}" -ab 192000 -vn "{audio_file}"')
        if not path.exists(audio_file):
            return None
        return audio_file

    def clean_audio(self, audio_file):
        unlink(audio_file)
