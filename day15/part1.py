#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *
from itertools import combinations_with_replacement

class Ingredient(object):
    def __init__(self, name, attribs):
        self.name = name
        self.mods = {}
        for attrib in attribs.split(','):
            attrib = attrib.strip()
            (k, v) = attrib.split(' ')
            self.mods[k] = int(v)
        print self.name, self.mods

class DayProcessor(Processor):
    def before(self):
        self.ingredients = []
        pass
    def process_line(self, line):
        (thing, attribs) = line.split(':')
        i = Ingredient(thing, attribs)
        self.ingredients.append(i)
        pass
    def after(self):
        for combo in combinations_with_replacement(self.ingredients, 100):
            attribs = {}
            for c in combo:
                for k in c.mods:
                    if k not in attribs:
                        attribs[k] = c.mods[k]
                    else:
                        attribs[k] += c.mods[k]
            score = 1
            for k in attribs:
                if k == 'calories':
                    # ignore calories
                    continue
                if attribs[k] < 0:
                    score = 0
                    break
                else:
                    score *= attribs[k]
            print score, attribs

DayProcessor().run()
