import heapq
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
def heuristic(state):
    # sum of Manhattan distances of all tiles from their goal positions
    dist = 0
    for i, tile in enumerate(state):
        if tile != 0:
            goal_row, goal_col = divmod(tile - 1, 4)
            dist += abs(i // 4 - goal_row) + abs(i % 4 - goal_col)
    return dist
def neighbors(state):
    z = state.index(0)
    row, col = divmod(z, 4)
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        r, c = row + dr, col + dc
        if 0 <= r < 4 and 0 <= c < 4:
            new = list(state)
            n = r * 4 + c
            new[z], new[n] = new[n], new[z]
            yield tuple(new)
def a_star(start):
    heap = [(heuristic(start), 0, start, [start])]    # (f, g, state, path)
    visited = set()
    while heap:
        f, g, state, path = heapq.heappop(heap)
        if state == GOAL:
            return path
        if state in visited:
            continue
        visited.add(state)
        for nxt in neighbors(state):
            if nxt not in visited:
                h = heuristic(nxt)
                heapq.heappush(heap, (g + 1 + h, g + 1, nxt, path + [nxt]))
    return None
start = (1, 2, 3, 4, 5, 0, 7, 8, 9, 6, 10, 12, 13, 14, 11, 15)
path = a_star(start)
print("Number of moves:", len(path) - 1)
for step, state in enumerate(path):
    print("\nStep", step, "(h =", heuristic(state), ")")
    for i in range(0, 16, 4):
        print(*[f"{t:2}" if t else " _" for t in state[i:i + 4]])
