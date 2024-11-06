# n queens

def is_safe(board, row, col, n):
    # Check if it's safe to place a queen at board[row][col]
    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve(col):
        if col == n:
            solution = ["".join("1" if cell == 1 else "." for cell in row) for row in board]
            solutions.append(solution)
            return
        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(col + 1)
                board[row][col] = 0

    solve(0)
    return solutions

# Example usage for N-Queens with N=4
n = 4
solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()
