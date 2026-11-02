# EXP05 - Predicate Logic

## Ubuntu setup

Open Terminal and install Python:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
cd /path/to/aisc/EXP05
python3 -m venv .venv
source .venv/bin/activate
```

These programs use only the Python standard library. Run each program with
`python3` from this folder.

## Programs

### `01_predicate_logic_library.py`

Run:

```bash
python 01_predicate_logic_library.py
```

This program demonstrates library predicates and queries using its built-in
knowledge base. It does not request runtime input.

### `AISC_EXP5.PY`

Run:

```bash
python AISC_EXP5.PY
```

Use the menu:

```text
1 Add Member
2 Add Book
3 Borrow Book
4 Return Book
5 Check Book Availability
6 Find Book Author
7 Show Borrowed Books
8 FOL Query
9 Display Knowledge Base
10 Expire Membership
11 Run Inference
12 Exit
```

Names and book titles are entered when the selected operation asks for them.
For an FOL query, enter a predicate such as `Member`, `Book`, `Available`,
`Borrower`, `MembershipExpired`, or `BorrowingLimitExceeded`, followed by its
value.

### `AISC_EXC5.1.PY`

Run:

```bash
python AISC_EXC5.1.PY
```

Use the displayed library menu and enter names, titles, authors, predicates,
and values as requested. This is the extended library exercise.

### `AISC_EXC5.2.PY`

Run:

```bash
python AISC_EXC5.2.PY
```

Use the hospital menu. When adding or updating a patient, enter `yes` or
`no` for fever, cough, and insurance, and enter a numeric age. FOL queries
include `Patient`, `Fever`, `Cough`, `Insurance`, `SeniorCitizen`, `Flu`, and
`PriorityTreatment`.
