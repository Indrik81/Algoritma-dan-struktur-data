import tkinter as tk
from tkinter import ttk

# ----------------------------
#   DATA ARRAY 2 DIMENSI
# ----------------------------
# Format: [Nama Kota/Kecamatan, Jumlah Penduduk (contoh data)]
data_kota = [
    ["Medan Kota", "122.000"],
    ["Medan Denai", "145.000"],
    ["Medan Tuntungan", "98.500"],
    ["Medan Amplas", "110.200"],
    ["Medan Selayang", "87.300"],
    ["Medan Deli", "133.400"],
    ["Medan Helvetia", "120.550"],
]

# ----------------------------
#            GUI
# ----------------------------
root = tk.Tk()
root.title("Daftar Kota di Medan (Array 2 Dimensi)")
root.geometry("600x450")
root.configure(bg="#1e1e2e")


title_label = tk.Label(
    root,
    text="📍 Daftar Kota / Kecamatan di Medan",
    font=("Arial", 18, "bold"),
    fg="#89b4fa",
    bg="#1e1e2e"
)
title_label.pack(pady=15)


# FRAME TABEL
frame = tk.Frame(root, bg="#313244", bd=3, relief="ridge")
frame.pack(pady=10, padx=10)

# STYLE TREEVIEW
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="#45475a",
                foreground="#f5e0dc",
                rowheight=30,
                fieldbackground="#45475a",
                font=("Consolas", 12))
style.configure("Treeview.Heading",
                background="#89b4fa",
                foreground="black",
                font=("Arial", 12, "bold"))
style.map("Treeview",
          background=[("selected", "#74c7ec")])

# TABLE
table = ttk.Treeview(frame, columns=("kota", "penduduk"), show="headings")
table.column("kota", width=250)
table.column("penduduk", width=150)

table.heading("kota", text="Nama Kota / Kecamatan")
table.heading("penduduk", text="Jumlah Penduduk")

# Memasukkan data ke tabel
for row in data_kota:
    table.insert("", tk.END, values=row)

table.pack(fill="both")


# ----------------------------
#      INPUT TAMBAHAN
# ----------------------------
input_frame = tk.Frame(root, bg="#1e1e2e")
input_frame.pack(pady=10)

lbl1 = tk.Label(input_frame, text="Nama Kota:", font=("Arial", 12), fg="#cba6f7", bg="#1e1e2e")
lbl1.grid(row=0, column=0, padx=5)

entry_kota = tk.Entry(input_frame, font=("Arial", 12), width=22)
entry_kota.grid(row=0, column=1, padx=5)

lbl2 = tk.Label(input_frame, text="Penduduk:", font=("Arial", 12), fg="#cba6f7", bg="#1e1e2e")
lbl2.grid(row=1, column=0, padx=5, pady=5)

entry_pdd = tk.Entry(input_frame, font=("Arial", 12), width=22)
entry_pdd.grid(row=1, column=1, pady=5)

def tambah_data():
    kota = entry_kota.get()
    pdd = entry_pdd.get()
    if kota.strip() and pdd.strip():
        table.insert("", tk.END, values=[kota, pdd])
        entry_kota.delete(0, tk.END)
        entry_pdd.delete(0, tk.END)

btn_add = tk.Button(
    root,
    text="Tambah Data",
    command=tambah_data,
    font=("Arial", 12, "bold"),
    bg="#74c7ec",
    fg="black",
    activebackground="#89dceb",
    width=15
)
btn_add.pack(pady=10)

root.mainloop()
