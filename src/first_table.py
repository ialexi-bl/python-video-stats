from stats import get_stats

class FirstTableThread(Thread):
    def __init__(self, name, write_line):
        Thread.__init__(self)
        self.name = name
        self.write_line = write_line
        
    def run(self):
                