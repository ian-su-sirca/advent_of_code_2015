#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *

class Reindeer(object):
    def __init__(self, name, kms, duration, rest):
        self.name = name
        self.kms = kms
        self.duration = duration
        self.rest = rest
        self.distance = 0
        self.remaining_energy = duration
        self.remaining_rest = 0

    def tick(self):
        # am i resting?
        if self.remaining_rest > 0:
            self.remaining_rest -= 1
            return
        # spend 1 energy
        self.remaining_energy -= 1
        self.distance += self.kms
        # do i need rest?
        if self.remaining_energy == 0:
            self.remaining_rest = self.rest
            self.remaining_energy = self.duration

class DayProcessor(Processor):
    def before(self):
        self.deers = []
    def process_line(self, line):
        tokens = line.split(' ')
        self.deers.append(Reindeer(tokens[0], int(tokens[3]), int(tokens[6]), int(tokens[-2])))
        pass
    def after(self):
        for i in range(2503):
            for deer in self.deers:
                deer.tick()
        for deer in self.deers:
            print deer.distance, deer.name

DayProcessor().run()
