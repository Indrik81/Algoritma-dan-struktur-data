import tkinter as tk
from tkinter import ttk

# ----------------------------
#   DATA ARRAY 3 DIMENSI
# ----------------------------
# Format:
# [
#   [ [Nama Kota, Jumlah Penduduk, Jumlah Kabupaten], ... ],
#   ...
# ]

data_kota_3d = [
    [   # Cluster 1 (Medan Pusat)
        ["Medan Kota", "122.000", "5"],
        ["Medan Denai", "145.000", "4"]
    ],
    [   # Cluster 2 (Medan Utara)
        ["Medan Marelan", "158.200", "6"],
        ["Medan Deli", "133.400", "5"]
    ],
    [   # Cluster 3 (Medan Selatan)
        ["Medan Johor", "140.300", "5"],
        ["Medan Amplas", "110.200", "3"]
    ]
]

# ----------------------------
#            GUI
# ----------------------------
root = tk.Tk()
root.title("Daftar Kota di Medan (Array 3 Dimensi + Kabupaten)")
root.geometry("700x520")
root.configure(bg="#1e1e2e")

title_label = tk.Label(
    root,
    text="📍 Daftar Kota / Kecamatan di Medan (3D Array)",
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
table = ttk.Treeview(frame, columns=("kota", "penduduk", "kabupaten"), show="headings")
table.column("kota", width=250)
table.column("penduduk", width=150)
table.column("kabupaten", width=150)

table.heading("kota", text="Nama Kota / Kecamatan")
table.heading("penduduk", text="Jumlah Penduduk")
table.heading("kabupaten", text="Jumlah Kabupaten")

table.pack(fill="both")

# -------------------------------------
# Memasukkan isi ARRAY 3 DIMENSI ke tabel
# -------------------------------------
for cluster in data_kota_3d:
    for row in cluster:
        table.insert("", tk.END, values=row)

# ----------------------------
#      INPUT TAMBAHAN
# ----------------------------
input_frame = tk.Frame(root, bg="#1e1e2e")
input_frame.pack(pady=10)

# Input Kota
lbl1 = tk.Label(input_frame, text="Nama Kota:", font=("Arial", 12), fg="#cba6f7", bg="#1e1e2e")
lbl1.grid(row=0, column=0, padx=5)

entry_kota = tk.Entry(input_frame, font=("Arial", 12), width=22)
entry_kota.grid(row=0, column=1, padx=5)

# Input Penduduk
lbl2 = tk.Label(input_frame, text="Penduduk:", font=("Arial", 12), fg="#cba6f7", bg="#1e1e2e")
lbl2.grid(row=1, column=0, padx=5, pady=5)

entry_pdd = tk.Entry(input_frame, font=("Arial", 12), width=22)
entry_pdd.grid(row=1, column=1, pady=5)

# Input Kabupaten
lbl3 = tk.Label(input_frame, text="Jumlah Kabupaten:", font=("Arial", 12), fg="#cba6f7", bg="#1e1e2e")
lbl3.grid(row=2, column=0, padx=5, pady=5)

entry_kab = tk.Entry(input_frame, font=("Arial", 12), width=22)
entry_kab.grid(row=2, column=1, pady=5)

def tambah_data():
    kota = entry_kota.get()
    pdd = entry_pdd.get()
    kab = entry_kab.get()

    if kota.strip() and pdd.strip() and kab.strip():
        # Masukkan ke cluster pertama
        data_kota_3d[0].append([kota, pdd, kab])
        table.insert("", tk.END, values=[kota, pdd, kab])

        entry_kota.delete(0, tk.END)
        entry_pdd.delete(0, tk.END)
        entry_kab.delete(0, tk.END)

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
