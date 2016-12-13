from calendar_ADT import *

if __name__ == "__main__":
    h = new_hour(int(input("h: ")))
    m = new_minute(int(input("m: ")))
    a = new_time(h,m)
    print('a', a)

    h = new_hour(int(input("h: ")))
    m = new_minute(int(input("m: ")))
    b = new_time(h,m)
    print('b', b)

    q = new_time_span(a, b)
    print('q', q)

    h = new_hour(int(input("h: ")))
    m = new_minute(int(input("m: ")))
    a = new_time(h,m)
    print('a', a)

    h = new_hour(int(input("h: ")))
    m = new_minute(int(input("m: ")))
    b = new_time(h,m)
    print('b', b)

    w = new_time_span(a, b)
    print('w', w)

    print(overlap(q,w))
