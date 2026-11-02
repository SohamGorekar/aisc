import numpy as np

weights = np.array(
    list(map(float, input("Enter 2 initial weights separated by spaces: ").split()))
)

if len(weights) != 2:
    raise SystemExit("Enter exactly 2 initial weights.")


inputs = list(map(float, input("Enter input values separated by spaces: ").split()))

if not inputs:
    raise SystemExit("Enter at least one input value.")

learning_rate = 0.5

print("Initial Weights:", weights)

for x in inputs:

    d1 = abs(x - weights[0])
    d2 = abs(x - weights[1])

    if d1 < d2:
        winner = 0
    else:
        winner = 1

    weights[winner] = weights[winner] + learning_rate * (x - weights[winner])

    print("\nInput :", x)
    print("Winner Neuron :", winner + 1)
    print("Updated Weights :", weights)

print("\nFinal Weights :", weights)
