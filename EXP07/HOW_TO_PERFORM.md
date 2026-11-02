# EXP07 - MLP Supervised Learning

## Ubuntu setup

Open Terminal and install Python and the required packages:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
cd /path/to/aisc/EXP07
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install numpy pandas scikit-learn
```

## `01_mlp_xor.py`

Run:

```bash
python 01_mlp_xor.py
```

The XOR training data is part of the experiment, so this program does not
request input. It prints actual and predicted outputs.

## `02_mlp_student_pass_fail.py`

Run:

```bash
python 02_mlp_student_pass_fail.py
```

Enter hours studied:

```text
Enter the number of hours studied: 6
```

The program prints the training accuracy and predicts `Pass` or `Fail`.

## `03_mlp_iris.py`

Place `iris.csv` in this folder with columns:

```text
SepalLength,SepalWidth,PetalLength,PetalWidth,Species
```

Run:

```bash
python 03_mlp_iris.py
```

After training, enter the number of flowers and four measurements per flower:

```text
Enter the number of flowers to predict: 2
Enter SepalLength SepalWidth PetalLength PetalWidth for flower 1: 5.1 3.5 1.4 0.2
Enter SepalLength SepalWidth PetalLength PetalWidth for flower 2: 6.5 3.0 5.5 1.8
```

The program prints test accuracy, a confusion matrix, and predictions.
