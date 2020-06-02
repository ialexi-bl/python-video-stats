from .xlsx import Xlsx
from .stats import get_stats
from os import path
import os

VIDEO_EXT = ["mp4", "mov", "avi"]


def launch():
    print("Input path to folder containing video files:")
    dirname = input()

    default = get_filename(path.expanduser("~/video-stats.xlsx"))
    print(f"Input path to resulting table (default {default})")

    xlsxname = input() or default
    main(path.expanduser(dirname), path.expanduser(xlsxname))

    print("Enter, чтобы закрыть...")
    try:
        input()
    except:
        pass



def main(dirname, xlsxname):
    if path.isdir(dirname):
        filenames = os.listdir(dirname)
        videos = [
            path.join(dirname, filename)
            for filename in filenames
            if get_ext(filename) in VIDEO_EXT
        ]
    elif not path.isfile(dirname):
        print("No such file")
        return
    elif get_ext(dirname) in VIDEO_EXT:
        videos = [dirname]
    else:
        print("Not a video file")
        return


    xlsx = Xlsx(get_filename(xlsxname))

    threads_count = 12
    threads = []

    try:
        for i in range(threads_count):
            thread = WorkerThread( videos[i::threads_count], xlsx)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        xlsx.save()
    except e:
        print(f"Error processing videos: {e}")


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
                self.xlsx.write_line(basename(video), stats)
            except Exception as e:
                print(
                    f"Failed to process file {basename(video)}: {e}"
                )


def get_ext(filename):
    return filename[-3:].lower()

def get_filename(filename):
    if !path.isfile(filename):
        return filename

    count = 1
    while path.isfile(filename + f"({count})"):
        count += 1

    return filename + f"({count})"
