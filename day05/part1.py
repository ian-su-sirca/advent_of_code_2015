#!/usr/bin/env python
from common import *

class DayProcessor(Processor):
    def before(self):
        self.nice = 0
        pass
    def process_line(self, line):
        naughty_pairs = [ 'ab', 'cd', 'pq', 'xy' ]
        for pair in naughty_pairs:
            if pair in line:
                return
        last_char = ''
        found_pair = False
        num_vowels = 0
        for char in line:
            if last_char == char:
                found_pair = True
            if char in 'aeiou':
                num_vowels += 1
            last_char = char
        if found_pair and num_vowels >= 3:
            self.nice += 1
        pass
    def after(self):
        print self.nice

DayProcessor().run()
