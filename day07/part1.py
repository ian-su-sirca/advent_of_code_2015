#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *

class DayProcessor(Processor):
    def before(self):
        self.wires = {}
        self.evaluated = {}

    def process_line(self, line):
        tokens = line.split(' ')
        expr = tokens[0:-2]
        wire = tokens[-1]
        self.wires[wire] = expr

    def evaluate(self, expr):
        if not isinstance(expr, list):
            expr = [expr]
        #print 'EVALUATING', ' '.join(expr)
        if len(expr) == 1:
            # number or wire
            try:
                return int(expr[0])
            except:
                # wire, evaluate the wire expr
                wire = expr[0]

                # check cache first
                if wire in self.evaluated:
                    #print 'EVALUATED [cache]', wire, self.evaluated[wire]
                    return self.evaluated[wire]

                # if not, calculate it
                wire_expr = self.wires[wire]
                wire_result = self.evaluate(wire_expr)

                # save the cache
                self.evaluated[wire] = wire_result
                #print 'EVALUATED', wire, wire_result
                return wire_result

        elif len(expr) == 2:
            # NOT
            assert expr[0] == 'NOT'
            return ~ self.evaluate(expr[1])
        elif len(expr) == 3:
            op = expr[1]
            if op == 'AND':
                return self.evaluate(expr[0]) & self.evaluate(expr[2])
            elif op == 'OR':
                return self.evaluate(expr[0]) | self.evaluate(expr[2])
            elif op == 'LSHIFT':
                return self.evaluate(expr[0]) <<  self.evaluate(expr[2])
            elif op == 'RSHIFT':
                return self.evaluate(expr[0]) >> self.evaluate(expr[2])
        raise ValueError(expr)

    def after(self):
        print self.evaluate('a') % 65536

DayProcessor().run()
