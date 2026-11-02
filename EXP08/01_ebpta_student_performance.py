import numpy as np

X = np.array([[2, 50], [3, 55], [4, 60], [5, 70], [6, 75], [7, 85]], dtype=float)


Y = np.array([[0], [0], [0], [1], [1], [1]], dtype=float)


X[:, 0] = X[:, 0] / 10
X[:, 1] = X[:, 1] / 100


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


W1 = np.array(
    [
        [0.2, 0.3, 0.4],
        [0.4, 0.5, 0.6],
    ]
)

W2 = np.array(
    [
        [0.6],
        [0.7],
        [0.8],
    ]
)

B1 = np.array([[0.1, 0.1, 0.1]])
B2 = np.array([[0.1]])

learning_rate = 0.5
epochs = 5000


for epoch in range(epochs):

    hidden_input = np.dot(X, W1) + B1
    hidden_output = sigmoid(hidden_input)

    output_input = np.dot(hidden_output, W2) + B2
    output = sigmoid(output_input)

    error = Y - output

    output_delta = error * output * (1 - output)

    hidden_delta = hidden_output * (1 - hidden_output) * np.dot(output_delta, W2.T)

    W2 = W2 + learning_rate * np.dot(hidden_output.T, output_delta)
    W1 = W1 + learning_rate * np.dot(X.T, hidden_delta)

    B2 = B2 + learning_rate * np.sum(output_delta, axis=0)
    B1 = B1 + learning_rate * np.sum(hidden_delta, axis=0)


print("\nTraining Completed!")
print("\nChecking Training Data:")

for i in range(len(X)):

    hidden = sigmoid(np.dot(X[i : i + 1], W1) + B1)
    result = sigmoid(np.dot(hidden, W2) + B2)

    predicted = 1 if result[0][0] >= 0.5 else 0

    actual_label = "Pass" if Y[i][0] == 1 else "Fail"
    predicted_label = "Pass" if predicted == 1 else "Fail"

    print(
        "Hours:",
        int(X[i][0] * 10),
        "Attendance:",
        int(X[i][1] * 100),
        "Actual:",
        actual_label,
        "Predicted:",
        predicted_label,
    )


print("\n----------------------------------")
print("TEST THE TRAINED EBPTA SYSTEM")
print("----------------------------------")

hours = float(input("Enter Hours Studied: "))
attendance = float(input("Enter Attendance (%): "))


new_student = np.array([[hours / 10, attendance / 100]])


hidden = sigmoid(np.dot(new_student, W1) + B1)
result = sigmoid(np.dot(hidden, W2) + B2)

predicted = 1 if result[0][0] >= 0.5 else 0

predicted_label = "Pass" if predicted == 1 else "Fail"

print("\nEBPTA Prediction:", predicted_label)
print("Output Value:", round(result[0][0], 4))


print("\nTo check whether the prediction is correct:")

actual = int(input("Enter Expected Target (0 = Fail, 1 = Pass): "))

if predicted == actual:
    print("Prediction is CORRECT")
else:
    print("Prediction is INCORRECT")

print("----------------------------------")
