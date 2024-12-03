def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    :param grid: List of list of integers, where 0 represents water and 1 represents land.
    :return: Perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with 4 sides
                perimeter += 4

                # Check if there is land above
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Remove 2 for shared edge

                # Check if there is land to the left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Remove 2 for shared edge

    return perimeter
