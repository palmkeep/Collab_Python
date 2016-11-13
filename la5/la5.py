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
            eval_repetition(statement)

        elif isselection(statement):
            eval_selection(statement)

        elif isoutput(statement):
            eval_output(statement)
        elif isinput(statement):
            eval_input(statement)



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



    # HELP FUNCTIONS
    def eval_output(expression):
        print(eval_expression(output_variable(statement)))

    def eval_input(input_statement):
        var = input_variable(input_statement)
        table[var] = input()

    def eval_variable(var):
        if var in table:
            return table[var]
        else:
            raise IOError(var, 'is not defined')

    def eval_binary(binary_statement):
        left_var = eval_expression(binary_left(binary_statement))
        right_var = eval_expression(binary_right(binary_statement))
        operator = binary_operator(binary_statement)

        if operator == '+':
            return left_var + right_var 
        elif operator == '-':
            return left_var - right_var
        elif operator == '*':
            return left_var * right_var
        elif operator == '/':
            return left_var / right_var

    def eval_assignment(assignment):
        var = assignment_variable(assignment)
        exp = eval_expression(assignment_expression(assignment))
        table[var] = exp

    def eval_repetition(repetition):
        cond = repetition_condition(repetition)
        statements = repetition_statements(repetition)
        while eval_condition(cond):
            eval_statement(statements)

    def eval_condition(condition):
        left_cond = eval_expression(condition_left(condition))
        right_cond = eval_expression(condition_right(condition))
        cond = condition_operator(condition)

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

    def eval_selection(selection):
        print(1)
 
 

    # START: EVAL_PROGRAM
    if isprogram(calc):
        eval_statement(program_statements(calc))
        return table
    else:
        raise IOError("Invalid input")




