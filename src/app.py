from xlsxwriter import Workbook as Wb
from os.path import expanduser, join, dirname
from threading import Thread
from src.blur import is_blurred
from src.sound import bad_sound
from src.brightness import bad_brightness


results = dict()


class Test(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run1(self, n, videos):  # 1st table
        # TODO: find bitrate, audio info; run tests, fill results
        pass

    def run2(self, n, videos):  # 2nd table
        # TODO: run tests, fill results
        pass

    def run3(self, n, videos):  # final table
        # TODO: run tests, fill results
        pass


def main(table):
    if table == 1:
        level1 = Wb(expanduser('~\\Desktop\\Критерии 1-го уровня.xlsx'))
    elif table == 2:
        level2 = Wb(expanduser('~\\Desktop\\Критерии 2-го уровня.xlsx'))
    else:
        level3 = Wb(expanduser('~\\Desktop\\Крупности.xlsx'))
    videos = []
    # TODO: fill videos
    for i in range(8):
        name = "Thread #%s" % i
        my_thread = Test(name)
        if table == 1:
            my_thread.run1(i, videos[i::8])
        elif table == 2:
            my_thread.run2(i, videos[i::8])
        else:
            my_thread.run3(i, videos[i::8])
    # TODO: sort answers
    if table == 1:
        level1.close()
    elif table == 2:
        level2.close()
    else:
        level3.close()
