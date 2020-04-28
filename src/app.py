from xlsxwriter import Workbook as Wb
from os.path import expanduser, join, dirname
from threading import Thread
from src.blur import is_blurred
from src.sound import bad_sound
from src.brightness import bad_brightness
from first_table import FirstTableThread


results = {}


def main(table):
    
    if table == 1:
        wb = Wb(expanduser("~\\Desktop\\Критерии 1-го уровня.xlsx"))
    if table == 1:
        level1 = 
    elif table == 2:
        level2 = Wb(expanduser("~\\Desktop\\Критерии 2-го уровня.xlsx"))
    else:
        level3 = Wb(expanduser("~\\Desktop\\Крупности.xlsx"))


    ws = wb.add_worksheet("Лист 1")
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

if __name__ == 'main':
    print("Введите путь к папке с видео:")
    dirname = input()
    main(dirname)
