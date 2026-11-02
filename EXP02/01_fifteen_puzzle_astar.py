# ------------------------------------------------------------
# Program: 15-Puzzle Problem using A* (A-Star) Search Algorithm
# Heuristic Used: Manhattan Distance
# ------------------------------------------------------------

import heapq

# Goal State
GOAL = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9,10,11,12),
    (13,14,15,0)
)

# Store the goal position of each tile
goal_position = {}
for i in range(4):
    for j in range(4):
        goal_position[GOAL[i][j]] = (i, j)


# ------------------------------------------------------------
# Node Class
# ------------------------------------------------------------
class Node:

    def __init__(self, state, parent=None, move=None, g=0):
        self.state = state          # Current puzzle state
        self.parent = parent        # Parent node
        self.move = move            # Move taken
        self.g = g                  # Cost from start
        self.h = self.heuristic()   # Manhattan Distance
        self.f = self.g + self.h    # Total cost

    # Calculate Manhattan Distance
    def heuristic(self):

        distance = 0

        for i in range(4):
            for j in range(4):

                tile = self.state[i][j]

                if tile != 0:

                    goal_row, goal_col = goal_position[tile]

                    distance += abs(i-goal_row) + abs(j-goal_col)

        return distance

    # Compare nodes according to f(n)
    def __lt__(self, other):
        return self.f < other.f


# ------------------------------------------------------------
# Find Blank Tile
# ------------------------------------------------------------
def find_blank(state):

    for i in range(4):
        for j in range(4):

            if state[i][j] == 0:
                return i, j


# ------------------------------------------------------------
# Generate Child States
# ------------------------------------------------------------
def generate_children(node):

    children = []

    row, col = find_blank(node.state)

    directions = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0,-1, "Left"),
        (0, 1, "Right")
    ]

    for dx, dy, move in directions:

        new_row = row + dx
        new_col = col + dy

        if 0 <= new_row < 4 and 0 <= new_col < 4:

            new_state = [list(r) for r in node.state]

            # Swap blank with neighbouring tile
            new_state[row][col], new_state[new_row][new_col] = \
            new_state[new_row][new_col], new_state[row][col]

            child = Node(
                tuple(tuple(r) for r in new_state),
                parent=node,
                move=move,
                g=node.g + 1
            )

            children.append(child)

    return children


# ------------------------------------------------------------
# Print Solution Path
# ------------------------------------------------------------
def print_solution(node):

    path = []

    while node:
        path.append(node)
        node = node.parent

    path.reverse()

    print("\n=========== SOLUTION PATH ===========\n")

    for step, state in enumerate(path):

        print("Step :", step)
        print("Move :", state.move)

        for row in state.state:
            print(row)

        print("g =", state.g)
        print("h =", state.h)
        print("f =", state.f)

        print("-----------------------------------")

    print("\nGoal State Reached!")
    print("Total Moves =", len(path)-1)


# ------------------------------------------------------------
# A* Search Algorithm
# ------------------------------------------------------------
def astar(initial_state):

    open_list = []
    closed = set()

    start = Node(initial_state)

    heapq.heappush(open_list, start)

    while open_list:

        current = heapq.heappop(open_list)

        if current.state == GOAL:
            print_solution(current)
            return

        closed.add(current.state)

        for child in generate_children(current):

            if child.state not in closed:
                heapq.heappush(open_list, child)

    print("No Solution Found")


# ------------------------------------------------------------
# Initial State
# ------------------------------------------------------------

initial_state = (
    (1, 2, 3, 4),
    (5, 6, 8, 0),
    (9,10,7,12),
    (13,14,11,15)
)

print("Initial State:\n")

for row in initial_state:
    print(row)

# Run A* Search
astar(initial_state)
