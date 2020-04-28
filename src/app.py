from .tables import *
from .xlsx import Xlsx
from os import path
import os


results = {}


def main(table, dirname):
    if not path.isdir(dirname):
        print("Path is not a directory")
        return

    filenames = os.listdir(dirname)
    videos = [
        path.join(dirname, filename)
        for filename in filenames
        if filename[-3:].lower() in ["mp4", "mov", "avi"]
    ]

    xlsx = Xlsx(table)

    threads_count = 8
    threads = []

    for i in range(threads_count):
        name = "Thread #%s" % i
        if table == 1:
            thread = FirstTableThread(str(i), videos[i::threads_count], xlsx)
        elif table == 2:
            thread = SecondTableThread(str(i), videos[i::threads_count], xlsx)
        else:
            thread = ThirdTableThread(str(i), videos[i::threads_count], xlsx)

        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    xlsx.save()


def launch():
    print("Введите путь к папке с видео:")
    dirname = input()
    main(1, path.expanduser(dirname))
