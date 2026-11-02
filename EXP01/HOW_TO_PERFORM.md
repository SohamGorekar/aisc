# EXP01

## How to perform

1. Open **Terminal** and change to this folder:

   ```bash
   cd /path/to/pracs/EXP01
   ```
2. Install Python and the dependencies once:

   ```bash
   sudo apt update
   sudo apt install -y python3 python3-pip python3-venv
   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install numpy matplotlib scikit-learn
   ```

3. Run any program:

   ```bash
   python3 01_eight_queens_uninformed.py
   ```

Use Python 3.10 or newer. Programs that display graphs open a Matplotlib
window; close it after examining the plots.

## Programs

- `01_eight_queens_uninformed.py` - **8-Queen Problem using uninformed search/backtracking**: Solve the 8-Queen problem by placing one queen per row without attacks.
- `02_tsp_dfs.py` - **Travelling Salesman Problem using DFS**: Enumerate all tours from city A and report the minimum-cost tour.

## Practical procedure

1. State the aim and explain the algorithm or learning rule.
2. Explain the important inputs, parameters and expected output.
3. Execute the selected file and show the result.
4. For a changed input, update the constants near the top of the file and run it again.
