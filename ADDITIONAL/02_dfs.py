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


start = input("Enter the starting node: ").strip().upper()

if start not in graph:
    raise SystemExit("Starting node is not present in the graph.")

print("Graph (adjacency list):", graph, "\n")
order = dfs(start, [])
print("\nDFS traversal order:", " -> ".join(order))
