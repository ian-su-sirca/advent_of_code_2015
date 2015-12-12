#!/usr/bin/env python
from common import *

class DayProcessor(Processor):
    def before(self):
        self.coords = {}
        self.x = 0
        self.y = 0
    def move_dir(self, move):
        if move == '^':
            self.y -= 1
        elif move == 'v':
            self.y += 1
        elif move == '<':
            self.x -= 1
        elif move == '>':
            self.x += 1
        else:
            raise ValueError(move)
        coord = '(%d,%d)' % (self.x, self.y)
        if coord not in self.coords:
            self.coords[coord] = 1
        else:
            self.coords[coord] += 1
    def process_line(self, line):
        for move in line:
            self.move_dir(move)
        pass
    def after(self):
        print len(self.coords.keys())

DayProcessor().run()
