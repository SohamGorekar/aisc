N = 8

board = [["." for i in range(N)] for j in range(N)]


def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == "Q":
            return False

    i = row
    j = col

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i = row
    j = col

    while i < N and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True


def solve(board, col):
    if col >= N:
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = "Q"

            if solve(board, col + 1):
                return True

            board[row][col] = "."

    return False


if solve(board, 0):
    print("Solution Found:\n")

    for row in board:
        print(" ".join(row))
else:
    print("No Solution Exists")
