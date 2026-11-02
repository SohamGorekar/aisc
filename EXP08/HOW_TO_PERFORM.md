# EXP08 - EBPTA

## Ubuntu setup

Open Terminal and install Python and NumPy:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
cd /path/to/aisc/EXP08
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install numpy
```

## `01_ebpta_student_performance.py`

Run:

```bash
python 01_ebpta_student_performance.py
```

Enter hours studied, attendance percentage, and the expected target:

```text
Enter Hours Studied: 7
Enter Attendance (%): 85
Enter Expected Target (0 = Fail, 1 = Pass): 1
```

The program prints the prediction and whether it matches the expected target.

## `02_ebpta_assignment_marks.py`

Run:

```bash
python 02_ebpta_assignment_marks.py
```

Enter hours, attendance percentage, and assignment marks percentage:

```text
Enter hours studied: 7
Enter attendance percentage: 85
Enter assignment marks percentage: 80
```

## `03_ebpta_learning_rate_01.py`

Run:

```bash
python 03_ebpta_learning_rate_01.py
```

This variant uses the fixed learning rate `0.1` and prints the training
results without requesting additional input.
