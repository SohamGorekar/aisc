# EXP04 - Alpha-Beta Pruning

## Ubuntu setup

Open Terminal and install Python:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
cd /path/to/aisc/EXP04
python3 -m venv .venv
source .venv/bin/activate
```

These programs use only the Python standard library. Run each program with
`python3` from this folder.

## Programs

### `01_minimax.py`

Run:

```bash
python 01_minimax.py
```

Enter exactly eight integer leaf values:

```text
Enter 8 leaf values separated by spaces: 3 5 6 9 1 2 0 -1
```

The program prints the minimax value.

### `02_alpha_beta.py`

Run:

```bash
python 02_alpha_beta.py
```

Enter the same eight-value format:

```text
Enter 8 leaf values separated by spaces: 3 5 6 9 1 2 0 -1
```

The program prints the optimal value and the leaf nodes evaluated after
pruning.

### Original exercise files

`AISC_EXP4.PY`, `AISC_EXC4.1.PY`, and `AISC_EXC4.2.PY` are additional
alpha-beta/minimax variants with fixed values from the original exercise.
They do not request runtime input. Run any of them with:

```bash
python AISC_EXP4.PY
```

Change the source values only when intentionally testing a different fixed
game tree.
