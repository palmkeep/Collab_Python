# -*- coding: utf-8

# LAB 6 #

#   Viktor Palm     André Palmborg
#   vikpa137        andpa149



def match(pattern, seq):
    """
    Returns whether a given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    elif pattern[0] == '--':
        if match(pattern[1:], seq):
            return True
        elif not seq:
            return False
        else:
            return match(pattern, seq[1:])
    elif not seq:
        return False 
    elif isinstance(pattern[0], list) and isinstance(seq[0], list):
        return match(pattern[0], seq[0]) and match(pattern[1:], seq[1:])
    elif pattern[0] == '&':
        return match(pattern[1:], seq[1:])
    elif seq[0] == pattern[0]:
        return match(pattern[1:], seq[1:])
    else:
        return False


def search(pattern, seq):
    """
    Returns all book-entries in $seq that match $pattern
    """
    if not seq:
        return []
    elif match(pattern, seq[0]):
        return [seq[0]] + search(pattern, seq[1:])
    else:
        return [] + search(pattern, seq[1:])



