# Program untuk menjumlahkan dua bilangan integer
a = int(input("Masukkan bilangan bulat pertama: "))  # Input sebagai integer
b = int(input("Masukkan bilangan bulat kedua: "))   # Input sebagai integer
jumlah = a + b  # Operasi penjumlahan menggunakan integer
print(f"Jumlah dari {a} + {b} = {jumlah}")  # Output hasil

print ("==SETELAH DI MODIFIKASI==")

import tkinter as tk

# Fungsi untuk menambahkan nilai ke display
def append_to_display(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

# Fungsi untuk menghapus display
def clear_display():
    display.delete(0, tk.END)

# Fungsi untuk menghitung hasil
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Sederhana Berwarna")
root.geometry("300x400")
root.configure(bg="#e0f7fa")  # Latar belakang biru muda

# Display (layar hitam dengan teks putih)
display = tk.Entry(root, font=("Arial", 24), bg="#000000", fg="#ffffff", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Tombol-tombol
buttons = [
    ("C", 1, 0, "#f44336", clear_display),  # Merah
    ("/", 1, 1, "#ff9800", lambda: append_to_display("/")),  # Oranye
    ("*", 1, 2, "#ff9800", lambda: append_to_display("*")),  # Oranye
    ("-", 1, 3, "#ff9800", lambda: append_to_display("-")),  # Oranye
    ("7", 2, 0, "#4caf50", lambda: append_to_display("7")),  # Hijau
    ("8", 2, 1, "#4caf50", lambda: append_to_display("8")),  # Hijau
    ("9", 2, 2, "#4caf50", lambda: append_to_display("9")),  # Hijau
    ("+", 2, 3, "#ff9800", lambda: append_to_display("+")),  # Oranye
    ("4", 3, 0, "#4caf50", lambda: append_to_display("4")),  # Hijau
    ("5", 3, 1, "#4caf50", lambda: append_to_display("5")),  # Hijau
    ("6", 3, 2, "#4caf50", lambda: append_to_display("6")),  # Hijau
    ("=", 3, 3, "#2196f3", calculate),  # Biru, span 2 baris
    ("1", 4, 0, "#4caf50", lambda: append_to_display("1")),  # Hijau
    ("2", 4, 1, "#4caf50", lambda: append_to_display("2")),  # Hijau
    ("3", 4, 2, "#4caf50", lambda: append_to_display("3")),  # Hijau
    ("0", 5, 0, "#4caf50", lambda: append_to_display("0")),  # Hijau
    (".", 5, 1, "#4caf50", lambda: append_to_display(".")),  # Hijau
]

# Membuat tombol
for text, row, col, color, command in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 18), bg=color, fg="white", command=command)
        btn.grid(row=row, column=col, rowspan=2, sticky="nsew", padx=5, pady=5)  # Span 2 baris
    else:
        btn = tk.Button(root, text=text, font=("Arial", 18), bg=color, fg="white", command=command)
        btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Mengatur grid agar responsif
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Jalankan aplikasi
root.mainloop()
