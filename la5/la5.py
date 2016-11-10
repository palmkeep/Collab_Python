#!/usr/bin env python
# -*- coding: utf-8

# LAB 5 #

from calc import *

def eval_program(calc, table={}):
    def output(calc):
        print(eval_program(output_variable(calc), table))

    def get_variable(var):
        if var in table:
            return table[var]
        else:
            return var

    print('calc', calc)
    if isprogram(calc):
        for statement in calc[1:]:
            table = eval_program(statement, table)
    elif isstatements(calc):
        pass
    elif isassignment(calc):
        pass
    elif isrepetition(calc):
        pass
    elif isselection(calc):
        pass
    elif isoutput(calc):
        output(calc)
    elif isinput(calc):
        pass
    elif isvariable(calc):
        return get_variable(calc)

