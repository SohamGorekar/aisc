# ADDITIONAL PROGRAMS

## Ubuntu setup

Open Terminal and install Python:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
cd /path/to/aisc/ADDITIONAL
python3 -m venv .venv
source .venv/bin/activate
```

These programs use only the Python standard library. Run each program with
`python3` from this folder.

## Programs and runtime input

### `01_bfs.py`

```bash
python 01_bfs.py
```

Enter one graph node, such as `A`. The program prints the BFS traversal.

### `02_dfs.py`

```bash
python 02_dfs.py
```

Enter one graph node, such as `A`. The program prints the DFS traversal.

### `03_water_jug_bfs.py`

```bash
python 03_water_jug_bfs.py
```

Enter Jug A capacity, Jug B capacity, and the target:

```text
Enter capacity of Jug A: 4
Enter capacity of Jug B: 3
Enter the target amount: 2
```

### `04_hill_climbing.py`

```bash
python 04_hill_climbing.py
```

Enter the starting integer value of `x`, such as `0`.

### `05_mcculloch_pitts.py`

```bash
python 05_mcculloch_pitts.py
```

Enter two binary values:

```text
Enter x1 and x2 values separated by spaces: 1 0
```

The selected pair is evaluated by both the AND and OR neurons.

### `06_perceptron_and.py`

```bash
python 06_perceptron_and.py
```

Enter the learning rate and maximum number of epochs:

```text
Enter the learning rate: 1
Enter the maximum number of epochs: 10
```

The program trains and tests the AND perceptron using its fixed truth table.

### `07_hebb_and_bipolar.py`

```bash
python 07_hebb_and_bipolar.py
```

Enter two bipolar inputs followed by a target:

```text
Enter bipolar x1 and x2 values separated by spaces: 1 1
Enter the target value (-1 or 1): 1
```

### `08_fuzzy_set_operations.py`

```bash
python 08_fuzzy_set_operations.py
```

Enter element names, then one membership value per element for each set:

```text
Enter element names separated by spaces: x1 x2 x3 x4
Enter 4 membership values for set A: 0.2 0.5 0.8 1.0
Enter 4 membership values for set B: 0.6 0.3 0.7 0.1
```

Membership values must be between `0` and `1`. The program prints union,
intersection, and complements.
