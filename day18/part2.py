#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *
import copy

class DayProcessor(Processor):
    def before(self):
        self.rows = []
        pass

    def is_on(self, row, col):
        if row < 0 or col < 0:
            return 0
        if row >= len(self.rows):
            return 0
        row_data = self.rows[row]
        if col >= len(row_data):
            return 0
        return row_data[col]

    def neighbors_on(self, row, col):
        return sum([
                self.is_on(row-1, col-1),
                self.is_on(row-1, col),
                self.is_on(row-1, col+1),
                self.is_on(row, col-1),
                self.is_on(row, col+1),
                self.is_on(row+1, col-1),
                self.is_on(row+1, col),
                self.is_on(row+1, col+1)])

    def tick(self):
        new_state = copy.deepcopy(self.rows)
        for row in range(100):
            for col in range(100):
                n = self.neighbors_on(row, col)
                if self.is_on(row, col):
                    if n == 2 or n == 3:
                        new_state[row][col] = 1
                    else:
                        new_state[row][col] = 0
                else:
                    if n == 3:
                        new_state[row][col] = 1
                    else:
                        new_state[row][col] = 0
        new_state[0][0] = 1
        new_state[0][99] = 1
        new_state[99][0] = 1
        new_state[99][99] = 1
        self.rows = new_state

    def process_line(self, line):
        row = [ 1 if c == '#' else 0 for c in line ]
        self.rows.append(row)
        pass
    def after(self):
        for i in range(100):
            self.tick()
        print sum([ sum(row) for row in self.rows ])
        pass

DayProcessor().run()
