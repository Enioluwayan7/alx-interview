#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a square matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of lists): A 2D square matrix of integers.

    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
