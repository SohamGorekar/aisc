import heapq
N = 8
def is_safe(cols, col):
    row = len(cols)
    return all(c != col and abs(c - col) != row - r for r, c in enumerate(cols))
def a_star():
    heap = [(N, N, [])]            # (f = g + h, h, columns placed so far)
    expanded = 0
    while heap:
        f, h, cols = heapq.heappop(heap)
        expanded += 1
        if h == 0:
            return cols, expanded
        for col in range(N):
            if is_safe(cols, col):
                g = len(cols) + 1
                heapq.heappush(heap, (g + (N - g), N - g, cols + [col]))
    return None, expanded
solution, expanded = a_star()
print("A* solution for", N, "queens (column of each row):", solution)
print("Nodes expanded:", expanded)
print()
for r in range(N):
    print(" ".join("Q" if solution[r] == c else "." for c in range(N)))
