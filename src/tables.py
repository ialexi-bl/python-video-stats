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
            try:
                stats = get_stats(video, ffmpeg)
                results1.append(stats)
                self.xlsx.write_stats(basename(video), stats)
            except Exception as e:
                print(
                    f"Не удалось обработать первый критерии для файла {basename(video)}: {e}"
                )
                results1.append(None)

            try:
                res = {}
                res["slideshow"], w, h = check_slideshow(video)
                res["bad_brightness"] = "нет"
                if h > w:
                    res["orientation"] = "В"
                else:
                    res["orientation"] = "Г"
                rot = check_rotation_deffects(video)
                res["rotated"] = "да" if rot[1] else "нет"
                res["unstable"] = "да" if rot[0] else "нет"
                res["unfocused"] = "нет" if blur_check(video) else "да"
                res["sound"] = bad_sound(video, ffmpeg)
                res["name"] = basename(video)
                self.xlsx.write_defects(video, res)
                results2.append(res)
            except Exception as e:
                print(
                    f"Не удалось обработать вторые критерии для файла {basename(video)}: {str(e)}"
                )
                results2.append(None)
