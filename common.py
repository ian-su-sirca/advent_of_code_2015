import argparse

class Processor(object):
    def __init__(self):
        p = argparse.ArgumentParser()
        p.add_argument('-i', '--inputfile', default='input.txt')
        a = p.parse_args()
        self.filename = a.inputfile
        self.filehandle = open(a.inputfile, 'r')

    def run(self):
        self.before()
        for line in self.filehandle:
            self.process_line(line.rstrip())
        self.after()

    def before(self):
        pass
    def after(self):
        pass

    def process_line(self, line):
        raise NotImplementedError
