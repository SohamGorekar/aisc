from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}


def bfs(start):
    visited = [start]
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print("Visiting", node, "| Queue now:", list(queue))
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited


start = input("Enter the starting node: ").strip().upper()

if start not in graph:
    raise SystemExit("Starting node is not present in the graph.")

print("Graph (adjacency list):", graph, "\n")
order = bfs(start)
print("\nBFS traversal order:", " -> ".join(order))
