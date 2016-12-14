# -*- coding: utf-8

# LAB 6 #

#   Viktor Palm     André Palmborg
#   vikpa137        andpa149



import randrange
from quicksort import quicksort



def check_sorted(seq):
    if not seq or len(seq) == 1:
        return True
    elif seq[0] <= seq[1]:
        return check_sorted(seq[1:])
    else:
        return False

if __name__ == "__main__":
    print("________________________________________")
    print("| Checking the quicksort() function    |")
    print("| by passing four random lists         |")
    print("|______________________________________|\n")

    num_tests = 4
    num_int_test_seq = 20
    while num_tests > 0:
        i = num_int_test_seq
        test_seq = []
        sorted_test_seq = []
        while i > 0:
            test_seq.append(randrange(1,100))
            i -= 1
        sorted_test_seq = quicksort(test_seq)

        print(test_seq)
        print(sorted_test_seq)

        assert check_sorted(sorted_test_seq) is True

        print("\n")
        num_tests -= 1

    print("________________________________________")
    print("| quicksort() passes all four tests    |")
    print("|______________________________________|")
