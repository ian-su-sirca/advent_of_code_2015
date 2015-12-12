#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *

def string_to_num(s):
    num = 0
    for c in s:
        charval = ord(c) - ord('a')
        num = num * 26 + charval
    return num

def num_to_string(n):
    s = ''
    while n >= 26:
        charval = n % 26
        s = chr(charval + ord('a')) + s
        n = int(n / 26)
    s = chr(n + ord('a')) + s
    return s

def is_valid(s):
    rule1 = False
    # rule 2
    for c in 'iol':
        if c in s:
            return False
    pairs = {}
    for i in range(len(s)):
        if i < len(s) - 2:
            if ord(s[i]) + 1 == ord(s[i+1]) and ord(s[i+1]) + 1 == ord(s[i+2]):
                rule1 = True
        if i < len(s) - 1:
            if s[i] == s[i+1]:
                pairs[s[i]] = i
    return rule1 and len(pairs.keys()) > 1

class DayProcessor(Processor):
    def before(self):
        pass
    def process_line(self, line):
        n = string_to_num(line)
        while not is_valid(num_to_string(n)):
            n += 1
        print num_to_string(n)
        n += 1
        while not is_valid(num_to_string(n)):
            n += 1
        print num_to_string(n)

    def after(self):
        pass

DayProcessor().run()
