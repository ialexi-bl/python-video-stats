from xlsxwriter import Workbook
from os import path

xlsx_paths = {
    1: path.expanduser("~/Desktop/Критерии 1-го уровня.xlsx"),
    2: path.expanduser("~/Desktop/Критерии 2-го уровня.xlsx"),
    3: path.expanduser("~/Desktop/Крупности.xlsx"),
}


class Xlsx:
    def __init__(self, table):
        if table not in xlsx_paths:
            raise Exception("Invalid table")

        self.wb = Workbook(xlsx_paths[table])
        self.ws = self.wb.add_worksheet("Лист 1")

        self.count = 2
        self.task = table
        self.write_titles()

    def write_titles(self):
        if self.task == 1:
            self.ws.write("A1", "Имя")
            self.ws.write("B1", "Размер, Мб")
            self.ws.write("C1", "Длительность, с")
            self.ws.write("D1", "Контейнер")
            self.ws.write("E1", "Ширина, px")
            self.ws.write("F1", "Высота, px")
            self.ws.write("G1", "Соотношение")
            self.ws.write("H1", "Дата создания, гг-мм-дд чч-мм-сс")
            self.ws.write("I1", "Частота кадров, fps")
            self.ws.write("J1", "Битрейт, Кбит/с")
            self.ws.write("K1", "Количество звуковых каналов, моно/стерео")
            self.ws.write("L1", "Частота дискретизации, кГц")
        elif self.task == 2:
            self.ws.write("A1", "Имя")
            self.ws.write("B1", "Вертикальное/ горизонтальное, В/Г")
            self.ws.write("C1", "Резкие перепады света в видео, да/нет")
            self.ws.write("D1", "Наличие заваленного горизонта, да/нет")
            self.ws.write("E1", "Отсутствие резкого фокуса хоть на одном кадре видео, да/нет")
            self.ws.write("F1", "Резкие перепады по звуку в видео, да/нет")
            self.ws.write("G1", "Является ли видео слайдшоу, да/нет")
            self.ws.write("H1", "Дрожание камеры в ролике, да/нет")
            self.ws.write("I1", "Соблюден ли баланс по белому, да/нет")
            self.ws.write("J1", "Ракурс соблюден, да/нет")
        else:
            self.ws.write("A1", "Имя")
            self.ws.write("B1", "Лицо человека")
            self.ws.write("C1", "Средний план, с")
            self.ws.write("D1", "Крупный план, с")
            self.ws.write("E1", "Дальний план, с")
            self.ws.write("F1", "Рука, с")
            self.ws.write("G1", "Ноги, с")
            self.ws.write("H1", "Объект - робот, с")

    def write_stats(self, filename, stats):
        c = self.count

        if self.task == 1:
            self.ws.write(f"A{c}", filename)
            self.ws.write(f"B{c}", stats["size"])
            self.ws.write(f"C{c}", stats["duration"])
            self.ws.write(f"D{c}", stats["container"])
            self.ws.write(f"E{c}", stats["width"])
            self.ws.write(f"F{c}", stats["height"])
            self.ws.write(f"G{c}", "да" if stats["width"] / stats["height"] == 16 / 9 else "нет")
            self.ws.write(f"H{c}", stats["created"])
            self.ws.write(f"I{c}", stats["fps"])
            self.ws.write(f"J{c}", stats["bitrate"])
            self.ws.write(f"K{c}", "Моно" if stats["channels"] == 1 else "Стерео")
            self.ws.write(f"L{c}", stats["frequency"])
        elif self.task == 2:
            self.ws.write(f"A{c}", filename)
            self.ws.write(f"B{c}", stats["orientation"])
            self.ws.write(f"C{c}", stats["bad_brightness"])
            self.ws.write(f"D{c}", stats["rotated"])
            self.ws.write(f"E{c}", stats["unfocused"])
            self.ws.write(f"F{c}", stats["sound"])
            self.ws.write(f"G{c}", stats["slideshow"])
            self.ws.write(f"H{c}", stats["unstable"])
            self.ws.write(f"I{c}", stats["white_balanced"])
        else:
            pass
        self.count += 1

    def save(self):
        self.wb.close()
