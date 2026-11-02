minmax_count = 0


def minmax(depth, node, isMax, values):
    global minmax_count
    minmax_count += 1
    if depth == 4:
        return values[node]

    if isMax:
        best = float("-inf")
        for i in range(2):
            val = minmax(depth + 1, node * 2 + i, False, values)
            best = max(best, val)
        return best
    else:
        best = float("inf")
        for i in range(2):
            val = minmax(depth + 1, node * 2 + i, True, values)
            best = min(best, val)
        return best


ab_count = 0


def alpha_beta(depth, node, isMax, values, alpha, beta):
    global ab_count
    ab_count += 1
    if depth == 4:
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


values = [3, 5, 6, 9, 1, 2, 0, -1, 4, 8, 2, 7, -3, 5, 1, 0]

minmax_result = minmax(0, 0, True, values)
ab_result = alpha_beta(0, 0, True, values, float("-inf"), float("inf"))

print("Min-Max Optimal Value      =", minmax_result)
print("Alpha-Beta Optimal Value   =", ab_result)
print("Nodes evaluated by Min-Max     :", minmax_count)
print("Nodes evaluated by Alpha-Beta  :", ab_count)
print("Nodes saved by pruning         :", minmax_count - ab_count)
