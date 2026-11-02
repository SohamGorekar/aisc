count = int(input("Enter the number of cities: "))

if count < 2:
    raise SystemExit("At least two cities are required.")

cities = [chr(ord("A") + i) for i in range(count)]
graph = []

print("Enter the cost matrix row by row, separated by spaces:")
for i in range(count):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    if len(row) != count:
        raise SystemExit(f"Each row must contain {count} values.")
    graph.append(row)

n = len(graph)
best_cost = float("inf")
best_path = []


def dfs(city, visited, path, cost):
    global best_cost, best_path
    if len(path) == n:
        total = cost + graph[city][0]
        tour = path + [0]
        print("Tour:", " -> ".join(cities[i] for i in tour), "| Cost =", total)
        if total < best_cost:
            best_cost, best_path = total, tour
        return
    for nxt in range(n):
        if nxt not in visited:
            dfs(nxt, visited + [nxt], path + [nxt], cost + graph[city][nxt])


print("All tours found by DFS:")
dfs(0, [0], [0], 0)
print("\nMinimum cost tour:", " -> ".join(cities[i] for i in best_path))
print("Minimum cost:", best_cost)
