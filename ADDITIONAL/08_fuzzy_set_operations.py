elements = input("Enter element names separated by spaces: ").split()

if not elements:
    raise SystemExit("Enter at least one element.")

A_values = list(
    map(
        float,
        input(f"Enter {len(elements)} membership values for set A: ").split(),
    )
)
B_values = list(
    map(
        float,
        input(f"Enter {len(elements)} membership values for set B: ").split(),
    )
)

if len(A_values) != len(elements) or len(B_values) != len(elements):
    raise SystemExit("Enter one membership value for every element.")

if any(value < 0 or value > 1 for value in A_values + B_values):
    raise SystemExit("Membership values must be between 0 and 1.")

A = dict(zip(elements, A_values))
B = dict(zip(elements, B_values))
print(f"{'Element':<8}{'A':<6}{'B':<6}{'Union':<7}{'Inter':<7}{'not A':<7}not B")
for x in A:
    u, i = max(A[x], B[x]), min(A[x], B[x])
    print(f"{x:<8}{A[x]:<6}{B[x]:<6}{u:<7}{i:<7}{1 - A[x]:<7.2f}{1 - B[x]:.2f}")
