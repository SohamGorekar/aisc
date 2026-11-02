import numpy as np

weights = np.array(
    list(map(float, input("Enter 3 initial weights separated by spaces: ").split()))
)

if len(weights) != 3:
    raise SystemExit("Enter exactly 3 initial weights.")


inputs = list(map(float, input("Enter input values separated by spaces: ").split()))

if not inputs:
    raise SystemExit("Enter at least one input value.")

learning_rate = 0.5

print("Initial Weights:", weights)

for x in inputs:

    distances = np.abs(x - weights)

    winner = np.argmin(distances)

    weights[winner] = weights[winner] + learning_rate * (x - weights[winner])

    print("\nInput:", x)
    print("Winner Neuron:", winner + 1)
    print("Updated Weights:", weights)

print("\nFinal Weights:", weights)
