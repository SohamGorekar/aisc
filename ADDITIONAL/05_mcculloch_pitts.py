inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
def mp_neuron(x1, x2, w1, w2, theta):
    net = x1 * w1 + x2 * w2
    return net, 1 if net >= theta else 0
for gate, theta in (("AND", 2), ("OR", 1)):
    print(f"\n{gate} gate (w1 = w2 = 1, threshold = {theta})")
    print("x1  x2  net  y")
    for x1, x2 in inputs:
        net, y = mp_neuron(x1, x2, 1, 1, theta)
        print(f"{x1}   {x2}   {net}    {y}")
