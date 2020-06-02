from xlsxwriter import Workbook
from os import path

class Xlsx:
    def __init__(self, path):
        self.wb = Workbook(path)
        self.ws = self.wb.add_worksheet("List 1")

        self.savecounter = 1
        self.count = 2
        self.write_titles()

    def write_titles(self):
        self.ws.write("A1", "Filename")
        self.ws.write("B1", "Size, Mb")
        self.ws.write("C1", "Duration, s")
        self.ws.write("D1", "Format")
        self.ws.write("E1", "Width, px")
        self.ws.write("F1", "Height, px")
        self.ws.write("G1", "Ratio")
        self.ws.write("H1", "Created, yy-mm-dd hh-mm-ss")
        self.ws.write("I1", "FPS")
        self.ws.write("J1", "Bitrate, Kbit/s")
        self.ws.write("K1", "Amount of sound channels")
        self.ws.write("L1", "Sampling rate, kHz")

    def write_value(self, cell, check, format=lambda x: x):
        if check is not None:
            self.ws.write(cell, format(check))
        else:
            self.ws.write(cell, "?")

    def write_line(self, filename, stats):
        c = self.count

        self.write_value(f"A{c}", stats["name"])
        self.write_value(f"B{c}", round(stats["size"] / 2 ** 20, 4))
        self.write_value(f"C{c}", stats["duration"], lambda x: round(x, 4))
        self.write_value(f"D{c}", stats["container"])
        self.write_value(f"E{c}", stats["width"])
        self.write_value(f"F{c}", stats["height"])
        self.write_value(
            f"G{c}",
            stats["width"] and stats["height"] and [stats["width"], stats["height"]],
            lambda x: x[0] / x[1]
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
        self.write_value(f"K{c}", stats["channels"])
        self.write_value(f"L{c}", stats["frequency"])

        self.count += 1

    def save(self):
        self.wb.close()
