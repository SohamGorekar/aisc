import heapq

JUG_A = int(input("Enter capacity of Jug A: "))
JUG_B = int(input("Enter capacity of Jug B: "))
goal_amount = int(input("Enter the target amount in Jug A: "))


GOAL = (goal_amount, 0)

if JUG_A <= 0 or JUG_B <= 0 or not 0 <= goal_amount <= JUG_A:
    raise SystemExit("Enter positive capacities and a valid target amount.")


class Node:

    def __init__(self, state, parent=None, action=None, g=0):

        self.state = state

        self.parent = parent

        self.action = action

        self.g = g

        self.h = self.heuristic()

        self.f = self.g + self.h

    def heuristic(self):

        return abs(self.state[0] - GOAL[0])

    def __lt__(self, other):
        return self.f < other.f


def generate_children(node):

    children = []

    a, b = node.state

    operations = []

    operations.append(((JUG_A, b), "Fill Jug A"))

    operations.append(((a, JUG_B), "Fill Jug B"))

    operations.append(((0, b), "Empty Jug A"))

    operations.append(((a, 0), "Empty Jug B"))

    transfer = min(a, JUG_B - b)

    operations.append(((a - transfer, b + transfer), "Pour Jug A -> Jug B"))

    transfer = min(b, JUG_A - a)

    operations.append(((a + transfer, b - transfer), "Pour Jug B -> Jug A"))

    visited = set()

    for state, action in operations:

        if state not in visited:

            visited.add(state)

            child = Node(state, parent=node, action=action, g=node.g + 1)

            children.append(child)

    return children


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

    print("No Solution Exists.")


initial_state = (0, 0)

print("Initial State :", initial_state)
print("Goal State    :", GOAL)

astar(initial_state)
