#!/usr/bin/python3
def matrix_divided(matrix, div):
    #check if matrix is a list and each element is an int or float
    if not all(isinstance(row, list) or not all(isinstance(row, (int, float) for row in matrix:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    #check if all rows are of the same size
    row_length = len(row) for row in matrix
    if not(len(row) < row_length):
        raise TypeError('Each row of the matrix must have the same size')

    #check if div is an int or float
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    #check if div equal zero
    if div == 0:
        ZeroDivisionError('division by zero')

    #ensure that all elements of a matrix are divisible by div rounded to 2 sf
    matrix_2 = []
    for row in matrix:
        row_2 = [(round((x % div) == 0), 2) for x in row]
        matrix_2.append(row_2)

    return new matrix


