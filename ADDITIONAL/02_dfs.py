graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}
def dfs(node, visited):
    visited.append(node)
    print("Visiting", node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour, visited)
    return visited
print("Graph (adjacency list):", graph, "\n")
order = dfs("A", [])
print("\nDFS traversal order:", " -> ".join(order))
