#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *

import re

class DayProcessor(Processor):
    def before(self):
        self.code_len = 0
        self.mem_len = 0
    def process_line(self, line):
        orig = line
        self.code_len += len(line)
        line = line.replace('\\\\', 'S')
        line = re.sub(r'\\x[0-9a-f][0-9a-f]', 'R', line)
        line = line.replace('\\"', 'Q')
        self.mem_len += len(line) - 2
    def after(self):
        print self.code_len - self.mem_len

DayProcessor().run()
