#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *
import json

class DayProcessor(Processor):
    def before(self):
        self.num = 0

    def proc_data(self, data):
        if isinstance(data, dict):
            for k in data:
                self.proc_data(data[k])
        elif isinstance(data, list):
            for v in data:
                self.proc_data(v)
        else:
            try:
                self.num += int(data)
            except:
                pass

    def process_line(self, line):
        j = json.loads(line)
        self.proc_data(j)
    def after(self):
        print self.num

DayProcessor().run()
