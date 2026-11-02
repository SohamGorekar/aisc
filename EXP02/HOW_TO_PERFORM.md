# EXP02 - Uninformed Search

## Ubuntu setup

Open Terminal and install Python:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
cd /path/to/aisc/EXP02
python3 -m venv .venv
source .venv/bin/activate
```

These programs use only the Python standard library. Run each program with
`python3` from this folder.

## Programs

### `01_N_queens_uninformed.py`

Run:

```bash
python 01_N_queens_uninformed.py
```

Input:

```text
Enter the number of queens: 8
```

The program prints one valid N-Queens board. Enter a positive integer.

### `02_tsp_dfs.py`

Run:

```bash
python 02_tsp_dfs.py
```

Enter the number of cities, followed by one complete cost-matrix row per
prompt. For four cities, enter:

```text
Enter the number of cities: 4
Row 1: 0 10 15 20
Row 2: 10 0 35 25
Row 3: 15 35 0 30
Row 4: 20 25 30 0
```

The program lists every DFS tour and prints the minimum-cost tour. The
starting city is always `A`.
