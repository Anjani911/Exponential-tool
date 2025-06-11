import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def calculate_e(n):
    try:
        n = int(float(n))
        result = pow((1 + 1/n), n)
        result_label.config(text=f"(1 + 1/{n})^{n} = {result:.10f}")

        
        update_plot(n)

    except ZeroDivisionError:
        result_label.config(text="Cannot divide by zero!")

def update_plot(current_n):
    n_vals = np.linspace(1, current_n, 200)
    y_vals = [(1 + 1/n)**n for n in n_vals]

    ax.clear()
    ax.plot(n_vals, y_vals, label="(1 + 1/n)^n", color="blue")
    ax.axhline(y=np.e, color="red", linestyle="--", label="e ≈ 2.71828")
    ax.set_title("Convergence of (1 + 1/n)^n → e")
    ax.set_xlabel("n")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid(True)
    canvas.draw()


root = tk.Tk()
root.title("e Approximation Visualizer")
root.geometry("800x600")
root.configure(bg="#f7f7f7")


style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14), background="#f7f7f7")


ttk.Label(root, text="Choose n (1 to 10,000):").pack(pady=10)
slider = ttk.Scale(root, from_=1, to=10000, orient=tk.HORIZONTAL, command=calculate_e)
slider.pack(fill="x", padx=20)


result_label = ttk.Label(root, text="", font=("Courier", 14))
result_label.pack(pady=10)


fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(pady=10)


root.mainloop()