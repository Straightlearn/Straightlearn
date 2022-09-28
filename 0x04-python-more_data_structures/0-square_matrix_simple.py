#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[row ** 2 for row in col] for col in matrix]
