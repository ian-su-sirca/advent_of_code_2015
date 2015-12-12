#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *

def look_and_say(s):
    look_and_say = ''
    last = None
    num = 1
    for c in s:
        if c == last:
            num += 1
        elif last is not None:
            look_and_say += '%d%s' % (num, last)
            num = 1
            last = c
        else:
            last = c
    look_and_say += '%d%s' % (num, last)
    return look_and_say

class DayProcessor(Processor):
    def before(self):
        pass
    def process_line(self, line):
        for i in range(40):
            line = look_and_say(line)
        print len(line)
        pass
    def after(self):
        pass

DayProcessor().run()
