from sklearn.neural_network import MLPClassifier

X = [[1], [2], [3], [5], [6], [7]]
y = [0, 0, 0, 1, 1, 1]

model = MLPClassifier(
    hidden_layer_sizes=(5,),
    solver="lbfgs",
    max_iter=1000,
    random_state=1,
)

model.fit(X, y)

print("Training accuracy:", model.score(X, y))

hours = float(input("\nEnter the number of hours studied: "))
prediction = model.predict([[hours]])[0]
result = "Pass" if prediction == 1 else "Fail"

print("Predicted result:", result)
