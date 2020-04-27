from sound import get_length, bad_sound
from xlsxwriter import Workbook as wb
from os.path import expanduser
from threading import Thread


class Test(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run1(self):  # 1st table
        pass

    def run2(self):  # 2nd table
        pass

    def run3(self):  # final table
        pass


def test1():
    level1 = wb(expanduser('~\\Desktop\\Критерии 1-го уровня.xlsx'))
    for i in range(8):
        name = "Thread #%s" % i
        my_thread = Test(name)
        my_thread.run1(i)
    level1.close()


def test2():
    level2 = wb(expanduser('~\\Desktop\\Критерии 2-го уровня.xlsx'))
    for i in range(8):
        name = "Thread #%s" % i
        my_thread = Test(name)
        my_thread.run2(i)
    level2.close()


def final_test():
    last = wb(expanduser('~\\Desktop\\Крупности.xlsx'))
    for i in range(8):
        name = "Thread #%s" % i
        my_thread = Test(name)
        my_thread.run3(i)
    last.close()


def main():
    test1()
    # test2()
    # final_test()


if __name__ == "__main__":
    main()
    exit = input()
