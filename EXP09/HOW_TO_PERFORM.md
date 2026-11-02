# EXP09 - Fuzzy Membership Functions

## Ubuntu setup

Open Terminal and install Python, NumPy, and Matplotlib:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
cd /path/to/aisc/EXP09
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install numpy matplotlib
```

## `01_temperature_fuzzy_membership.py`

Run:

```bash
python 01_temperature_fuzzy_membership.py
```

Enter one room temperature in Celsius:

```text
Enter a room temperature in Celsius: 22
```

The program prints triangular, trapezoidal, and Gaussian membership values
for that temperature, then opens the comparison plot.

## `02_attendance_fuzzy_membership.py`

Run:

```bash
python 02_attendance_fuzzy_membership.py
```

Enter attendance values separated by spaces:

```text
Enter attendance values to evaluate, separated by spaces (default: 40 50 60 70 80 90): 40 50 60 70 80 90
```

Press Enter without values to use the default six values. The program prints
Low, Moderate, and High membership values for all three function types and
opens comparison plots.
