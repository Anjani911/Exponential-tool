# e Approximation Visualizer

This is a simple Python desktop GUI app that visualizes the exponential limit formula:

\[
(1 + \frac{1}{n})^n
\]

As `n → ∞`, the expression approaches Euler's number `e ≈ 2.71828`.

## 🔍 Features

- Interactive slider to select `n` (from 1 to 10,000)
- Real-time result display of `(1 + 1/n)^n`
- Live plot showing convergence toward `e`
- Clean and minimal GUI built using `tkinter` and `matplotlib`

## 📦 Requirements

- Python 3.x
- matplotlib
- numpy

Install dependencies:

```bash
pip install matplotlib numpy


Run
python e_approx_gui.py



While studying exponential functions, I came across a teaching tool demonstrating this formula with a slider. I built this GUI to better understand why we can't calculate e exactly, but can only approximate it as n increases.