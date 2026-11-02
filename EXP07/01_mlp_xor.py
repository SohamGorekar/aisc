from sklearn.neural_network import MLPClassifier

X = [[0, 0], [0, 1], [1, 0], [1, 1]]


y = [0, 1, 1, 0]


mlp = MLPClassifier(
    hidden_layer_sizes=(4,),
    max_iter=1000,
    random_state=1,
)


mlp.fit(X, y)


prediction = mlp.predict(X)


print("Input:")
print(X)

print("Actual Output:")
print(y)

print("Predicted Output:")
print(prediction)
