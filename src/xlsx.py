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
        self.write_titles()
        self.task = table

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

        if self.task == 1:
            self.ws.write(f"A{c}", filename)
            self.ws.write(f"B{c}", stats["size"])
            self.ws.write(f"C{c}", stats["duration"])
            self.ws.write(f"D{c}", stats["container"])
            self.ws.write(f"E{c}", stats["width"])
            self.ws.write(f"F{c}", stats["height"])
            self.ws.write(f"G{c}", round(stats["width"] / stats["height"], 8))
            self.ws.write(f"H{c}", stats["created"])
            self.ws.write(f"I{c}", stats["fps"])
            self.ws.write(f"J{c}", stats["bitrate"])
            self.ws.write(f"K{c}", "Моно" if stats["channels"] == 1 else "Стерео")
            self.ws.write(f"L{c}", stats["frequency"])
        elif self.task == 2:
            pass
        else:
            pass
        self.count += 1

    def save(self):
        self.wb.close()
