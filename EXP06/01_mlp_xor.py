import numpy as np
from sklearn.neural_network import MLPClassifier
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])                       # XOR truth table
model = MLPClassifier(
    hidden_layer_sizes=(4,),
    activation="tanh",
    solver="lbfgs",
    max_iter=1000,
    random_state=1,
)
model.fit(X, y)
pred = model.predict(X)
prob = model.predict_proba(X)[:, 1]
print("MLP: 2 inputs -> 4 hidden neurons (tanh) -> 1 output\n")
print("x1  x2  Target  Predicted  Probability")
for (x1, x2), t, p, pr in zip(X, y, pred, prob):
    print(f"{x1}   {x2}     {t}        {p}        {pr:.3f}")
print("\nTraining accuracy:", model.score(X, y) * 100, "%")
print("Prediction for input [1, 0]:", model.predict([[1, 0]])[0])
