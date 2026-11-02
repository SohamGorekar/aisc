# EXP02

## How to perform

1. Open **Terminal** and change to this folder:

   ```bash
   cd /path/to/pracs/EXP02
   ```
2. Install Python and the dependencies once:

   ```bash
   sudo apt update
   sudo apt install -y python3 python3-pip python3-venv
   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install numpy matplotlib scikit-learn
   ```

3. Run any program, for example:

   ```bash
   python3 01_fifteen_puzzle_astar.py
   ```

Use Python 3.10 or newer.

## Programs

- `01_fifteen_puzzle_astar.py` - **15-Puzzle using A***: Use Manhattan distance with A* to solve a 15-puzzle.
- `02_water_jug_astar.py` - **Water Jug using A***: Measure 2 litres with 4-litre and 3-litre jugs using A*.
- `03_eight_queens_astar.py` - **8-Queen using A***: Use A* to find a valid 8-Queen placement.

## Practical procedure

1. State the aim and explain the algorithm or learning rule.
2. Explain the important inputs, parameters and expected output.
3. Execute the selected file and show the result.
4. For a changed input, update the constants near the top of the file and run it again.
