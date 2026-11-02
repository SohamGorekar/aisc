# EXP10 - Fuzzy Washing Machine

## Ubuntu setup

Open Terminal and install Python, NumPy, and Matplotlib:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
cd /path/to/aisc/EXP10
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install numpy matplotlib
```

## `01_fuzzy_washing_machine.py`

Run:

```bash
python 01_fuzzy_washing_machine.py
```

Enter dirt and grease percentages from 0 to 100:

```text
Enter dirt percentage (0-100): 45
Enter grease percentage (0-100): 65
```

The program prints membership values, activated rules, and the recommended
wash time. It also opens membership and aggregated-output plots.

## `02_fuzzy_washing_machine_fabric.py`

Run:

```bash
python 02_fuzzy_washing_machine_fabric.py
```

Enter dirt percentage, grease percentage, and one fabric type:

```text
Enter dirt percentage (0-100): 45
Enter grease percentage (0-100): 65
Enter fabric type (delicate/normal/heavy): heavy
```

Valid fabric values are `delicate`, `normal`, and `heavy`.

## `03_fuzzy_washing_machine_temperature.py`

Run:

```bash
python 03_fuzzy_washing_machine_temperature.py
```

Enter dirt and grease percentages:

```text
Enter dirt percentage (0-100): 45
Enter grease percentage (0-100): 65
```

The program recommends both wash time and water temperature.
