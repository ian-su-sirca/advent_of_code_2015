#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *
import json

class DayProcessor(Processor):
    def before(self):
        pass

    def eval_data(self, data):
        if isinstance(data, dict):
            try:
                return sum([self.eval_data(data[k]) for k in data])
            except ValueError:
                return 0
        elif isinstance(data, list):
            val = 0
            for v in data:
                try:
                    val += self.eval_data(v)
                except:
                    pass
            return val
        else:
            if data == 'red':
                raise ValueError('red')
            try:
                return int(data)
            except:
                return 0

    def process_line(self, line):
        j = json.loads(line)
        print self.eval_data(j)

    def after(self):
        pass
DayProcessor().run()
