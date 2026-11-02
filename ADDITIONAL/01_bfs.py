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
print("Graph (adjacency list):", graph, "\n")
order = bfs("A")
print("\nBFS traversal order:", " -> ".join(order))
