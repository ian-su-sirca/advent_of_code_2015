#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *

class DayProcessor(Processor):
    def before(self):
        self.data = {
                'children': 3,
                'cats': 7,
                'samoyeds': 2,
                'pomeranians': 3,
                'akitas': 0,
                'vizslas': 0,
                'goldfish': 5,
                'trees': 3,
                'cars': 2,
                'perfumes': 1
        }
        pass
    def process_line(self, line):
        (sue, things) = line.split(':', 1)
        ok = True
        suethings = {}
        for thing in things.split(','):
            (k, v) = thing.split(':')
            k = k.strip()
            v = int(v)
            if k in ('cats', 'trees'):
                if self.data[k] >= v:
                    ok = False
            elif k in ('pomeranians', 'goldfish'):
                if self.data[k] <= v:
                    ok = False
            else:
                if self.data[k] != v:
                    ok = False
        if ok:
            print sue, things
        pass
    def after(self):
        pass

DayProcessor().run()
