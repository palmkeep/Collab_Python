from books import db
from match import search

def test_search(pattern, result):
    res = search(db, pattern)
    assert res is result , "beeeeeeooop"


