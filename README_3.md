# 🧮 Smart Calculator

A feature-rich command-line calculator built in Python with basic arithmetic, scientific functions, calculation history, and full error handling.

---

## Features

- **Basic Arithmetic** — Addition, Subtraction, Multiplication, Division, Modulus, Power
- **Scientific Functions** — Square Root, Factorial, Logarithm, Sin, Cos, Tan, Absolute Value
- **Calculation History** — View all previous calculations with numbering, option to clear history
- **Error Handling** — Handles invalid inputs, division by zero, negative square roots, and more
- **Clean Results** — Rounded to 6 decimal places to avoid floating point clutter

---

## How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
python Smart_Calculator_with_error_handling.py
```

---

## Usage

```
--------------------------------------------------
         Welcome to Smart Calculator
--------------------------------------------------
1. Basic Arithmetic (+, -, *, /, %, **)
2. Scientific Functions (sqrt, factorial, log, sin, cos, tan, abs)
3. View Calculation History
4. Exit
```

**Basic Arithmetic Example:**
```
Enter number 1: 10
Enter number 2: 3
Enter operator: **
10.0 ** 3.0 = 1000.0
```

**Scientific Example:**
```
Enter your choice: 1  (Square Root)
Enter number: 144
√144.0 = 12.0
```

**History Example:**
```
Calculation History:
1. 10.0 ** 3.0 = 1000.0
2. √144.0 = 12.0

Clear history? (y/n):
```

---

## Concepts Used

- Functions and modular code structure
- Dictionary-based operator mapping
- `math` and `operator` modules
- Exception handling (`try/except`)
- Loops and user input validation
- List operations for history tracking

---

## What I Learned

Built as part of my Python learning journey. This project helped me practice structuring a multi-feature program, using Python's built-in modules, and writing robust error handling for real user input scenarios.

---

## Author

**Your Name**  
[GitHub Profile](https://github.com/yourusername)
