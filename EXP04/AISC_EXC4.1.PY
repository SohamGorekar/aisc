def alpha_beta(depth, node, isMax, values, alpha, beta):
    if depth == 3:
        return values[node]

    if isMax:
        best = float("-inf")
        for i in range(2):
            val = alpha_beta(depth + 1, node * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Branch pruned at MAX node (node={node}, depth={depth})")
                break
        return best
    else:
        best = float("inf")
        for i in range(2):
            val = alpha_beta(depth + 1, node * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Branch pruned at MIN node (node={node}, depth={depth})")
                break
        return best


values = [2, 3, 5, 9, 0, 1, 7, 5]

result = alpha_beta(0, 0, True, values, float("-inf"), float("inf"))

print("Optimal Value =", result)
