import sys

def print_solutions(board):
    """Prints the board configuration as required."""
    print([[i, board[i]] for i in range(len(board))])

def is_safe(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(n, row, board, solutions):
    """Uses backtracking to solve the N Queens problem."""
    if row == n:
        print_solutions(board)
        solutions.append(board[:])
    else:
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve_n_queens(n, row + 1, board, solutions)
                board[row] = -1

def main():
    """Main function to check input and initiate the solving process."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_n_queens(n, 0, board, solutions)

if __name__ == "__main__":
    main()
