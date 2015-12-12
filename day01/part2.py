#!/usr/bin/env python
import sys
with open('input.txt') as f:
    floor = 0
    pos = 0
    for line in f:
        for char in line:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            pos += 1
            if floor == -1:
                print pos
                sys.exit(0)
