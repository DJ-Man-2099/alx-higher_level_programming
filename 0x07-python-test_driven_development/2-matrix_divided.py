#!/usr/bin/python3
"""
Module for second task
Using Tests to check task if successful

"""


def matrix_divided(matrix, div):
    """
    This Function divides all elements of a matrix

    params: matrix
            div
    """
    if check_if_is_not_number(div):
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or\
        not len(matrix) or\
        any(type(row) is not list for row in matrix) or\
        any(check_if_is_not_number(i) for row in matrix for i in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    
    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            new_i = round(i/div, 2)
            new_row.append(new_i)
        new_matrix.append(new_row)
    return new_matrix


def check_if_is_not_number(i):
    """
    checks if number isn't int or float

    params: i
    """
    return type(i) is not int and type(i) is not float
