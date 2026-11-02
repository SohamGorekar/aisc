import numpy as np
np.random.seed(1)
# columns: hours studied, attendance (%)
data = np.array([
    [1, 40], [2, 50], [3, 60], [4, 55],
    [6, 75], [7, 80], [8, 90], [9, 95],
])
target = np.array([[0], [0], [0], [0], [1], [1], [1], [1]])     # 1 = Pass, 0 = Fail
X = data / [10, 100]                                             # normalise inputs
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
lr = 0.5
W1 = np.random.randn(2, 3)
b1 = np.zeros(3)
W2 = np.random.randn(3, 1)
b2 = np.zeros(1)
for epoch in range(1, 5001):
    # forward pass
    H = sigmoid(X @ W1 + b1)
    O = sigmoid(H @ W2 + b2)
    # backward pass: error terms (delta) and weight updates
    delta_o = (target - O) * O * (1 - O)
    delta_h = (delta_o @ W2.T) * H * (1 - H)
    W2 += lr * H.T @ delta_o
    b2 += lr * delta_o.sum(axis=0)
    W1 += lr * X.T @ delta_h
    b1 += lr * delta_h.sum(axis=0)
    if epoch % 1000 == 0:
        print(f"Epoch {epoch:4d}   Mean squared error = {np.mean((target - O) ** 2):.5f}")
def predict(hours, attendance):
    x = np.array([hours, attendance]) / [10, 100]
    return sigmoid(sigmoid(x @ W1 + b1) @ W2 + b2)[0]
print("\nTraining data results")
print("Hours  Attendance  Output  Result")
for (hrs, att), t in zip(data, target):
    p = predict(hrs, att)
    print(f"{hrs:>5}  {att:>10}  {p:.3f}   {'Pass' if p > 0.5 else 'Fail'}")
print("\nPrediction for new students")
for hrs, att in [(7, 85), (2, 45), (8, 92), (1, 35)]:
    p = predict(hrs, att)
    result = "Pass" if p > 0.5 else "Fail"
    print(f"Hours = {hrs}, Attendance = {att}%  ->  {p:.3f}  ->  {result}")
