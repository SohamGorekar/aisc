from collections import deque

CAP_A = int(input("Enter capacity of Jug A: "))
CAP_B = int(input("Enter capacity of Jug B: "))
TARGET = int(input("Enter the target amount: "))

if CAP_A <= 0 or CAP_B <= 0 or not 0 <= TARGET <= max(CAP_A, CAP_B):
    raise SystemExit("Enter positive capacities and a valid target.")


def next_moves(x, y):
    pour_ab = min(x, CAP_B - y)
    pour_ba = min(y, CAP_A - x)
    return [
        ("Fill A", (CAP_A, y)),
        ("Fill B", (x, CAP_B)),
        ("Empty A", (0, y)),
        ("Empty B", (x, 0)),
        ("Pour A -> B", (x - pour_ab, y + pour_ab)),
        ("Pour B -> A", (x + pour_ba, y - pour_ba)),
    ]


def bfs():
    queue = deque([[("Start", (0, 0))]])
    visited = {(0, 0)}
    while queue:
        path = queue.popleft()
        x, y = path[-1][1]
        if x == TARGET or y == TARGET:
            return path
        for action, state in next_moves(x, y):
            if state not in visited:
                visited.add(state)
                queue.append(path + [(action, state)])
    return None


path = bfs()

if path is None:
    raise SystemExit("No solution exists for the supplied values.")

print(f"Jug A = {CAP_A} L, Jug B = {CAP_B} L, Target = {TARGET} L\n")
print(f"{'Step':<6}{'Action':<14}{'(A, B)'}")
for i, (action, state) in enumerate(path):
    print(f"{i:<6}{action:<14}{state}")
print("\nTotal steps:", len(path) - 1)
