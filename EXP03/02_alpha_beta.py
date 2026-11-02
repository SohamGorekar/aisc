import math
leaves = [3, 5, 6, 9, 1, 2, 0, -1]
DEPTH = 3
checked = 0
def alphabeta(depth, index, is_max, alpha, beta):
    global checked
    if depth == DEPTH:
        checked += 1
        return leaves[index]
    best = -math.inf if is_max else math.inf
    for k in (0, 1):
        value = alphabeta(depth + 1, index * 2 + k, not is_max, alpha, beta)
        if is_max:
            best = max(best, value)
            alpha = max(alpha, best)
        else:
            best = min(best, value)
            beta = min(beta, best)
        if beta <= alpha:
            if k == 0:
                kind = "MAX" if is_max else "MIN"
                print(f"{'  ' * depth}Pruned at {kind} node: alpha={alpha}, beta={beta}")
            break
    return best
print("Leaf values:", leaves, "\n")
best = alphabeta(0, 0, True, -math.inf, math.inf)
print("\nOptimal value at the root (MAX player):", best)
print("Leaf nodes evaluated:", checked, "out of", len(leaves))
