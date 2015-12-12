#!/usr/bin/env python
with open('input.txt') as f:
    floor = 0
    for line in f:
        for char in line:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
    print floor
