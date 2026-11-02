import numpy as np
import matplotlib.pyplot as plt
def triangular(x, a, b, c):
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)
def trapezoidal(x, a, b, c, d):
    return np.maximum(np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)), 0)
def gaussian(x, mean, sigma):
    return np.exp(-((x - mean) ** 2) / (2 * sigma ** 2))
# parameters of each set: (triangular), (trapezoidal), (gaussian)
sets = {
    "Cold": ((-20, 0, 20), (-10, 0, 10, 20), (5, 6)),
    "Comfortable": ((10, 20, 30), (10, 18, 24, 32), (22, 5)),
    "Hot": ((20, 40, 60), (22, 32, 40, 50), (38, 6)),
}
functions = (triangular, trapezoidal, gaussian)
names = ("Triangular", "Trapezoidal", "Gaussian")
for i, name in enumerate(names):
    print(f"\n{name} membership values")
    print(f"{'Temp':>6}{'Cold':>8}{'Comfortable':>14}{'Hot':>8}   Class")
    for t in (10, 15, 20, 25, 30, 35):
        mu = [functions[i](t, *sets[s][i]) for s in sets]
        label = list(sets)[int(np.argmax(mu))]
        print(f"{t:>4} C{mu[0]:>8.2f}{mu[1]:>14.2f}{mu[2]:>8.2f}   {label}")
x = np.linspace(0, 40, 401)
for i, name in enumerate(names):
    plt.subplot(1, 3, i + 1)
    for s, p in sets.items():
        plt.plot(x, functions[i](x, *p[i]), label=s)
    plt.title(name)
    plt.xlabel("Temperature (C)")
    plt.ylabel("Membership")
    plt.legend()
plt.show()
