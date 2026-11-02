import heapq


class Node:

    def __init__(self, board, row):
        self.board = board
        self.row = row

        self.g = row

        self.h = self.heuristic()

        self.f = self.g + self.h

    def heuristic(self):

        attacks = 0

        for i in range(len(self.board)):

            if self.board[i] == -1:
                continue

            for j in range(i + 1, len(self.board)):

                if self.board[j] == -1:
                    continue

                if self.board[i] == self.board[j]:
                    attacks += 1

                elif abs(i - j) == abs(self.board[i] - self.board[j]):
                    attacks += 1

        return attacks

    def __lt__(self, other):
        return self.f < other.f


def generate_children(node, N):

    children = []

    if node.row == N:
        return children

    for col in range(N):

        new_board = node.board[:]
        new_board[node.row] = col

        child = Node(new_board, node.row + 1)

        children.append(child)

    return children


def print_board(board):

    N = len(board)

    for row in range(N):

        for col in range(N):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


def astar_nqueen(N):

    initial_board = [-1] * N

    open_list = []

    start = Node(initial_board, 0)

    heapq.heappush(open_list, start)

    while open_list:

        current = heapq.heappop(open_list)

        if current.row == N and current.h == 0:

            print("\nSolution Found!\n")

            print("Board Representation:")

            print(current.board)

            print("\nChess Board:\n")

            print_board(current.board)

            print("\ng =", current.g)
            print("h =", current.h)
            print("f =", current.f)

            return

        children = generate_children(current, N)

        for child in children:

            heapq.heappush(open_list, child)

    print("No Solution Found")


N = int(input("Enter the number of queens: "))

if N < 1:
    raise SystemExit("The number of queens must be at least 1.")

print("Solving", N, "- Queen Problem using A* Search\n")

astar_nqueen(N)
