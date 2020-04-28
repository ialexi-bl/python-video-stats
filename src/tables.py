from threading import Thread
from os.path import basename
from .stats import get_stats
from .xlsx import Xlsx


class FirstTableThread(Thread):
    def __init__(self, name: str, videos: [str], xlsx: Xlsx):
        Thread.__init__(self)
        self.videos = videos
        self.name = name
        self.xlsx = xlsx

    def run(self):
        for video in self.videos:
            stats = get_stats(video)
            self.xlsx.write_stats(basename(video), stats)


class SecondTableThread(Thread):
    def __init__(self, name: str, videos: [str], xlsx: Xlsx):
        Thread.__init__(self)
        self.videos = videos
        self.name = name
        self.xlsx = xlsx

    def run(self):
        res = []
        for video in self.videos:
            # TODO
            self.xlsx.write_stats(basename(video), res)


class ThirdTableThread(Thread):
    def __init__(self, name: str, videos: [str], xlsx: Xlsx):
        Thread.__init__(self)
        self.videos = videos
        self.name = name
        self.xlsx = xlsx

    def run(self):
        res = []
        for video in self.videos:
            # TODO
            self.xlsx.write_stats(basename(video), res)
