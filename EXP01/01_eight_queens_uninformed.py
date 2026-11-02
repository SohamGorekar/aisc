N = 8
def is_safe(board, row, col):
    # check column and both diagonals against queens already placed
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True
def solve(board, row):
    if row == N:
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve(board, row + 1):
                return True
            board[row] = -1
    return False
board = [-1] * N
if solve(board, 0):
    print("One valid solution of the 8-Queen problem")
    print("Queen positions (row, col):", [(r, board[r]) for r in range(N)])
    print()
    for r in range(N):
        print(" ".join("Q" if board[r] == c else "." for c in range(N)))
else:
    print("No solution exists")
