import tkinter as tk
from math import pow

def calculate_e(n):
    try:
        n = int(n)
        result = pow((1 + 1/n), n)
        result_label.config(text=f"(1 + 1/{n})^{n} = {result:.10f}")
    except ZeroDivisionError:
        result_label.config(text="Cannot divide by zero!")

root = tk.Tk()
root.title("e Approximation Visualizer")   

slider = tk.Scale(root, from_=1, to=10000, orient=tk.HORIZONTAL, label="Choose n", command=calculate_e)
slider.pack(pady=20)

result_label = tk.Label(root, text="Move the slider to calculate", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()