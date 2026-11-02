# EXP06 - Kohonen Self-Organizing Map

## Ubuntu setup

Open Terminal and install Python and NumPy:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
cd /path/to/aisc/EXP06
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install numpy
```

## `01_kohonen_som.py`

Run:

```bash
python 01_kohonen_som.py
```

Enter two initial weights and one or more input values:

```text
Enter 2 initial weights separated by spaces: 0.3 0.8
Enter input values separated by spaces: 0.35 0.40 0.45 0.75 0.80 0.90
```

The program prints the winner neuron and updated weights after each input.

## `02_kohonen_som_three_neurons.py`

Run:

```bash
python 02_kohonen_som_three_neurons.py
```

Enter three initial weights and one or more input values:

```text
Enter 3 initial weights separated by spaces: 0.2 0.5 0.8
Enter input values separated by spaces: 0.15 0.25 0.45 0.55 0.75 0.90
```
