leaves = list(map(int, input("Enter 8 leaf values separated by spaces: ").split()))

if len(leaves) != 8:
    raise SystemExit("Enter exactly 8 leaf values.")
DEPTH = 3


def minimax(depth, index, is_max):
    if depth == DEPTH:
        return leaves[index]
    left = minimax(depth + 1, index * 2, not is_max)
    right = minimax(depth + 1, index * 2 + 1, not is_max)
    value = max(left, right) if is_max else min(left, right)
    kind = "MAX" if is_max else "MIN"
    pad = "  " * depth
    print(f"{pad}{kind} node (level {depth}): children ({left}, {right}) -> {value}")
    return value


print("Leaf values:", leaves, "\n")
best = minimax(0, 0, True)
print("\nOptimal value at the root (MAX player):", best)
