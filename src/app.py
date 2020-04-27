from sound import get_length, bad_sound
from xlsxwriter import Workbook as Wb
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


def main():
    level1 = Wb(expanduser('~\\Desktop\\Критерии 1-го уровня.xlsx'))
    #  level2 = Wb(expanduser('~\\Desktop\\Критерии 2-го уровня.xlsx'))
    #  last = Wb(expanduser('~\\Desktop\\Крупности.xlsx'))
    for i in range(8):
        name = "Thread #%s" % i
        my_thread = Test(name)
        my_thread.run1(i)
        #  my_thread.run2(i)
        #  my_thread.run3(i)
    level1.close()
    #  level2.close()
    #  last.close()


if __name__ == "__main__":
    main()
    exit = input()
