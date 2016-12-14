# -*- coding: utf-8

# LAB 6 #

#   Viktor Palm     André Palmborg
#   vikpa137        andpa149



def quicksort(seq):
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
