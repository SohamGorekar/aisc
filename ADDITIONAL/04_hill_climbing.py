def f(x):
    return -((x - 3) ** 2) + 9


x = int(input("Enter the starting value of x: "))
step = 0
print(f"{'Step':<6}{'x':<6}{'f(x)'}")
while True:
    print(f"{step:<6}{x:<6}{f(x)}")
    best = max((x - 1, x + 1), key=f)
    if f(best) <= f(x):
        break
    x = best
    step += 1
print(f"\nPeak (local maximum) reached at x = {x}, f(x) = {f(x)}")
