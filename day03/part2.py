#!/usr/bin/env python
from common import *

class Mover(object):
    def __init__(self):
        self.x = 0
        self.y = 0
    def move(self, move):
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
    def coord(self):
        return '(%d,%d)' % (self.x, self.y)

class DayProcessor(Processor):
    def before(self):
        self.coords = {}
        self.santa = Mover()
        self.robot = Mover()
    def move_dir(self, move, isSanta):
        if isSanta:
            mover = self.santa
        else:
            mover = self.robot
        mover.move(move)
        coord = mover.coord()
        if coord not in self.coords:
            self.coords[coord] = 1
        else:
            self.coords[coord] += 1
    def process_line(self, line):
        isSanta = True
        for move in line:
            self.move_dir(move, isSanta)
            isSanta = not isSanta
    def after(self):
        print len(self.coords.keys())

DayProcessor().run()
