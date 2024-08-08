#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns  list of integers
    represents the Pascal Triangle of n
    returns empty list if n <= 0
    """
    z = []
    if n <= 0:
        return z
    z = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(z[i - 1]) - 1):
            curr = z[i - 1]
            temp.append(z[i - 1][j] + z[i - 1][j + 1])
        temp.append(1)
        z.append(temp)
    return z
