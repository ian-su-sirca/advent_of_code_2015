#!/usr/bin/env python
from common import *

class WrappingPaper(Processor):
    def before(self):
        self.ribbon = 0
    def process_line(self, line):
        sides = map(lambda x: int(x), line.split('x'))
        (w, h) = sorted(sides)[:2]
        ribbon = 2 * (w + h)
        bow = sides[0] * sides[1] * sides[2]
        self.ribbon += ribbon + bow
        print line, ribbon, bow
    def after(self):
        print self.ribbon

WrappingPaper().run()
