# EXP07

## How to perform

1. Open **Terminal** and change to this folder:

   ```bash
   cd /path/to/pracs/EXP07
   ```
2. Install Python and the dependencies once:

   ```bash
   sudo apt update
   sudo apt install -y python3 python3-pip python3-venv
   python3 -m venv .venv
   source .venv/bin/activate
   python3 -m pip install numpy matplotlib scikit-learn
   ```

3. Run the program:

   ```bash
   python3 01_ebpta_student_performance.py
   ```

Use Python 3.10 or newer.

## Programs

- `01_ebpta_student_performance.py` - **EBPTA Student Performance Prediction**: Train a 2-3-1 sigmoid network to predict Pass or Fail.

## Practical procedure

1. State the aim and explain the algorithm or learning rule.
2. Explain the important inputs, parameters and expected output.
3. Execute the selected file and show the result.
4. For a changed input, update the constants near the top of the file and run it again.
