import numpy as np


def sigmoid(value):
    return 1 / (1 + np.exp(-value))


data = np.array(
    [
        [2, 50],
        [3, 55],
        [4, 60],
        [5, 70],
        [6, 75],
        [7, 85],
    ],
    dtype=float,
)
target = np.array([[0], [0], [0], [1], [1], [1]], dtype=float)
X = data / [10, 100]

np.random.seed(1)
W1 = np.random.randn(2, 3)
B1 = np.zeros((1, 3))
W2 = np.random.randn(3, 1)
B2 = np.zeros((1, 1))

learning_rate = 0.1
epochs = 5000

for _ in range(epochs):
    hidden = sigmoid(X @ W1 + B1)
    output = sigmoid(hidden @ W2 + B2)

    output_delta = (target - output) * output * (1 - output)
    hidden_delta = (output_delta @ W2.T) * hidden * (1 - hidden)

    W2 += learning_rate * hidden.T @ output_delta
    B2 += learning_rate * output_delta.sum(axis=0, keepdims=True)
    W1 += learning_rate * X.T @ hidden_delta
    B1 += learning_rate * hidden_delta.sum(axis=0, keepdims=True)


print(f"Learning rate: {learning_rate}")
print("Training results:")
for row, expected in zip(data, target):
    probability = sigmoid(sigmoid((row / [10, 100]) @ W1 + B1) @ W2 + B2)[0, 0]
    result = "Pass" if probability >= 0.5 else "Fail"
    expected_result = "Pass" if expected[0] == 1 else "Fail"
    print(
        f"Hours={row[0]:.0f}, Attendance={row[1]:.0f}% -> "
        f"{result} ({probability:.3f}), expected {expected_result}"
    )
