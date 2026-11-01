print("8-QUEENS PROBLEM USING BACKTRACKING")

N = 8

# Create an 8x8 chessboard
board = [[0 for i in range(N)] for j in range(N)]

# Check whether a queen can be placed safely
def is_safe(row, col):

    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Backtracking function
def solve(row):

    # All 8 queens are placed
    if row == N:
        return True

    # Try each column in the current row
    for col in range(N):

        if is_safe(row, col):

            print("Placing Queen at Row", row, "Column", col)

            board[row][col] = 1

            if solve(row + 1):
                return True

            # Backtrack if placement does not lead to a solution
            print("Backtracking from Row", row, "Column", col)
            board[row][col] = 0

    return False


# Place the first queen at (0, 0)
board[0][0] = 1

print("\nFirst Queen placed at Row 0, Column 0")

# Start placing the remaining queens
if solve(1):

    print("\nFinal 8-Queens Matrix:\n")

    for row in board:
        print(row)

else:
    print("No solution exists.")