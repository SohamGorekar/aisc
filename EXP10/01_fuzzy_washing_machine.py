import numpy as np
import matplotlib.pyplot as plt


def triangular(x, a, b, c):
    x = np.asarray(x, dtype=float)
    mu = np.zeros_like(x)
    if a == b:
        mu[x <= b] = 1.0
        mask = (x > b) & (x < c)
        mu[mask] = (c - x[mask]) / (c - b)
    elif b == c:
        mu[x >= b] = 1.0
        mask = (x > a) & (x < b)
        mu[mask] = (x[mask] - a) / (b - a)
    else:
        mask = (x >= a) & (x <= b)
        mu[mask] = (x[mask] - a) / (b - a)
        mask = (x > b) & (x <= c)
        mu[mask] = (c - x[mask]) / (c - b)
    return np.clip(mu, 0, 1)


dirt_domain = np.linspace(0, 100, 1001)
grease_domain = np.linspace(0, 100, 1001)
time_domain = np.linspace(0, 60, 1201)

dirt_mfs = {
    "SD - Small Dirt": triangular(dirt_domain, 0, 0, 50),
    "MD - Medium Dirt": triangular(dirt_domain, 0, 50, 100),
    "LD - Large Dirt": triangular(dirt_domain, 50, 100, 100),
}
grease_mfs = {
    "NG - No Grease": triangular(grease_domain, 0, 0, 50),
    "MG - Medium Grease": triangular(grease_domain, 0, 50, 100),
    "LG - Large Grease": triangular(grease_domain, 50, 100, 100),
}
time_mfs = {
    "VS - Very Short": triangular(time_domain, 0, 0, 10),
    "S - Short": triangular(time_domain, 0, 10, 25),
    "M - Medium": triangular(time_domain, 10, 25, 40),
    "L - Large": triangular(time_domain, 25, 40, 60),
    "VL - Very Large": triangular(time_domain, 40, 60, 60),
}

rules = {
    ("SD - Small Dirt", "NG - No Grease"): "VS - Very Short",
    ("SD - Small Dirt", "MG - Medium Grease"): "M - Medium",
    ("SD - Small Dirt", "LG - Large Grease"): "L - Large",
    ("MD - Medium Dirt", "NG - No Grease"): "S - Short",
    ("MD - Medium Dirt", "MG - Medium Grease"): "M - Medium",
    ("MD - Medium Dirt", "LG - Large Grease"): "L - Large",
    ("LD - Large Dirt", "NG - No Grease"): "M - Medium",
    ("LD - Large Dirt", "MG - Medium Grease"): "L - Large",
    ("LD - Large Dirt", "LG - Large Grease"): "VL - Very Large",
}


def calculate_wash_time(dirt_value, grease_value):
    dirt_mu = {
        key: float(np.interp(dirt_value, dirt_domain, value))
        for key, value in dirt_mfs.items()
    }
    grease_mu = {
        key: float(np.interp(grease_value, grease_domain, value))
        for key, value in grease_mfs.items()
    }

    fired_rules = []
    for (dirt_set, grease_set), output_set in rules.items():
        strength = min(dirt_mu[dirt_set], grease_mu[grease_set])
        if strength > 0:
            fired_rules.append((strength, dirt_set, grease_set, output_set))

    aggregated = np.zeros_like(time_domain)
    for strength, _, _, output_set in fired_rules:
        clipped = np.minimum(time_mfs[output_set], strength)
        aggregated = np.maximum(aggregated, clipped)

    maximum = np.max(aggregated)
    indices = np.where(np.isclose(aggregated, maximum, atol=1e-8))[0]
    wash_time = float(np.mean(time_domain[indices]))
    return dirt_mu, grease_mu, fired_rules, aggregated, wash_time


def plot_memberships(domain, membership_functions, title, xlabel, ticks):
    plt.figure(figsize=(9, 5))
    for label, membership in membership_functions.items():
        plt.plot(domain, membership, label=label)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Membership Value")
    plt.xticks(ticks)
    plt.ylim(0, 1.08)
    plt.grid(True, alpha=0.35)
    plt.legend()
    plt.tight_layout()
    plt.show()


plot_memberships(
    dirt_domain,
    dirt_mfs,
    "Fuzzy Membership Functions: Dirt",
    "Dirt on Clothes (%)",
    [0, 50, 100],
)
plot_memberships(
    grease_domain,
    grease_mfs,
    "Fuzzy Membership Functions: Grease",
    "Grease on Clothes (%)",
    [0, 50, 100],
)
plot_memberships(
    time_domain,
    time_mfs,
    "Fuzzy Membership Functions: Wash Time",
    "Wash Time (minutes)",
    [0, 10, 25, 40, 60],
)

try:
    dirt = float(input("Enter dirt percentage (0-100): "))
    grease = float(input("Enter grease percentage (0-100): "))
except ValueError:
    raise SystemExit("Please enter numeric values.")

if not (0 <= dirt <= 100 and 0 <= grease <= 100):
    raise SystemExit("Dirt and grease must be between 0 and 100.")

dirt_mu, grease_mu, fired_rules, aggregated, wash_time = calculate_wash_time(
    dirt, grease
)

print("\nDirt membership values:")
for label, value in dirt_mu.items():
    if value > 0:
        print(f"{label}: {value:.2f}")

print("\nGrease membership values:")
for label, value in grease_mu.items():
    if value > 0:
        print(f"{label}: {value:.2f}")

print("\nActivated IF-THEN rules:")
for strength, dirt_set, grease_set, output_set in fired_rules:
    print(
        f"IF {dirt_set} AND {grease_set} THEN {output_set}; strength = {strength:.2f}"
    )

print(f"\nRecommended wash time (MoM): {wash_time:.2f} minutes")

plt.figure(figsize=(9, 5))
plt.plot(time_domain, aggregated, label="Aggregated output membership")
plt.axvline(
    wash_time,
    linestyle="--",
    label=f"MoM wash time = {wash_time:.2f} min",
)
plt.title("Wash-Time Output and Mean of Maximum Defuzzification")
plt.xlabel("Wash Time (minutes)")
plt.ylabel("Membership Value")
plt.xticks([0, 10, 25, 40, 60])
plt.ylim(0, 1.08)
plt.grid(True, alpha=0.35)
plt.legend()
plt.tight_layout()
plt.show()
