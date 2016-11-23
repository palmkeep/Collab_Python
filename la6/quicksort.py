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
