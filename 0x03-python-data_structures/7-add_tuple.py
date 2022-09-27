#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in range(3):
        if len(tuple_a) < i:
            tuple_a = *tuple_a, 0
        if len(tuple_b) < i:
            tuple_b = *tuple_b, 0
    elem1 = tuple_a[0] + tuple_b[0]
    elem2 = tuple_a[1] + tuple_b[1]
    return (elem1, elem2)
