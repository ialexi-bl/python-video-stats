from threading import Thread
from os.path import basename
from .stats import get_stats
from .xlsx import Xlsx
from .defects.blur import blur_check
from .sound import bad_sound
from .brightness import bad_brightness
from .slideshow import check_slideshow


first_res = dict()


class FirstTableThread(Thread):
    def __init__(self, name: str, videos: [str], xlsx: Xlsx):
        Thread.__init__(self)
        self.videos = videos
        self.name = name
        self.xlsx = xlsx

    def run(self):
        for video in self.videos:
            stats = get_stats(video)
            first_res.update({video: stats})
            self.xlsx.write_stats(basename(video), stats)


class SecondTableThread(Thread):
    def __init__(self, name: str, videos: [str], xlsx: Xlsx):
        Thread.__init__(self)
        self.videos = videos
        self.name = name
        self.xlsx = xlsx

    def run(self):
        res = {}
        for video in self.videos:
            res['slideshow'] = check_slideshow(video)
            res['bad_brightness'] = bad_brightness(video)
            h, w = first_res[video]["height"], first_res[video]["width"]
            if h > w:
                res['orientation'] = 'вертик'
            else:
                res['orientation'] = 'горизонт'

            res['unfocused'] = 'да' if blur_check(video) else 'нет'
            res['sound'] = bad_sound(video, self.name)
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
