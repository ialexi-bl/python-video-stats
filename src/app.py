from xlsxwriter import Workbook as Wb
from os.path import expanduser
from threading import Thread


class Test(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run1(self, n):  # 1st table
        pass

    def run2(self, n):  # 2nd table
        pass

    def run3(self, n):  # final table
        pass


def main(table):
    if table == 1:
        level1 = Wb(expanduser('~\\Desktop\\Критерии 1-го уровня.xlsx'))
    elif table == 2:
        level2 = Wb(expanduser('~\\Desktop\\Критерии 2-го уровня.xlsx'))
    else:
        level3 = Wb(expanduser('~\\Desktop\\Крупности.xlsx'))
    for i in range(8):
        name = "Thread #%s" % i
        my_thread = Test(name)
        if table == 1:
            my_thread.run1(i)
        elif table == 2:
            my_thread.run2(i)
        else:
            my_thread.run3(i)
    if table == 1:
        level1.close()
    elif table == 2:
        level2.close()
    else:
        level3.close()
