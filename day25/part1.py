#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *

def diag(row, col):
    r = 1
    c = 1
    n = 0
    while r != row or c != col:
        n += 1
#        print n, r, c 
        if r == 1:
            r = c + 1
            c = 1
        else:
            r -= 1
            c += 1
    return n

def nth_code(n):
    v = 20151125
    for i in xrange(n):
        v = (v * 252533) % 33554393
    return v

class DayProcessor(Processor):
    def before(self):
        self.row = 2978
        self.col = 3083
        pass
    def process_line(self, line):
        pass
    def after(self):
        n = diag(self.row, self.col)
        print n
        print nth_code(n)
        pass

DayProcessor().run()
