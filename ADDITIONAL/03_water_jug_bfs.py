from collections import deque
CAP_A, CAP_B, TARGET = 4, 3, 2
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
print("Jug A = 4 L, Jug B = 3 L, Target = 2 L\n")
print(f"{'Step':<6}{'Action':<14}{'(A, B)'}")
for i, (action, state) in enumerate(path):
    print(f"{i:<6}{action:<14}{state}")
print("\nTotal steps:", len(path) - 1)
