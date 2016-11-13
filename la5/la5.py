#!/usr/bin env python
# -*- coding: utf-8

# LAB 5 #

from calc import *

def eval_program(calc, table={}):


    # EVAL_STATEMENT
    def eval_statement(statement, table)
        elif isstatements(calc):
            eval_program(first_statement(calc), table)
            eval_program(rest_statement(calc), table)
        elif isassignment(calc):
            pass
        elif isrepetition(calc):
            print(repetition_condition(calc))
            while repetition_condition(calc):
                eval_program(repetition_statements(calc), table)
        elif isselection(calc):
            pass 
        elif isoutput(calc):
            output(calc)
        elif isbinary(calc):
            return eval_binary(calc)
        elif iscondition(calc):
            return eval_condition(calc)
        elif isinput(calc):
            pass
        elif isvariable(calc):
            return get_variable(calc)


    # EVAL_EXPRESSION
    def eval_expression(exp, table):
        if isbinary(exp):
            return eval_binary(exp)
        elif iscondition(exp):
            return eval_condition(exp)
        elif isvariable(exp):
            return eval_variable(exp)


    # HELP FUNCTION
    def output(output_statement):
        print(eval_program(output_variable(output_statement), table))

    def eval_variable(var):
        if var in table:
            return table[var]
        else:
            return var

    def eval_binary(binary_statement):
        left_var = eval_program(binary_left(binary_statement), table)
        right_var = eval_program(binary_right(binary_statement), table)
        bin_operator = binary_operator(binary_statement)

        if bin_operator == '+':
            return left_var + right_var 
        elif bin_operator == '-':
            return left_var - right_var
        elif bin_operator == '*':
            return left_var * right_var
        elif bin_operator == '/':
            return left_var / right_var

    def eval_condition(condition_statement):
        left_cond = eval_program(condition_left(condition_statement), table)
        right_cond = eval_program(condition_right(condition_statement),table)
        cond_operator = condition_operator(condition_statement)
 

    # START: EVAL_PROGRAM
    if isprogram(calc):
        for statement in calc[1:]:
            table = eval_program(statement, table)
    else:
        raise IOError("Invalid input")




