#!/usr/bin/env python
from common import *

class WrappingPaper(Processor):
    def before(self):
        self.area = 0
    def process_line(self, line):
        (w, h, l) = map(lambda x: int(x), line.split('x'))
        wh = w*h
        hl = h*l
        lw = l*w
        slack = min(wh, min(hl, lw))
        area = 2 * (wh + hl + lw) + slack
        self.area += area
    def after(self):
        print self.area

WrappingPaper().run()
