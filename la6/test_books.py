# -*- coding: utf-8

# LAB 6 #

#   Viktor Palm     André Palmborg
#   vikpa137        andpa149

from books import db
from match import match, search
if __name__ == "__main__":
    print("Testing match() and search()")

    tests = [
                [
                    [['författare',['john','&']], '--', ['titel',['data','--']], '--'], 
                    db,
                    [[['författare', ['john', 'zelle']], ['titel', ['data','structures', 'and', 'algorithms', 'using', 'python', 'and', 'c++']], ['år',2009]]]
                ],
                [
                    ['--', ['författare',['%','Palmborg'], '--']],
                    db,
                    []
                ],
                [
                    ['--', ['titel', ['&', '&']], '--'],
                    db,
                    [[['författare', ['armen', 'asratian']], ['titel', ['diskret', 'matematik']], ['år', 2012]]]
                ]
            ]
    try:
        for test in tests:
            assert (search(test[0], test[1]) == test[2]) is True
        print("search() and match() passes all tests")
    except:
        print("search() or match() has failed")
