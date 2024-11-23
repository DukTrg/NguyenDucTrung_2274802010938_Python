import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from db_connect import Database

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng Nhập")
        # self.root.geometry("300x200")
        self.username = "admin"
        self.password = "123"
        
        # Login Frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="Tên đăng nhập:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_username = tk.Entry(self.login_frame)
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.login_frame, text="Mật khẩu:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        self.login_button = tk.Button(self.login_frame, text="Đăng Nhập", command=self.check_login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def check_login(self):
        if self.entry_username.get() == self.username and self.entry_password.get() == self.password:
            messagebox.showinfo("Thành công", "Đăng nhập thành công!")
            self.login_frame.destroy()
            StudentManagerApp(self.root)
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")

class StudentManagerApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("Quản Lý Sinh Viên")

        self.create_widgets()
        self.populate_table()

    def create_widgets(self):
        # Frame for form inputs
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        tk.Label(self.frame, text="Mã:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_ma = tk.Entry(self.frame)
        self.entry_ma.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame, text="Họ:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_ho = tk.Entry(self.frame)
        self.entry_ho.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame, text="Tên:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_ten = tk.Entry(self.frame)
        self.entry_ten.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        tk.Button(self.button_frame, text="Thêm", command=self.add_record).grid(row=0, column=0, padx=5)
        tk.Button(self.button_frame, text="Sửa", command=self.update_record).grid(row=0, column=1, padx=5)
        tk.Button(self.button_frame, text="Xóa", command=self.delete_record).grid(row=0, column=2, padx=5)
        tk.Button(self.button_frame, text="Xem lại", command=self.populate_table).grid(row=0, column=3, padx=5)

        # Table to display records
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.pack(pady=10)

        self.columns = ("ma", "ho", "ten")
        self.tree = ttk.Treeview(self.tree_frame, columns=self.columns, show="headings")
        self.tree.heading("ma", text="Mã")
        self.tree.heading("ho", text="Họ")
        self.tree.heading("ten", text="Tên")
        self.tree.bind("<Double-1>", self.select_record)

        self.tree.pack()

    def populate_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in self.db.view():
            self.tree.insert("", tk.END, values=row)

    def add_record(self):
        try:
            ma = int(self.entry_ma.get())
            ho = self.entry_ho.get()
            ten = self.entry_ten.get()
            self.db.insert(ma, ho, ten)
            self.populate_table()
            self.clear_inputs()
        except Exception as e:
            messagebox.showerror("Error", f"Could not add record: {e}")

    def delete_record(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            ma = item['values'][0]
            self.db.delete(ma)
            self.populate_table()
        else:
            messagebox.showwarning("Warning", "Please select a record to delete")

    def update_record(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            ma = item['values'][0]
            try:
                ho = self.entry_ho.get()
                ten = self.entry_ten.get()
                self.db.update(ma, ho, ten)
                self.populate_table()
                self.clear_inputs()
            except Exception as e:
                messagebox.showerror("Error", f"Could not update record: {e}")
        else:
            messagebox.showwarning("Warning", "Please select a record to update")

    def select_record(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            self.entry_ma.delete(0, tk.END)
            self.entry_ho.delete(0, tk.END)
            self.entry_ten.delete(0, tk.END)
            self.entry_ma.insert(0, item['values'][0])
            self.entry_ho.insert(0, item['values'][1])
            self.entry_ten.insert(0, item['values'][2])

    def clear_inputs(self):
        self.entry_ma.delete(0, tk.END)
        self.entry_ho.delete(0, tk.END)
        self.entry_ten.delete(0, tk.END)

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
