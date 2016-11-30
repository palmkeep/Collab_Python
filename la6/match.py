# -*- coding: utf-8


def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False 
    elif isinstance(pattern[0], list) and isinstance(seq[0], list):
        return match(seq[0], pattern[0]) and match(seq[1:], pattern[1:])
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    else:
        return False

def search(seq, pattern):
    if not seq:
        return None
    elif match(seq[0], pattern):
        print(seq[0])
    return search(seq[1:], pattern)


#def et_impera(seq, pivot):
#    if seq[0] < pivot:
#        return 
#    else:
#        return 

    
    
