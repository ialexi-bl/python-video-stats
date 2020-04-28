from threading import Thread
from os.path import basename
from .ffmpeg import Ffmpeg
from .stats import get_stats
from .xlsx import Xlsx
from .defects.blur import blur_check
from .sound import bad_sound
from .brightness import bad_brightness
from .slideshow import check_slideshow
from .defects.horizon import check_rotation_deffects


class FirstTableThread(Thread):
    def __init__(self, name: str, videos: [str], xlsx: Xlsx):
        Thread.__init__(self)
        self.videos = videos
        self.name = name
        self.xlsx = xlsx

    def run(self):
        ffmpeg = Ffmpeg()
        for video in self.videos:
            stats = get_stats(video, ffmpeg)
            self.xlsx.write_stats(basename(video), stats)


class SecondTableThread(Thread):
    def __init__(self, name: str, videos: [str], xlsx: Xlsx):
        Thread.__init__(self)
        self.videos = videos
        self.name = name
        self.xlsx = xlsx

    def run(self):
        res = {}
        ffmpeg = Ffmpeg()
        for video in self.videos:
            res["slideshow"], w, h = check_slideshow(video)
            res["bad_brightness"] = bad_brightness(video)
            if h > w:
                res["orientation"] = "В"
            else:
                res["orientation"] = "Г"
            # rot = check_rotation_deffects(video)
            rot = [False, False]
            res["rotated"] = "да" if rot[1] else "нет"
            res["unstable"] = "да" if rot[0] else "нет"
            res["unfocused"] = "да" if blur_check(video) else "нет"
            res["sound"] = bad_sound(video, ffmpeg)
            res["name"] = basename(video)
            # TODO: res['white_balanced'], eyes
<<<<<<< HEAD
            self.xlsx.write_defects(video, res)
=======

            second_res.update({video: res})
            self.xlsx.write_stats(basename(video), res)
>>>>>>> 105b06ceb549be4d1f55f9f8959dca7f1d03f05d


class ThirdTableThread(Thread):
    def __init__(self, name: str, videos: [str], xlsx: Xlsx):
        Thread.__init__(self)
        self.videos = videos
        self.name = name
        self.xlsx = xlsx

    def run(self):
        res = []
        for video in self.videos:
            # TODO: everything xD
            self.xlsx.write_stats(basename(video), res)
