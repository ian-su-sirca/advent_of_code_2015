#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *

class DayProcessor(Processor):
    def before(self):
        self.nice = 0
    def process_line(self, line):
        # rule 1
        tokens = {}
        rule1 = False
        rule2 = False
        for i in range(0, len(line)):
            token = line[i:i+2]
            if token in tokens and i - tokens[token] > 1:
                rule1 = True
            if token not in tokens:
                tokens[token] = i
            if i < len(line) - 2 and line[i] == line[i+2]:
                rule2 = True
        if rule1 and rule2:
            self.nice += 1
    def after(self):
        print self.nice

DayProcessor().run()
