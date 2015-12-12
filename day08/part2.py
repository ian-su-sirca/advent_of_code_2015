#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *

class DayProcessor(Processor):
    def before(self):
        self.orig_len = 0
        self.enc_len = 0
    def process_line(self, line):
        self.orig_len += len(line)
        # replace \ -> \\
        line = line.replace('\\', '\\\\')
        # replace " -> \"
        line = line.replace('\"', '\\\"')
        self.enc_len += len(line) + 2
    def after(self):
        print self.enc_len - self.orig_len

DayProcessor().run()
