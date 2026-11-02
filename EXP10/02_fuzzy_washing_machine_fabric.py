import numpy as np


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


def calculate_wash_time(dirt, grease, fabric):
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
    fabric_sets = {
        "delicate": 1.0 if fabric == "delicate" else 0.0,
        "normal": 1.0 if fabric == "normal" else 0.0,
        "heavy": 1.0 if fabric == "heavy" else 0.0,
    }
    base_time = {
        ("small", "low"): 10,
        ("small", "medium"): 20,
        ("small", "high"): 30,
        ("medium", "low"): 20,
        ("medium", "medium"): 30,
        ("medium", "high"): 40,
        ("large", "low"): 30,
        ("large", "medium"): 40,
        ("large", "high"): 50,
    }
    fabric_adjustment = {"delicate": -5, "normal": 0, "heavy": 5}

    weighted_time = 0.0
    total_strength = 0.0
    for dirt_set, dirt_strength in dirt_sets.items():
        for grease_set, grease_strength in grease_sets.items():
            strength = min(dirt_strength, grease_strength)
            if strength > 0:
                weighted_time += strength * (
                    base_time[(dirt_set, grease_set)] + fabric_adjustment[fabric]
                )
                total_strength += strength

    if total_strength == 0:
        raise ValueError("No fuzzy rule was activated.")
    return weighted_time / total_strength


dirt = float(input("Enter dirt percentage (0-100): "))
grease = float(input("Enter grease percentage (0-100): "))
fabric = input("Enter fabric type (delicate/normal/heavy): ").strip().lower()

if not 0 <= dirt <= 100 or not 0 <= grease <= 100:
    raise SystemExit("Dirt and grease must be between 0 and 100.")
if fabric not in {"delicate", "normal", "heavy"}:
    raise SystemExit("Fabric must be delicate, normal, or heavy.")

wash_time = calculate_wash_time(dirt, grease, fabric)
print(f"\nRecommended wash time: {wash_time:.2f} minutes")
