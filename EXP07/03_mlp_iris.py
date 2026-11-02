import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

data = pd.read_csv("iris.csv")

print("Dataset:")
print(data.head())


X = data[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]


y = data["Species"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=1,
    stratify=y,
)


model = MLPClassifier(
    hidden_layer_sizes=(5,),
    max_iter=1000,
    random_state=1,
)
model.fit(X_train, y_train)


prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)

print("\nAccuracy:", accuracy)
print("\nConfusion matrix:")
print(confusion_matrix(y_test, prediction, labels=model.classes_))


new_data = []
sample_count = int(input("\nEnter the number of flowers to predict: "))

for index in range(sample_count):
    values = list(
        map(
            float,
            input(
                f"Enter SepalLength SepalWidth PetalLength PetalWidth "
                f"for flower {index + 1}: "
            ).split(),
        )
    )

    if len(values) != 4:
        raise SystemExit("Each flower must have exactly 4 feature values.")

    new_data.append(values)

new_prediction = model.predict(new_data)

print("\nPredictions:")
for i, flower in enumerate(new_prediction, start=1):
    print("Flower", i, ":", flower)
