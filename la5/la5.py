#!/usr/bin env python
# -*- coding: utf-8

# LAB 5 #

from calc import *

def eval_program(calc, table={}):

    # EVAL_STATEMENT
    def eval_statement(statement):
        if isstatements(statement):
            for stat in statement:
                eval_statement(stat)

        elif isassignment(statement):
            eval_assignment(statement)

        elif isrepetition(statement):
            eval_condition(statement)

        elif isselection(statement):
            eval_selection(statement)

        elif isoutput(statement):
            output(statement)



    # EVAL_EXPRESSION
    def eval_expression(exp):
        if isbinary(exp):
            return eval_binary(exp)
        elif iscondition(exp):
            return eval_condition(exp)
        elif isvariable(exp):
            return eval_variable(exp)
        elif isconstant(exp):
            return exp




    # HELP FUNCTION
    def output(output_statement):
        print(eval_program(output_variable(output_statement), table))

    def eval_variable(var):
        if var in table:
            return table[var]
        else:
            return var

    def eval_binary(binary_statement):
        left_var = eval_expression(binary_left(binary_statement), table)
        right_var = eval_expression(binary_right(binary_statement), table)
        operator = binary_operator(binary_statement)

        if operator == '+':
            return left_var + right_var 
        elif operator == '-':
            return left_var - right_var
        elif operator == '*':
            return left_var * right_var
        elif operator == '/':
            return left_var / right_var

    def eval_condition(condition_statement):
        left_cond = eval_expression(condition_left(condition_statement), table)
        right_cond = eval_expressionp(condition_right(condition_statement),table)
        cond = condition_operator(condition_statement)

        if cond == '<':
            if left_cond < right_cond:
                return True
            else:
                return False
        elif cond == '>':
            if left_cond > right_cond:
                return True
            else:
                return False
        elif cond == '=':
            if left_cond == right_cond:
                return True
            else:
                return False

 

    # START: EVAL_PROGRAM
    if isprogram(calc):
        eval_statement(program_statements(calc))
        return table
    else:
        raise IOError("Invalid input")




