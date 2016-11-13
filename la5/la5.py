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
            pass
        elif isselection(statement):
            pass 
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

    def eval_assignment(assignment):
        var = assignment_variable(assignment)
        exp = assignment_expression(assignment)
        print(str(var) + " " + str(exp))
        table[var] = eval_expression(exp)
        
    def eval_selection():
        pass
 

    # START: EVAL_PROGRAM
    if isprogram(calc):
        eval_statement(program_statements(calc))
        return table
    else:
        raise IOError("Invalid input")




