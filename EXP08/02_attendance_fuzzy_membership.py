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
    "Low": ((-50, 0, 50), (-10, 0, 30, 50), (0, 15)),
    "Moderate": ((25, 50, 75), (30, 50, 70, 90), (50, 12)),
    "High": ((50, 100, 150), (60, 80, 100, 110), (95, 10)),
}
functions = (triangular, trapezoidal, gaussian)
names = ("Triangular", "Trapezoidal", "Gaussian")
for i, name in enumerate(names):
    print(f"\n{name} membership values")
    print(f"{'Attendance':>11}{'Low':>8}{'Moderate':>10}{'High':>8}")
    for a in (40, 50, 60, 70, 80, 90):
        mu = [functions[i](a, *sets[s][i]) for s in sets]
        print(f"{a:>10}%{mu[0]:>8.2f}{mu[1]:>10.2f}{mu[2]:>8.2f}")
x = np.linspace(0, 100, 501)
for i, name in enumerate(names):
    plt.subplot(1, 3, i + 1)
    for s, p in sets.items():
        plt.plot(x, functions[i](x, *p[i]), label=s)
    plt.title(name)
    plt.xlabel("Attendance (%)")
    plt.ylabel("Membership")
    plt.legend()
plt.show()
