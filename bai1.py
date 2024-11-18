import tkinter as tk

def on_button_click(button):
    if button == 'C':
        expression_var.set("")
        result_var.set("")
    elif button == '=':
        try:
            result = eval(expression_var.get())
            result_var.set(result)
        except:
            result_var.set("Error")
    else:
        expression_var.set(expression_var.get() + button)

def on_key_press(event):
    key = event.char
    if key in '0123456789+-*/.':
        expression_var.set(expression_var.get() + key)
    elif key == '\r':  # Enter key
        on_button_click('=')
    elif key == '\x08':  # Backspace key
        expression_var.set(expression_var.get()[:-1])

root = tk.Tk()
root.title("Máy Tính Ảo")

# Biến lưu trữ phép tính và kết quả
expression_var = tk.StringVar()
result_var = tk.StringVar()

# Khung nhập lớn hiển thị cả phép tính và kết quả
display_frame = tk.Frame(root, bd=10, relief="ridge")
display_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Nhãn hiển thị phép tính
expression_label = tk.Label(display_frame, textvariable=expression_var, font=('Arial', 20), anchor='e', bg="white", height=2, width=24)
expression_label.pack(fill='both')

# Nhãn hiển thị kết quả
result_label = tk.Label(display_frame, textvariable=result_var, font=('Arial', 24, 'bold'), anchor='e', bg="white", height=1, width=24)
result_label.pack(fill='both')

# Danh sách nút bấm
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Tạo các nút bấm
for i, button in enumerate(buttons):
    color = "white" if button.isdigit() or button == '0' else "orange"
    tk.Button(
        root, text=button, font=('Arial', 20), width=5, height=2, bg=color,
        command=lambda b=button: on_button_click(b)
    ).grid(row=1 + i // 4, column=i % 4, padx=5, pady=5)

# Bắt sự kiện bàn phím
root.bind('<Key>', on_key_press)

root.mainloop()
