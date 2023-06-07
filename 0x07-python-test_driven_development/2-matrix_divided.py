#!/usr/bin/python3
'''
A function that devides all elements of a matrix.
'''


def matrix_divided(matrix, divisor):
    if not isinstance(matrix, list) or not all(isinstance(row, list)
            for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if not isinstance(divisor, (int, float)):
        raise TypeError("divisor must be a number")

    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if len(row) != row_size:
            raise ValueError("each row of the matrix must have the same size")

        new_row = [round(element / divisor, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
