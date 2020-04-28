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

        self.path = xlsx_paths[table]
        self.wb = Workbook(self.path)
        self.ws = self.wb.add_worksheet("Лист 1")

        self.count = 2
        self.task = table
        self.write_titles()

    def write_value(self, cell, check, format=lambda x: x):
        if check is not None:
            self.ws.write(cell, format(check))
        else:
            self.ws.write(cell, "?")

    def write_titles(self):
        if self.task == 1:
            self.ws.write("A1", "Имя")
            self.ws.write("B1", "Размер, Мб")
            self.ws.write("C1", "Длительность, с")
            self.ws.write("D1", "Контейнер")
            self.ws.write("E1", "Ширина, px")
            self.ws.write("F1", "Высота, px")
            self.ws.write("G1", "Соотношение")
            self.ws.write("H1", "Дата создания")
            self.ws.write("I1", "FPS")
            self.ws.write("J1", "Битрейт, Кбит/с")
            self.ws.write("K1", "Моно/Стерео")
            self.ws.write("L1", "Частота, кГц")
        elif self.task == 2:
            self.ws.write("A1", "Имя")
            self.ws.write("B1", "Вертик/горизонт")
            self.ws.write("C1", "Перепады по свету")
            self.ws.write("D1", "Горизонт завален")
            self.ws.write("E1", "Размытый фокус")
            self.ws.write("F1", "Перепады по звуку")
            self.ws.write("G1", "Слайдшоу")
            self.ws.write("H1", "Дрожание камеры")
            self.ws.write("I1", "Соблюден баланс по белому")
            self.ws.write("J1", "Ракурс напротив глаз")
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

        self.write_value(f"A{c}", stats["name"])
        # Convert to Mb
        self.write_value(f"B{c}", stats["size"], lambda x: round(x / 2 * 20, 4))
        self.write_value(f"C{c}", stats["duration"], lambda x: round(x, 4))
        self.write_value(f"D{c}", stats["container"])
        self.write_value(f"E{c}", stats["width"])
        self.write_value(f"F{c}", stats["height"])
        self.write_value(
            f"G{c}",
            stats["width"] and stats["height"] and [stats["width"], stats["height"]],
            lambda x: "да" if x[0] / x[1] == 16 / 9 else "нет",
        )
        self.write_value(
            f"H{c}",
            stats["created"],
            lambda x: "{}-{}-{} {}-{}-{}".format(
                x.year, x.month, x.day, x.hour, x.minute, x.second,
            ),
        )
        self.write_value(f"I{c}", stats["fps"])
        self.write_value(f"J{c}", stats["bitrate"])
        self.write_value(
            f"K{c}", stats["channels"], lambda x: "Моно" if x == 1 else "Стерео"
        )
        self.write_value(f"L{c}", stats["frequency"])

        self.count += 1

    def save(self):
        self.wb.close()
        print(f"Создан файл {self.path}")
