# ------------------------------------------------------------
# Program: Water Jug Problem using A* Search Algorithm
# Goal   : Obtain 2 liters in the 4-liter jug
# ------------------------------------------------------------

import heapq

# ------------------------------------------------------------
# Jug capacities
# ------------------------------------------------------------
JUG_A = 4
JUG_B = 3

# Goal State (2 liters in Jug A)
GOAL = (2, 0)

# ------------------------------------------------------------
# Node Class
# ------------------------------------------------------------
class Node:

    def __init__(self, state, parent=None, action=None, g=0):

        # Current state (JugA, JugB)
        self.state = state

        # Parent node
        self.parent = parent

        # Action performed
        self.action = action

        # Cost from initial state
        self.g = g

        # Heuristic value
        self.h = self.heuristic()

        # Evaluation function
        self.f = self.g + self.h

    # --------------------------------------------------------
    # Heuristic Function
    # Difference between current amount and goal amount
    # --------------------------------------------------------
    def heuristic(self):

        return abs(self.state[0] - GOAL[0])

    # Priority Queue comparison
    def __lt__(self, other):
        return self.f < other.f


# ------------------------------------------------------------
# Generate all possible successor states
# ------------------------------------------------------------
def generate_children(node):

    children = []

    a, b = node.state

    operations = []

    # Fill Jug A
    operations.append(((JUG_A, b), "Fill Jug A"))

    # Fill Jug B
    operations.append(((a, JUG_B), "Fill Jug B"))

    # Empty Jug A
    operations.append(((0, b), "Empty Jug A"))

    # Empty Jug B
    operations.append(((a, 0), "Empty Jug B"))

    # Pour A -> B
    transfer = min(a, JUG_B - b)

    operations.append(
        ((a - transfer, b + transfer),
         "Pour Jug A -> Jug B")
    )

    # Pour B -> A
    transfer = min(b, JUG_A - a)

    operations.append(
        ((a + transfer, b - transfer),
         "Pour Jug B -> Jug A")
    )

    # Remove duplicate states
    visited = set()

    for state, action in operations:

        if state not in visited:

            visited.add(state)

            child = Node(
                state,
                parent=node,
                action=action,
                g=node.g + 1
            )

            children.append(child)

    return children


# ------------------------------------------------------------
# Print Solution Path
# ------------------------------------------------------------
def print_solution(goal_node):

    path = []

    while goal_node:

        path.append(goal_node)

        goal_node = goal_node.parent

    path.reverse()

    print("\n========== SOLUTION ==========\n")

    for step, node in enumerate(path):

        print("Step :", step)
        print("Action :", node.action)
        print("State :", node.state)
        print("g =", node.g)
        print("h =", node.h)
        print("f =", node.f)

        print("--------------------------------")

    print("\nGoal Achieved!")


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

        # Goal Test
        if current.state == GOAL:

            print_solution(current)

            return

        closed.add(current.state)

        # Expand current state
        for child in generate_children(current):

            if child.state not in closed:

                heapq.heappush(open_list, child)

    print("No Solution Exists.")


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------

initial_state = (0, 0)

print("Initial State :", initial_state)
print("Goal State    :", GOAL)

astar(initial_state)