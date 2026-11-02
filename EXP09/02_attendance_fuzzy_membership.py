import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 500)


def triangular(x, a, b, c):
    return np.maximum(
        np.minimum(
            (x - a) / (b - a),
            (c - x) / (c - b),
        ),
        0,
    )


def trapezoidal(x, a, b, c, d):
    return np.maximum(
        np.minimum(
            np.minimum((x - a) / (b - a), 1),
            (d - x) / (d - c),
        ),
        0,
    )


def gaussian(x, mean, sigma):
    return np.exp(-((x - mean) ** 2) / (2 * sigma**2))


sets = {
    "Low": {
        "triangular": (-50, 0, 50),
        "trapezoidal": (-10, 0, 30, 50),
        "gaussian": (0, 15),
    },
    "Moderate": {
        "triangular": (25, 50, 75),
        "trapezoidal": (30, 50, 70, 90),
        "gaussian": (50, 12),
    },
    "High": {
        "triangular": (50, 100, 150),
        "trapezoidal": (60, 80, 100, 110),
        "gaussian": (95, 10),
    },
}


membership_functions = {
    "Triangular": triangular,
    "Trapezoidal": trapezoidal,
    "Gaussian": gaussian,
}

attendance_values = list(
    map(
        float,
        input(
            "\nEnter attendance values to evaluate, separated by spaces "
            "(default: 40 50 60 70 80 90): "
        ).split(),
    )
)

if not attendance_values:
    attendance_values = [40, 50, 60, 70, 80, 90]

for function_name, function in membership_functions.items():
    print(f"\n{function_name} membership values")
    print(f"{'Attendance':>11}{'Low':>8}{'Moderate':>10}{'High':>8}")

    for attendance in attendance_values:
        values = []

        for parameters in sets.values():
            values.append(function(attendance, *parameters[function_name.lower()]))

        print(
            f"{attendance:>10}%"
            f"{values[0]:>8.2f}"
            f"{values[1]:>10.2f}"
            f"{values[2]:>8.2f}"
        )


plt.figure(figsize=(15, 5))

for index, (function_name, function) in enumerate(membership_functions.items()):
    plt.subplot(1, 3, index + 1)

    for set_name, parameters in sets.items():
        plt.plot(
            x,
            function(x, *parameters[function_name.lower()]),
            label=set_name,
        )

    plt.title(function_name)
    plt.xlabel("Attendance (%)")
    plt.ylabel("Membership Value")
    plt.ylim(0, 1.1)
    plt.grid(True)
    plt.legend()

plt.tight_layout()
plt.show()
