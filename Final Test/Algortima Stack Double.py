import tkinter as tk
from tkinter import messagebox


# =======================================================
#                KELAS DOUBLE STACK
# =======================================================
class DoubleStack:
    def __init__(self, size=10):
        self.size = size
        self.data = [None] * size
        self.topA = -1
        self.topB = size

    def pushA(self, value):
        if self.topA + 1 == self.topB:
            return False
        self.topA += 1
        self.data[self.topA] = value
        return True

    def pushB(self, value):
        if self.topB - 1 == self.topA:
            return False
        self.topB -= 1
        self.data[self.topB] = value
        return True

    def popA(self):
        if self.topA == -1:
            return None
        item = self.data[self.topA]
        self.data[self.topA] = None
        self.topA -= 1
        return item

    def popB(self):
        if self.topB == self.size:
            return None
        item = self.data[self.topB]
        self.data[self.topB] = None
        self.topB += 1
        return item

    def getA(self):
        return [x for x in self.data[: self.topA + 1] if x is not None]

    def getB(self):
        return [x for x in reversed(self.data[self.topB:]) if x is not None]


# =======================================================
#                 TKINTER GUI SETUP
# =======================================================
app = tk.Tk()
app.title("Double Stack Tkinter + History List")
app.geometry("800x550")
app.configure(bg="#e8eafe")

stack = DoubleStack(size=10)

history = []   # <= HISTORY LIST SEDERHANA


# =======================================================
#                CREATE WIDGETS
# =======================================================
title = tk.Label(app, text="DOUBLE STACK + HISTORY LIST",
                 font=("Arial", 22, "bold"),
                 bg="#e8eafe", fg="#3a3aff")
title.pack(pady=10)

main_frame = tk.Frame(app, bg="white", bd=3, relief="ridge")
main_frame.pack(pady=10, padx=10, fill="x")

entry = tk.Entry(app, font=("Arial", 14), width=25, justify="center")
entry.pack(pady=10)

btn_frame = tk.Frame(app, bg="#e8eafe")
btn_frame.pack(pady=5)

btn_pushA = tk.Button(btn_frame, text="Push A", width=12, font=("Arial", 12, "bold"),
                      bg="#4a90e2", fg="white")
btn_pushA.grid(row=0, column=0, padx=10)

btn_pushB = tk.Button(btn_frame, text="Push B", width=12, font=("Arial", 12, "bold"),
                      bg="#f5a623", fg="white")
btn_pushB.grid(row=0, column=1, padx=10)

btn_popA = tk.Button(btn_frame, text="Pop A", width=12, font=("Arial", 12, "bold"),
                     bg="#d0021b", fg="white")
btn_popA.grid(row=1, column=0, padx=10, pady=5)

btn_popB = tk.Button(btn_frame, text="Pop B", width=12, font=("Arial", 12, "bold"),
                     bg="#7ed321", fg="white")
btn_popB.grid(row=1, column=1, padx=10, pady=5)

# DISPLAY STACK
labelA = tk.Label(main_frame, text="STACK A", font=("Arial", 12, "bold"),
                  bg="white", fg="#4a90e2")
labelA.grid(row=0, column=0, pady=5)

labelB = tk.Label(main_frame, text="STACK B", font=("Arial", 12, "bold"),
                  bg="white", fg="#f5a623")
labelB.grid(row=0, column=1, pady=5)

listA = tk.Listbox(main_frame, width=20, height=10, font=("Arial", 12), bd=2, relief="solid")
listA.grid(row=1, column=0, padx=10, pady=5)

listB = tk.Listbox(main_frame, width=20, height=10, font=("Arial", 12), bd=2, relief="solid")
listB.grid(row=1, column=1, padx=10, pady=5)

# HISTORY FRAME
hist_frame = tk.Frame(app, bg="white", bd=3, relief="ridge")
hist_frame.pack(pady=10, fill="both")

tk.Label(hist_frame, text="History Push (Seperti List)",
         font=("Arial", 14, "bold"),
         bg="white", fg="#3a3aff").pack(pady=5)

hist = tk.Listbox(hist_frame, width=80, height=10, font=("Arial", 12),
                  bd=2, relief="solid")
hist.pack(padx=10, pady=5)


# =======================================================
#                UPDATE TAMPILAN STACK
# =======================================================
def update_view():
    # Stack A
    listA.delete(0, tk.END)
    for item in reversed(stack.getA()):
        listA.insert(tk.END, item)

    # Stack B
    listB.delete(0, tk.END)
    for item in reversed(stack.getB()):
        listB.insert(tk.END, item)

    # History list
    hist.delete(0, tk.END)
    for item in history:
        hist.insert(tk.END, item)


# =======================================================
#                FUNGSI PUSH / POP
# =======================================================
def push_A():
    val = entry.get().strip()
    if val == "":
        messagebox.showwarning("Warning", "Input tidak boleh kosong")
        return

    if stack.pushA(val):
        history.append(val)     # Tambah ke list
    else:
        messagebox.showerror("Overflow", "Stack A penuh!")

    update_view()
    entry.delete(0, tk.END)


def push_B():
    val = entry.get().strip()
    if val == "":
        messagebox.showwarning("Warning", "Input tidak boleh kosong")
        return

    if stack.pushB(val):
        history.append(val)     # Tambah ke list
    else:
        messagebox.showerror("Overflow", "Stack B penuh!")

    update_view()
    entry.delete(0, tk.END)


def pop_A():
    removed = stack.popA()
    if removed is None:
        messagebox.showerror("Underflow", "Stack A kosong!")
    else:
        messagebox.showinfo("POP A", f"Data '{removed}' dihapus dari Stack A")

        # Hapus dari history
        if history:
            history.pop()

    update_view()


def pop_B():
    removed = stack.popB()
    if removed is None:
        messagebox.showerror("Underflow", "Stack B kosong!")
    else:
        messagebox.showinfo("POP B", f"Data '{removed}' dihapus dari Stack B")

        # Hapus dari history
        if history:
            history.pop()

    update_view()


# Bind buttons
btn_pushA.config(command=push_A)
btn_pushB.config(command=push_B)
btn_popA.config(command=pop_A)
btn_popB.config(command=pop_B)

update_view()
app.mainloop()
