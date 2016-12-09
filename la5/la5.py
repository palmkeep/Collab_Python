#!/usr/bin/env python
# -*- coding: utf-8

# LAB 5 #

#   Viktor Palm     André Palmborg
#   vikpa137        andpa149

# Lab 6 will be written entirely in english, most of the docstrings in this
# where stil in swedish.

# -----
# Komplettering 3
# -----
from calc import *
from copy import deepcopy



def eval_statements(statements, table):
    """
    Kör alla statements i den ordning de sats in i den inmatade listan
    """
    if isstatements(statements):
        for statement in statements:
            table = eval_statement(statement, deepcopy(table))
    return table


def eval_statement(statement, table):
    """
    Ser till att rätt funktion används på ett statement.
    """
    if isassignment(statement):
        table = eval_assignment(statement, deepcopy(table))

    elif isrepetition(statement):
        table = eval_repetition(statement, deepcopy(table))

    elif isselection(statement):
        table = eval_selection(statement, deepcopy(table))

    elif isoutput(statement):
        eval_output(statement, table)

    elif isinput(statement):
        table = eval_input(statement, deepcopy(table))

    else:
        raise SyntaxError(statement, 'not a statement')

    return table



def eval_expression(exp, table):
    """
    Ser till att rätt funktion används på ett expression. 
    """
    if isbinary(exp):
        return eval_binary(exp, table)
    elif iscondition(exp):
        return eval_condition(exp, table)
    elif isvariable(exp):
        return eval_variable(exp, table)
    elif isconstant(exp):
        return exp
    else:
        raise SyntaxError(exp, 'not an expression')


def eval_output(exp, table):
    """
    Skriver ut en variabel i terminalen.
    """
    variable = output_variable(exp)
    value = eval_expression(variable, deepcopy(table))
    print(str(variable) + " = " + str(value))

def eval_input(input_statement, table):
    """
    Läser in ett värde från tangentbordet.
    """
    var = input_variable(input_statement)
    table[var] = int(input('Enter value for ' + var + ': '))
    return table

def eval_variable(var, table):
    """
    Returnerar värdet på en variabel.
    """
    if var in table:
        return table[var]
    else:
        raise IOError(var, 'is not defined')

def eval_binary(binary_statement, table):
    """
    Evaluerar och returnerar ett uttryck med en binär operator.
    """
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
    else:
        raise IOError(operator, 'not a binary operator')

def eval_assignment(assignment, table):
    """
    Sätter, skapar och sparar variabler i $table och ger dem ett värde.
    """
    var = assignment_variable(assignment)
    exp = eval_expression(assignment_expression(assignment), table)
    table[var] = exp
    return table

def eval_repetition(repetition, table):
    """
    Evaluerar och kör en 'while'-loop.
    """
    cond = repetition_condition(repetition)
    statements = repetition_statements(repetition)
    while eval_condition(cond, table):
        table = eval_statements(statements, deepcopy(table))
    return table

def eval_condition(condition, table):
    """
    Evaluerar och returnerar resultatet av en jämförelse-sats.
    """
    left_cond = eval_expression(condition_left(condition), table)
    right_cond = eval_expression(condition_right(condition), table)
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

# -----
# Komplettering 5
# -----
def eval_selection(selection, table):
    """
    Evaluerar och kör olika statement-satser beroende på en jämförelse-sats.
    """
    if eval_condition(selection_condition(selection), table):
        table = eval_statement(selection_true(selection), deepcopy(table))
    elif hasfalse(selection):
        table = eval_statement(selection_false(selection), deepcopy(table))
    return table



def eval_program(calc, input_table={}):
    """
    Evaluerar och kör kod skriven i "calc-språket". Resulterande variabler
    sparas i en dictionary som eval_program() returnerar.
    """
    # -----
    # TODO: Komplettering 1 och 2
    # -----
    
    table = deepcopy(input_table)

    if isprogram(calc):
        return eval_statements(program_statements(calc), deepcopy(table))
    else:
        raise IOError("Invalid input")
