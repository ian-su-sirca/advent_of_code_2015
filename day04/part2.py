#!/usr/bin/env python
from common import *
import md5

class DayProcessor(Processor):
    def before(self):
        pass
    def process_line(self, line):
        n = 0
        while True:
            k = '%s%d' % (line, n)
            h = md5.md5(k).hexdigest()
            if h[:6] == '000000':
                print k, h, n
                return
            n += 1
        pass
    def after(self):
        pass

DayProcessor().run()
