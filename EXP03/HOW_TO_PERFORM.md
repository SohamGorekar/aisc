# EXP03 - Informed Search

## Ubuntu setup

Open Terminal and install Python:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
cd /path/to/aisc/EXP03
python3 -m venv .venv
source .venv/bin/activate
```

These programs use only the Python standard library. Run each program with
`python3` from this folder.

## Programs

### `01_fifteen_puzzle_astar.py`

Run:

```bash
python 01_fifteen_puzzle_astar.py
```

Enter all 16 puzzle values in row order. Use `0` for the blank:

```text
Enter the 15-puzzle values row-wise (use 0 for blank): 1 2 3 4 5 6 8 0 9 10 7 12 13 14 11 15
```

Every value from `0` through `15` must appear exactly once.

### `02_water_jug_astar.py`

Run:

```bash
python 02_water_jug_astar.py
```

Enter Jug A capacity, Jug B capacity, and the target amount in Jug A:

```text
Enter capacity of Jug A: 4
Enter capacity of Jug B: 3
Enter the target amount in Jug A: 2
```

### `03_N_queens_astar.py`

Run:

```bash
python 03_N_queens_astar.py
```

Enter a positive board size:

```text
Enter the number of queens: 4
```
