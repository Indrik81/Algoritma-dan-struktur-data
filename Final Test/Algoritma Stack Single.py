import tkinter as tk
from tkinter import messagebox

# ==========================
#      CLASS STACK
# ==========================
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def clear(self):
        self.items = []

    def get_stack(self):
        return self.items


# ==========================
#      GUI APLIKASI
# ==========================
app = tk.Tk()
app.title("Algoritma Stack - Tkinter")
app.geometry("430x430")
app.configure(bg="#eef2ff")

stack = Stack()

# --------------------------
#   FRAME UTAMA (CARD)
# --------------------------
frame = tk.Frame(app, bg="white", bd=2, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center", width=360, height=360)

title = tk.Label(frame, text="STACK SINGLE", font=("Arial", 16, "bold"),
                 bg="white", fg="#4a4aff")
title.pack(pady=10)

# --------------------------
#     INPUT DATA
# --------------------------
entry = tk.Entry(frame, font=("Arial", 14), justify="center", bd=2, relief="solid")
entry.pack(pady=10)

# --------------------------
#    UPDATE TAMPILAN STACK
# --------------------------
def update_stack_view():
    listbox.delete(0, tk.END)
    for item in reversed(stack.get_stack()):
        listbox.insert(tk.END, item)

# --------------------------
#        FUNGSI PUSH
# --------------------------
def push_item():
    data = entry.get().strip()
    if data == "":
        messagebox.showwarning("Peringatan", "Input tidak boleh kosong!")
        return
    stack.push(data)
    update_stack_view()
    entry.delete(0, tk.END)

# --------------------------
#        FUNGSI POP
# --------------------------
def pop_item():
    removed = stack.pop()
    if removed is None:
        messagebox.showinfo("Stack Kosong", "Tidak ada data yang bisa di-pop.")
    else:
        messagebox.showinfo("Data Terhapus", f"Data '{removed}' berhasil di-pop.")
    update_stack_view()

# --------------------------
#        FUNGSI RESET
# --------------------------
def reset_stack():
    stack.clear()
    update_stack_view()

# --------------------------
#       TOMBOL-TOMBOL
# --------------------------
btn_frame = tk.Frame(frame, bg="white")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="PUSH", font=("Arial", 12, "bold"),
          bg="#4a4aff", fg="white", width=8, command=push_item).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="POP", font=("Arial", 12, "bold"),
          bg="#ff4a4a", fg="white", width=8, command=pop_item).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="RESET", font=("Arial", 12, "bold"),
          bg="#ffaa00", fg="white", width=8, command=reset_stack).grid(row=0, column=2, padx=5)

# --------------------------
#     LISTBOX STACK VIEW
# --------------------------
listbox = tk.Listbox(frame, font=("Arial", 12), height=8, width=25,
                     bd=2, relief="solid", justify="center")
listbox.pack(pady=10)

# Start GUI
app.mainloop()
