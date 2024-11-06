#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Backtrack function to find solution.
    """
    if r == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(n):
        # Skip this column if it’s under attack by any previously placed queens
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        # Place the queen
        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        # Move to the next row
        backtrack(r + 1, n, cols, pos, neg, board)

        # Backtrack: Remove the queen and update the sets
        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solve the N-Queens problem.
    Args:
        n (int): The number of queens. Must be >= 4.
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    # Start the backtracking process from row 0
    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
