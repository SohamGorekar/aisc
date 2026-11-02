# ADDITIONAL

## How to perform

1. Open **Terminal** and change to this folder:

   ```bash
   cd /path/to/pracs/ADDITIONAL
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
   python3 01_bfs.py
   ```

Use Python 3.10 or newer.

## Programs

- `01_bfs.py` - **Breadth First Search**: Traverse a graph level by level using a queue.
- `02_dfs.py` - **Depth First Search**: Traverse a graph depth-first using recursion.
- `03_water_jug_bfs.py` - **Water Jug using BFS**: Find the shortest 4-litre/3-litre jug solution using BFS.
- `04_hill_climbing.py` - **Hill Climbing Search**: Climb neighbouring values to reach the maximum of a function.
- `05_mcculloch_pitts.py` - **McCulloch-Pitts Neuron**: Implement AND and OR gates with fixed weights and thresholds.
- `06_perceptron_and.py` - **Perceptron Learning**: Learn the AND gate with the perceptron learning rule.
- `07_hebb_and_bipolar.py` - **Hebb Network**: Train a bipolar Hebb network for the AND gate.
- `08_fuzzy_set_operations.py` - **Fuzzy Set Operations**: Calculate union, intersection and complements of fuzzy sets.

## Practical procedure

1. State the aim and explain the algorithm or learning rule.
2. Explain the important inputs, parameters and expected output.
3. Execute the selected file and show the result.
4. For a changed input, update the constants near the top of the file and run it again.
