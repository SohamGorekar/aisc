# ------------------------------------------------------------
# Program : N-Queen Problem using A* Search Algorithm
# Example : 4-Queen Problem
# ------------------------------------------------------------

import heapq

# ------------------------------------------------------------
# Node Class
# ------------------------------------------------------------
class Node:

    def __init__(self, board, row):
        self.board = board      # Queen positions
        self.row = row          # Number of queens placed

        # Cost from start
        self.g = row

        # Heuristic value
        self.h = self.heuristic()

        # Evaluation function
        self.f = self.g + self.h

    # --------------------------------------------------------
    # Heuristic Function
    # Counts attacking queen pairs
    # --------------------------------------------------------
    def heuristic(self):

        attacks = 0

        for i in range(len(self.board)):

            if self.board[i] == -1:
                continue

            for j in range(i + 1, len(self.board)):

                if self.board[j] == -1:
                    continue

                # Same column
                if self.board[i] == self.board[j]:
                    attacks += 1

                # Same diagonal
                elif abs(i - j) == abs(self.board[i] - self.board[j]):
                    attacks += 1

        return attacks

    # Priority Queue comparison
    def __lt__(self, other):
        return self.f < other.f


# ------------------------------------------------------------
# Generate Child Nodes
# ------------------------------------------------------------
def generate_children(node, N):

    children = []

    # All queens placed
    if node.row == N:
        return children

    # Try placing queen in every column
    for col in range(N):

        new_board = node.board[:]
        new_board[node.row] = col

        child = Node(new_board, node.row + 1)

        children.append(child)

    return children


# ------------------------------------------------------------
# Print Chess Board
# ------------------------------------------------------------
def print_board(board):

    N = len(board)

    for row in range(N):

        for col in range(N):

            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()


# ------------------------------------------------------------
# A* Search Algorithm
# ------------------------------------------------------------
def astar_nqueen(N):

    # Initial board
    initial_board = [-1] * N

    open_list = []

    start = Node(initial_board, 0)

    heapq.heappush(open_list, start)

    while open_list:

        current = heapq.heappop(open_list)

        # Goal Test
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

        # Expand node
        children = generate_children(current, N)

        for child in children:

            heapq.heappush(open_list, child)

    print("No Solution Found")


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

N = 4

print("Solving", N, "- Queen Problem using A* Search\n")

astar_nqueen(N)