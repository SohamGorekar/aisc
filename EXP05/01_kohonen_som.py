import numpy as np
X = np.array([[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]], dtype=float)
W = np.array([[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3]])   # 2 cluster units
alpha = 0.6                                                    # learning rate
epochs = 10
def winner(x):
    distances = ((W - x) ** 2).sum(axis=1)       # squared Euclidean distance
    return int(np.argmin(distances))
print("Initial weights:\n", W)
for epoch in range(1, epochs + 1):
    for x in X:
        j = winner(x)
        W[j] += alpha * (x - W[j])               # update winning unit only
    alpha *= 0.5
    if epoch <= 3 or epoch == epochs:
        print(f"\nEpoch {epoch}: weights (next learning rate = {alpha:.4f})")
        print(W.round(3))
print("\nClustering result")
for x in X:
    print("Input", x.astype(int), "-> Cluster", winner(x))
