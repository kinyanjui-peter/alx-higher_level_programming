#!/usr/bin/python3
def pascal_triangle(n):
    """
    Function that prints Pascal's Triangle up to row n.
    """
    triangle = [[1]]
    
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        
        for j in range(1, i):
            new_value = prev_row[j - 1] + prev_row[j]
            new_row.append(new_value)
        
        new_row.append(1)
        triangle.append(new_row)
    
    # Print the Pascal's Triangle
    for row in triangle:
        print(" ".join(map(str, row)).center(n * 3))
