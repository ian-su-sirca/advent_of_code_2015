#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *

class LightsMatrix(object):
    def __init__(self, width, height):
        self.lights = []
        for i in range(height):
            self.lights.append([0] * width)

    def set(self, x0, y0, x1, y1, value):
        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                self.lights[x][y] = value

    def toggle(self, x0, y0, x1, y1):
        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                self.lights[x][y] = (self.lights[x][y] + 1) % 2

    def count(self):
        return sum([sum(row) for row in self.lights])

class DayProcessor(Processor):
    def before(self):
        self.matrix = LightsMatrix(1000, 1000)
        pass
    def process_line(self, line):
        tokens = line.split(' ')
        (x0, y0) = map(lambda x: int(x), tokens[-3].split(','))
        (x1, y1) = map(lambda x: int(x), tokens[-1].split(','))
        if line.startswith('turn on'):
            self.matrix.set(x0, y0, x1, y1, 1)
        elif line.startswith('turn off'):
            self.matrix.set(x0, y0, x1, y1, 0)
        elif line.startswith('toggle'):
            self.matrix.toggle(x0, y0, x1, y1)
        else:
            raise ValueError
    def after(self):
        print self.matrix.count()
        pass

DayProcessor().run()
