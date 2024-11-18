import tkinter as tk
from time import strftime

def update_clock():
    clock_label.config(text=strftime("%H:%M:%S"))
    clock_label.after(1000, update_clock)

root = tk.Tk()
root.title("Đồng Hồ")

clock_label = tk.Label(root, font=("Arial", 48))
clock_label.pack()

update_clock()
root.mainloop()
