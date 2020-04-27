from sound import get_length, bad_sound
from xlsxwriter import Workbook as wb
from os.path import expanduser


def main():  # creating answer files, calling info functions
    level1 = wb(expanduser('~\\Desktop\\Критерии 1-го уровня.xlsx'))
    level2 = wb(expanduser('~\\Desktop\\Критерии 2-го уровня.xlsx'))
    last = wb(expanduser('~\\Desktop\\Крупности.xlsx'))

    # magic

    level1.close()
    level2.close()
    last.close()


if __name__ == "__main__":
    main()
    exit = input()
