def triangular(value, left, peak, right):
    if left == peak:
        return 1.0 if value <= peak else max(0.0, (right - value) / (right - peak))
    if peak == right:
        return 1.0 if value >= peak else max(0.0, (value - left) / (peak - left))
    if value <= left or value >= right:
        return 0.0
    if value <= peak:
        return (value - left) / (peak - left)
    return (right - value) / (right - peak)


def recommend(dirt, grease):
    dirt_sets = {
        "small": triangular(dirt, 0, 0, 50),
        "medium": triangular(dirt, 0, 50, 100),
        "large": triangular(dirt, 50, 100, 100),
    }
    grease_sets = {
        "low": triangular(grease, 0, 0, 50),
        "medium": triangular(grease, 0, 50, 100),
        "high": triangular(grease, 50, 100, 100),
    }
    rules = {
        ("small", "low"): (15, 25),
        ("small", "medium"): (25, 30),
        ("small", "high"): (35, 40),
        ("medium", "low"): (25, 30),
        ("medium", "medium"): (35, 40),
        ("medium", "high"): (45, 50),
        ("large", "low"): (35, 40),
        ("large", "medium"): (45, 50),
        ("large", "high"): (55, 60),
    }

    weighted_time = 0.0
    weighted_temperature = 0.0
    total_strength = 0.0
    for dirt_set, dirt_strength in dirt_sets.items():
        for grease_set, grease_strength in grease_sets.items():
            strength = min(dirt_strength, grease_strength)
            if strength > 0:
                time, temperature = rules[(dirt_set, grease_set)]
                weighted_time += strength * time
                weighted_temperature += strength * temperature
                total_strength += strength

    if total_strength == 0:
        raise ValueError("No fuzzy rule was activated.")
    return weighted_time / total_strength, weighted_temperature / total_strength


dirt = float(input("Enter dirt percentage (0-100): "))
grease = float(input("Enter grease percentage (0-100): "))

if not 0 <= dirt <= 100 or not 0 <= grease <= 100:
    raise SystemExit("Dirt and grease must be between 0 and 100.")

wash_time, water_temperature = recommend(dirt, grease)
print(f"\nRecommended wash time: {wash_time:.2f} minutes")
print(f"Recommended water temperature: {water_temperature:.2f} C")
