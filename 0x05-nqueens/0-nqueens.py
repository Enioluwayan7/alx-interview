#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    """Check if a queen can be placed at board[row] = col."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, row=0, board=None, solutions=None):
    """Recursive backtracking to find all solutions for N queens problem."""
    if solutions is None:
        solutions = []
    if board is None:
        board = [-1] * N
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return solutions
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1
    return solutions

def main():
    """Main function to parse input and print solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
