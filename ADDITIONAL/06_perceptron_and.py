inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
targets = [0, 0, 0, 1]
w1 = w2 = bias = 0
lr = 1
def output(x1, x2):
    return 1 if w1 * x1 + w2 * x2 + bias > 0 else 0
for epoch in range(1, 11):
    errors = 0
    for (x1, x2), t in zip(inputs, targets):
        e = t - output(x1, x2)
        if e != 0:
            w1 += lr * e * x1
            w2 += lr * e * x2
            bias += lr * e
            errors += 1
    print(f"Epoch {epoch}: w1 = {w1}, w2 = {w2}, bias = {bias}, errors = {errors}")
    if errors == 0:
        break
print("\nTesting the trained perceptron")
print("x1  x2  Target  Output")
for (x1, x2), t in zip(inputs, targets):
    print(f"{x1}   {x2}     {t}       {output(x1, x2)}")
