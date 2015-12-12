#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *
from itertools import permutations

class DayProcessor(Processor):
    def before(self):
        self.locations = set()
        self.distances = {}
        pass
    def process_line(self, line):
        (loc0, _, loc1, _, dist) = line.split(' ')
        self.locations.add(loc0);
        self.locations.add(loc1);
        if loc0 not in self.distances:
            self.distances[loc0] = {}
        self.distances[loc0][loc1] = int(dist)
        if loc1 not in self.distances:
            self.distances[loc1] = {}
        self.distances[loc1][loc0] = int(dist)
        pass

    def calc_dist(self, order):
        path = ' -> '.join(order)
        l = list(order)
        src = l.pop()
        d = 0
        while len(l) > 0:
            dest = l.pop()
            dd = self.distances[src][dest]
            #print '%s->%s %d' % (src, dest, dd)
            d += dd
            src = dest
        print d, path

    def after(self):
        for p in permutations(self.locations):
            self.calc_dist(p)
        pass

DayProcessor().run()
