# Bisection Method Solver

A Python implementation of the **Bisection Method** for finding roots of continuous functions, provided in two versions:
- **Console version** (`Bisection method.py`) — Simple command-line interface
- **GUI version** (`gui.py`) — Full-featured graphical interface with plotting and export capabilities

---

## Overview

The **Bisection Method** is a numerical root-finding algorithm that repeatedly bisects an interval and selects a subinterval in which a root must lie. It requires:
- A continuous function `f(x)`
- An interval `[a, b]` where `f(a) * f(b) < 0` (the function changes sign)

The method guarantees convergence to a root if the initial condition is satisfied.

---

## Files

| File | Description |
|------|-------------|
| `Bisection method.py` | Minimal console-based implementation |
| `gui.py` | Feature-rich Tkinter GUI with plotting, export, and enhanced precision options |

---

## Quick Start

### Console Version
```bash
python "Bisection method.py"
```

### GUI Version
```bash
python gui.py
```

> **Requirements**: Python 3.x with standard library (GUI version requires `matplotlib` for plotting: `pip install matplotlib`)

---

## Console Version (`Bisection method.py`)

### Features
- Interactive input for function, interval bounds, and tolerance
- Iteration table showing: iteration number, `a`, `b`, midpoint `c`, and `f(c)`
- Fixed tolerance: `ε = 0.0001`
- Stops when `|f(c)| < ε`

### Usage Example
```
Enter the function f(x): math.sin(x) - x/2
Enter a: 1
Enter b: 2

Iteration      a            b            c            f(c)
---------------------------------------------------------------
1               1.0          2.0          1.5          -0.239713
2               1.0          1.5          1.25         0.110364
3               1.25         1.5          1.375        -0.068414
...
```

### Supported Functions
Use standard Python `math` module functions:
- `math.sin(x)`, `math.cos(x)`, `math.tan(x)`
- `math.exp(x)`, `math.log(x)`, `math.sqrt(x)`
- `x**2`, `x**3`, etc. (power operator)
- Constants: `math.pi`, `math.e`

---

## GUI Version (`gui.py`)

### Features

#### Input Parameters
- **Function entry** — Enter any valid Python expression using `x` as variable
- **Interval [a, b]** — Lower and upper bounds
- **Precision Settings**:
  - **Absolute Error** — Stop when `|f(c)| < ε` or interval size `< ε`
  - **Relative Error** — Stop when `|cₙ - cₙ₋₁| / |cₙ| < ε`
- **Tolerance (ε)** — Default: `1e-8`
- **Max Iterations** — Default: `100`

#### Built-in Examples
- `math.sin(x) - x/2`
- `x**3 - 2*x - 5`
- `math.exp(-x) - x`
- `math.cos(x) - x`

#### Output Displays
1. **Statistics Panel** — Root value, iterations, absolute error, final interval, `f(root)`
2. **Iteration Table** — Columns: Iter, a, b, c, f(c), Error, Interval Size (12-decimal precision)
3. **Detailed Console** — Full calculation log with headers and final results

#### Buttons
| Button | Action |
|--------|--------|
| **Calculate Root** | Runs bisection method with current inputs |
| **Clear Results** | Resets all outputs |
| **Plot Function** | Opens matplotlib window with function plot and root visualization |
| **Export Results** | Saves complete results (inputs, statistics, iteration table) to `.txt` file |

#### Plotting Features
- **Main plot**: Function curve, interval bounds, shaded search interval, root marker
- **Zoomed plot**: Detailed view around the found root with tolerance band
- Requires `matplotlib` and `numpy`

#### Export Format
```
============================================================
BISECTION METHOD RESULTS
============================================================
Function: f(x) = math.sin(x) - x/2
Interval: [1.0, 2.0]
Tolerance: 1e-8
Tolerance type: absolute

FINAL RESULTS:
Approximate root: 1.895494267033981
Iterations: 27
Absolute error: 1.23e-09
Final interval: [1.895494, 1.895494]
f(root): 1.23e-09

ITERATION HISTORY:
----------------------------------------------------------------------------------------------------
Iter    a    b    c    f(c)    Error    Interval Size
----------------------------------------------------------------------------------------------------
1    1.000000000000    2.000000000000    1.500000000000    -2.40e-01    2.40e-01    1.00e+00
...
```

---

## Algorithm Details

### Bisection Method
Given `f(x)` continuous on `[a, b]` with `f(a) * f(b) < 0`:

1. Compute midpoint: `c = (a + b) / 2`
2. Evaluate `f(c)`
3. If `|f(c)| < ε` (or other stopping criterion): **stop**, `c` is the approximate root
4. If `f(a) * f(c) < 0`: root in `[a, c]` → set `b = c`
5. Else: root in `[c, b]` → set `a = c`
6. Repeat from step 1

### Stopping Criteria (GUI)
| Type | Condition |
|------|-----------|
| Absolute Error | `|f(c)| < ε` **or** `interval_size < ε` |
| Relative Error | `|cₙ - cₙ₋₁| / |cₙ| < ε` (after iteration 1) |
| Exact Root | `f(c) == 0` |
| Max Iterations | Iteration count reaches limit |

### Convergence
- **Guaranteed** if `f(a) * f(b) < 0` and `f` is continuous
- **Linear convergence** — error halves each iteration
- **Number of iterations** for tolerance `ε`: `n ≥ log₂((b-a)/ε)`

---

## Requirements

| Component | Console | GUI |
|-----------|---------|-----|
| Python | 3.x | 3.x |
| Standard Library | `math` | `tkinter`, `math` |
| Optional | — | `matplotlib`, `numpy` (for plotting) |

Install optional dependencies:
```bash
pip install matplotlib numpy
```

---

## Safety Notes

Both versions use `eval()` with a restricted namespace (`{"__builtins__": {}}`) containing only the `math` module and variable `x`. This limits but does not eliminate code execution risk. **Do not use with untrusted input.**

---

## License

This project is provided as-is for educational and practical use.