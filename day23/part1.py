#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *

class DayProcessor(Processor):
    def before(self):
        self.a = 0
        self.b = 0
        self.op_pointer = 0
        self.code = []
        pass

    def execute(self):
        print 'a', self.a
        print 'b', self.b
        print 'p', self.op_pointer
        if self.op_pointer < 0 or self.op_pointer >= len(self.code):
            print 'OUT OF RANGE'
            return False
        opcode, operands = self.code[self.op_pointer]
        print 'op', opcode
        print 'operand', operands
        if opcode == 'hlf':
            if operands[0] == 'a':
                self.a = int(self.a / 2)
            else:
                self.b = int(self.b / 2)
            self.op_pointer += 1
            return True
        elif opcode == 'tpl':
            if operands[0] == 'a':
                self.a = self.a * 3
            else:
                self.b = self.b * 3
            self.op_pointer += 1
            return True
        elif opcode == 'inc':
            if operands[0] == 'a':
                self.a = self.a + 1
            else:
                self.b = self.b + 1
            self.op_pointer += 1
            return True
        elif opcode == 'jmp':
            self.op_pointer += int(operands[0])
            return True
        elif opcode == 'jie':
            do_jmp = False
            if operands[0] == 'a':
                do_jmp = self.a % 2 == 0
            else:
                do_jmp = self.b % 2 == 0
            if do_jmp:
                self.op_pointer += int(operands[1])
            else:
                self.op_pointer += 1
            return True
        elif opcode == 'jio':
            do_jmp = False
            if operands[0] == 'a':
                do_jmp = self.a == 1
            else:
                do_jmp = self.b == 1
            if do_jmp:
                self.op_pointer += int(operands[1])
            else:
                self.op_pointer += 1
            return True
        return False

    def process_line(self, line):
        opcode, operands = line.split(' ', 1)
        ops = [o.strip() for o in operands.split(',')]
        self.code.append((opcode, ops))
        pass
    def after(self):
        while self.execute():
            pass
        print 'a', self.a
        print 'b', self.b

DayProcessor().run()
