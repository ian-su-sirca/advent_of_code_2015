#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *
from itertools import combinations

class DayProcessor(Processor):
    def before(self):
        self.containers = []
        pass
    def process_line(self, line):
        self.containers.append(int(line))
        pass
    def after(self):
        num = 0
        for n in xrange(len(self.containers)):
            for c in combinations(self.containers, n):
                s = sum(c)
                if s == 150:
                    num+=1
                    print len(c), s, c
            if num > 0:
                break
        print num
        pass

DayProcessor().run()
