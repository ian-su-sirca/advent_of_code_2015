#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *
from itertools import permutations

class DayProcessor(Processor):
    def before(self):
        self.people = set(['You'])
        self.happiness = { 'You': {} }
        pass
    def process_line(self, line):
        line = line.rstrip('.')
        tokens = line.split()
        left = tokens[0]
        right = tokens[-1]
        happiness = int(tokens[3])
        if tokens[2] == 'lose':
            happiness = -happiness
        self.people.add(left)
        self.people.add(right)
        if left not in self.happiness:
            self.happiness[left] = {}
        self.happiness[left][right] = happiness
    def after(self):
        # add You pairings
        for ppl in self.people:
            self.happiness[ppl]['You'] = 0
            self.happiness['You'][ppl] = 0
        for p in permutations(self.people):
            happiness = 0
            for i in range(len(p)):
                if i == len(p) - 1:
                    right = p[0]
                else:
                    right = p[i+1]
                left = p[i]
                lr_happiness = self.happiness[left][right]
                rl_happiness = self.happiness[right][left]
                happiness += lr_happiness + rl_happiness
            print happiness, p
        pass

DayProcessor().run()
