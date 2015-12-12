import argparse
import StringIO

class Processor(object):
    def __init__(self):
        p = argparse.ArgumentParser()
        p.add_argument('-i', '--inputfile', default='input.txt')
        p.add_argument('-l', '--inputline', default=None)
        a = p.parse_args()
        if a.inputline:
            self.filename = 'inputline'
            self.filehandle = StringIO.StringIO(a.inputline)
        else:   
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
