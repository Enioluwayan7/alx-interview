#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Arguments:
    grid -- a list of list of integers where:
            0 represents water
            1 represents land

    Returns:
    int -- the perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell (up)
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

                # Subtract 2 for each adjacent land cell (left)
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
