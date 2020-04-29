from threading import Thread
from os.path import basename
from .ffmpeg import Ffmpeg
from .stats import get_stats
from .xlsx import Xlsx
from .defects.blur import blur_check
from .sound import bad_sound
from .brightness import bad_brightness
from .slideshow import check_slideshow


first_res, second_res = dict(), dict()


def get_results():
    return first_res, second_res


results1 = []
results2 = []


def get_results():
    return results1, results2


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
            results1.append(stats)
            self.xlsx.write_stats(basename(video), stats)
            first_res.update({video: stats})

            res = {}
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
            res["name"] = ".".join(
                [
                    *basename(video).split(".")[:-1],
                    basename(video).split(".")[-1].lower(),
                ]
            )
            # TODO: res['white_balanced'], eyes
            self.xlsx.write_defects(video, res)
            results2.append(res)


# class SecondTableThread(Thread):
#     def __init__(self, name: str, videos: [str], xlsx: Xlsx):
#         Thread.__init__(self)
#         self.videos = videos
#         self.name = name
#         self.xlsx = xlsx

#     def run(self):
#         res = {}
#         ffmpeg = Ffmpeg()
#         for video in self.videos:


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
