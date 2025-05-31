import tkinter as tk
from math import pow

def calculate_e(n):
    try:
        n = int(n)
        result = pow((1 + 1/n), n)
        result_label.config(text=f"(1 + 1/{n})^{n} = {result:.10f}")
    except ZeroDivisionError:
        result_label.config(text="Cannot divide by zero!")