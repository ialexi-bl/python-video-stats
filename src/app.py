from .xlsx import Xlsx
from .stats import get_stats
from .ffmpeg import Ffmpeg
from threading import Thread
from os import path
import time
import os

VIDEO_EXT = [".mp4", ".mov", ".avi"]


def launch():
    print("Input path to folder containing video files:")
    dirname = input()

    default = get_filename(normalize("~/video-stats.xlsx"))
    print(f"Input path to resulting table (default {default})")

    xlsxname = input() or default
    main(normalize(dirname), normalize(xlsxname))

    print("Enter, чтобы закрыть...")
    try:
        input()
    except:
        pass


def main(dirname, xlsxname):
    if path.isdir(dirname):
        filenames = os.listdir(dirname)
        videos = [
            path.join(dirname, filename) for filename in filenames
            if path.splitext(filename)[1] in VIDEO_EXT
        ]
    elif not path.isfile(dirname):
        print("No such file")
        return
    elif path.splitext(dirname)[1] in VIDEO_EXT:
        videos = [dirname]
    else:
        print("Not a video file")
        return

    print(f"Found {len(videos)} video files")

    if path.isdir(xlsxname):
        xlsxname = get_filename(xlsxname + '/video-stats.xlsx')
        print(f'Saving results to {xlsxname}')

    xlsx = Xlsx(xlsxname)

    threads_count = 12
    threads = []
    start = time.time()

    try:
        for i in range(threads_count):
            thread = WorkerThread(videos[i::threads_count], xlsx)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        xlsx.save()
    except e:
        print(f"Error processing videos: {e}")

    dur = round(time.time() - start, 2)
    print(f"Done in {dur}s")


class WorkerThread(Thread):
    def __init__(self, videos, xlsx: Xlsx):
        Thread.__init__(self)
        self.videos = videos
        self.xlsx = xlsx

    def run(self):
        ffmpeg = Ffmpeg()

        for video in self.videos:
            try:
                stats = get_stats(video, ffmpeg)
                self.xlsx.write_line(path.basename(video), stats)
            except Exception as e:
                print(f"Failed to process file {path.basename(video)}: {e}")


def normalize(file):
    return path.normpath(path.expanduser(file))


def get_filename(filename):
    if not path.isfile(filename):
        return filename

    base, ext = path.splitext(filename)

    count = 1
    while path.isfile(f"{base} ({count}){ext}"):
        count += 1

    return f"{base} ({count}){ext}"
