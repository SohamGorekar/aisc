A = {"x1": 0.2, "x2": 0.5, "x3": 0.8, "x4": 1.0}
B = {"x1": 0.6, "x2": 0.3, "x3": 0.7, "x4": 0.1}
print(f"{'Element':<8}{'A':<6}{'B':<6}{'Union':<7}{'Inter':<7}{'not A':<7}not B")
for x in A:
    u, i = max(A[x], B[x]), min(A[x], B[x])
    print(f"{x:<8}{A[x]:<6}{B[x]:<6}{u:<7}{i:<7}{1 - A[x]:<7.2f}{1 - B[x]:.2f}")
