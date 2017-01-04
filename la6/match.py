# -*- coding: utf-8

# LAB 6 #

#   Viktor Palm     André Palmborg
#   vikpa137        andpa149



def match(pattern, seq):
    """
    Returns whether a given sequence matches the given pattern
    """
    if not pattern:
        #if end of the pattern check if end of seq return true else false
        return not seq
    elif pattern[0] == '--':
        #if wildcard return true if either the rest of the patter matches the seq or the rest of the seq matches the pattern
        if match(pattern[1:], seq):
            return True
        elif not seq:
            return False
        else:
            return match(pattern, seq[1:])
    elif not seq:
        # if the sequence end before the patter ends then return false
        return False 
    elif isinstance(pattern[0], list) and isinstance(seq[0], list):
        # if there are sub patterns check wheter those match sub seq
        return match(pattern[0], seq[0]) and match(pattern[1:], seq[1:])
    elif pattern[0] == '&':
        #if & then skip this part of the pattern
        return match(pattern[1:], seq[1:])
    elif seq[0] == pattern[0]:
        #if both first elements match then continue matching
        return match(pattern[1:], seq[1:])
    else:
        return False


def search(pattern, seq):
    """
    Returns all book-entries in $seq that match $pattern
    """
    #if a book matches the patternm ad it to the final result and check next book else dont, if you are out of books then stop matching.
    if not seq:
        return []
    elif match(pattern, seq[0]):
        return [seq[0]] + search(pattern, seq[1:])
    else:
        return [] + search(pattern, seq[1:])



