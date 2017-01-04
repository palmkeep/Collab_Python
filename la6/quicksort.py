# -*- coding: utf-8

# LAB 6 #

#   Viktor Palm     André Palmborg
#   vikpa137        andpa149


"""
quicksort() sorts a list by splitting a list of numbers into three 
lists: the first element, all elements smaller than the first element and
all elements equal to or greater than the first element. quicksort() is then
called again to sort the two lists that were created and this process is
repeated until quicksort() is being called upon empty lists.

"""

def quicksort(seq):
    """
    Sorts $seq in ascending order. Returns a new sorted list.
    """
    if not seq:
        return []

    a = []
    b = []
    for elem in seq[1:]:
        if elem < seq[0]:
            a.append(elem)
        else:
            b.append(elem)

    return quicksort(a) + [seq[0]] + quicksort(b)
