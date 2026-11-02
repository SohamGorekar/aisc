values = list(
    map(
        int,
        input("Enter bipolar x1 and x2 values separated by spaces: ").split(),
    )
)

if len(values) != 2 or any(value not in (-1, 1) for value in values):
    raise SystemExit("Enter exactly two bipolar values: -1 or 1.")

inputs = [tuple(values)]
targets = [int(input("Enter the target value (-1 or 1): "))]

if targets[0] not in (-1, 1):
    raise SystemExit("The target must be -1 or 1.")
w1 = w2 = bias = 0
print("x1  x2   t   dw1 dw2  db | w1  w2   b")
for (x1, x2), t in zip(inputs, targets):
    dw1, dw2, db = x1 * t, x2 * t, t
    w1, w2, bias = w1 + dw1, w2 + dw2, bias + db
    print(
        f"{x1:>2} {x2:>3} {t:>3} {dw1:>5} {dw2:>3} {db:>3} | {w1:>2} {w2:>3} {bias:>3}"
    )
print("\nTesting the trained network")
for (x1, x2), t in zip(inputs, targets):
    y = 1 if w1 * x1 + w2 * x2 + bias > 0 else -1
    print(f"Input ({x1:>2}, {x2:>2}) -> Output {y:>2} (target {t:>2})")
