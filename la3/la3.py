#!/usr/bin env python
# -*- coding: utf-8



# LAB 3A #
def split_rec(jumbledString):
    a = ''
    b = ''
    
    if not jumbledString:
        return a, b
    else:
        c = jumbledString[0]
        if c.islower() or c == '.' or c == '_':
            a = c
        elif c.isupper() or c == ' ' or c == '|':
            b = c
        restJumbledString = split_rec(jumbledString[1:])
        return a + restJumbledString[0], b + restJumbledString[1]



def split_it(JumbledString):
    ''' Returnerar de två gömda meddelandena i den inmatade strängen enligt reglerna beskrivna i la3A '''
    StringLower = ''
    StringUpper = ''

    CharList = list(JumbledString)
    for c in JumbledString:
        if c.islower() or c == '.' or c == '_':
            StringLower += c
        elif c.isupper() or c == ' ' or c == '|':
            StringUpper += c

    return StringLower, StringUpper





# LAB 3B #
def interpret(expression, logic_dict):
    '''
    Evaluerar ett booleskt uttryck och returnerar en sträng med 
    sanningsvärdet. Om en dictionary matas in kan godtyckliga 
    strängar evalueras som boolska värden eller uttryck 
    '''
    if isinstance(expression, str):
            if expression in logic_dict:
                return logic_dict[expression]
            if expression == "true":
                return "true"
            else:
                return "false"

    elif isinstance(expression, list):
        if len(expression) == 2:
            if expression[0] == "NOT":
                return op_not(expression[1], logic_dict)
        elif len(expression) == 3:
            if expression[1] == "AND":
                return op_and(expression[0], expression[2], logic_dict)
            elif expression[1] == "OR":
                return op_or(expression[0], expression[2], logic_dict)



def op_not(exp1, logic_dict):
    if interpret(exp1, logic_dict) == "true":
        return "false"
    elif interpret(exp1, logic_dict) == "false":
        return "true"

def op_or(exp1, exp2, logic_dict):
    ''' op_or utför den booleska funktionen 'eller' på två strängar '''
    if interpret(exp1, logic_dict) == "true" or interpret(exp2, logic_dict) == "true":
        return "true"
    else:
        return "false"

def op_and(exp1, exp2, logic_dict):
    ''' op_and utför den booleska funktionen 'och' på två strängar '''
    if interpret(exp1, logic_dict) == "true" and interpret(exp2, logic_dict) == "true":
        return "true"
    else:
        return "false"



# LAB 3C #
boardRow = {}

def reset_board():
    global boardRow
    boardRow = {}
    boardRow.clear()

def isfree(row, column):
    if row in boardRow:
        if column in boardRow[row]:
            return False
        else:
            return True
    else:
        return True


def place_piece(row, column, playerPiece):
    if row in boardRow:
        if column in boardRow[row]:
            return False
        else:
            boardRow[row][column] = playerPiece
            return True
    else:
        boardRow[row] = {}
        boardRow[row][column] = playerPiece
        return True


def get_piece(row, column):
    if not isfree(row, column):
        return boardRow[row][column]
    else:
        return False


def remove_piece(row, column):
    if not isfree(row, column):
        if len(boardRow[row]) == 1:
            del boardRow[row]
            return True
        else:
            del boardRow[row][column]
            return True
    else:
        return False


def move_piece(row, column, newRow, newColumn):
    if not isfree(row, column):
        if isfree(newRow, newColumn):
            place_piece(newRow, newColumn, get_piece(row, column))
            remove_piece(row, column)
            return True
        else:
            return False

def count(rowOrColumn, lineNumber, playerPiece):
    count = 0

    if rowOrColumn == 'column':
        for piece in boardRow[lineNumber]:
            if boardRow[lineNumber][piece] == playerPiece:
                count += 1
    elif rowOrColumn == 'row':
        for row in boardRow:
            if lineNumber in boardRow[row]:
                if boardRow[row][lineNumber] == playerPiece:
                    count += 1

    return count

def nearest_piece(row, column):
    near = [0, 0]
    orig = [row, column]

    for rowNum in boardRow:
        for colNum in boardRow[row]:
            if (row - orig[0])**2 + (column - orig[1])**2 < (near[0] - orig[0])**2 + (near[1] - orig[1])**2:
                near[0] = rowNum
                near[1] = colNum
    if near == [0, 0]:
        return False
    else:
        return near[0], near[1]



