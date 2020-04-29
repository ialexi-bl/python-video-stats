from xlsxwriter import Workbook
from os import path

xlsx_paths = {
    1: path.expanduser("~/Desktop/Критерии 1-го уровня.xlsx"),
    2: path.expanduser("~/Desktop/Критерии 2-го уровня.xlsx"),
    3: path.expanduser("~/Desktop/Лучшее Ой Сложно.xlsx"),
}


class Xlsx:
    def __init__(self, table):
        # if table not in xlsx_paths:
        #     raise Exception("Invalid table")

        # self.path = xlsx_paths[table]
        self.wb1 = Workbook(xlsx_paths[1])
        self.ws1 = self.wb1.add_worksheet("List 1")
        self.wb2 = Workbook(xlsx_paths[2])
        self.ws2 = self.wb2.add_worksheet("List 1")

        self.savecounter = 1
        self.count1 = 2
        self.count2 = 2
        self.task = table
        self.write_titles()

    def write_best(self, data):
        wb = Workbook(xlsx_paths[3])
        ws = wb.add_worksheet()
        ws.write("A1", "Имя")
        counter = 2
        for d in data:
            ws.write(f"A{counter}", d)
            counter += 1
        wb.close()

    def write_titles(self):
        self.ws1.write("A1", "Имя")
        self.ws1.write("B1", "Размер, Мб")
        self.ws1.write("C1", "Длительность, с")
        self.ws1.write("D1", "Контейнер")
        self.ws1.write("E1", "Ширина, px")
        self.ws1.write("F1", "Высота, px")
        self.ws1.write("G1", "Соотношение")
        self.ws1.write("H1", "Дата создания, гг-мм-дд чч-мм-сс")
        self.ws1.write("I1", "Частота кадров, fps")
        self.ws1.write("J1", "Битрейт, Кбит/с")
        self.ws1.write("K1", "Количество звуковых каналов, моно/стерео")
        self.ws1.write("L1", "Частота дискретизации, кГц")

        self.ws2.write("A1", "Имя")
        self.ws2.write("B1", "Вертикальное/ горизонтальное, В/Г")
        self.ws2.write("C1", "Резкие перепады света в видео, да/нет")
        self.ws2.write("D1", "Наличие заваленного горизонта, да/нет")
        self.ws2.write(
            "E1", "Отсутствие резкого фокуса хоть на одном кадре видео, да/нет"
        )
        self.ws2.write("F1", "Резкие перепады по звуку в видео, да/нет")
        self.ws2.write("G1", "Является ли видео слайдшоу, да/нет")
        self.ws2.write("H1", "Дрожание камеры в ролике, да/нет")
        self.ws2.write("I1", "Соблюден ли баланс по белому, да/нет")
        self.ws2.write("J1", "Ракурс соблюден, да/нет")

    def write_value(self, table, cell, check, format=lambda x: x):
        ws = self.ws1 if table == 1 else self.ws2
        if check is not None:
            ws.write(cell, format(check))
        else:
            ws.write(cell, "?")

    def write_stats(self, filename, stats):
        c = self.count1

        self.write_value(1, f"A{c}", stats["name"])
        # Convert to Mb
        self.write_value(1, f"B{c}", stats["size"], lambda x: round(x / 2 * 20, 4))
        self.write_value(1, f"C{c}", stats["duration"], lambda x: round(x, 4))
        self.write_value(1, f"D{c}", stats["container"])
        self.write_value(1, f"E{c}", stats["width"])
        self.write_value(1, f"F{c}", stats["height"])
        self.write_value(
            1,
            f"G{c}",
            stats["width"] and stats["height"] and [stats["width"], stats["height"]],
            lambda x: "да" if x[0] / x[1] == 16 / 9 else "нет",
        )
        self.write_value(
            1,
            f"H{c}",
            stats["created"],
            lambda x: "{}-{}-{} {}-{}-{}".format(
                x.year, x.month, x.day, x.hour, x.minute, x.second,
            ),
        )
        self.write_value(1, f"I{c}", stats["fps"])
        self.write_value(1, f"J{c}", stats["bitrate"])
        self.write_value(
            1,
            f"K{c}",
            stats["channels"],
            lambda x: "Моно" if x == 1 else ("Стерео" if x == 2 else x),
        )
        self.write_value(1, f"L{c}", stats["frequency"])

        self.count1 += 1

    def write_defects(self, filename, data):
        c = self.count2

        self.write_value(2, f"A{c}", path.basename(filename))
        # Convert to Mb
        self.write_value(2, f"B{c}", data["orientation"])
        self.write_value(2, f"C{c}", data["bad_brightness"])
        self.write_value(2, f"D{c}", data["rotated"])
        self.write_value(2, f"E{c}", data["unfocused"])
        self.write_value(2, f"F{c}", data["sound"])
        self.write_value(2, f"G{c}", data["slideshow"])
        self.write_value(2, f"H{c}", data["unstable"])
        # self.write_value(f"I{c}", data["white_balance"])
        self.write_value(2, f"I{c}", "?")
        # self.write_value(f"J{c}", stats["bitrate"])
        self.write_value(2, f"J{c}", "?")

        self.count2 += 1

    def save(self):
        self.wb1.close()
        self.wb2.close()
