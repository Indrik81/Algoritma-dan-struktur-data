import tkinter as tk
from tkinter import ttk

# ----------------------------
#   DATA ARRAY 1 DIMENSI
# ----------------------------
kota_medan = [
    "Medan Kota", "Medan Tuntungan", "Medan Denai", "Medan Selayang",
    "Medan Johor", "Medan Amplas", "Medan Timur", "Medan Barat",
    "Medan Deli", "Medan Helvetia", "Medan Marelan", "Medan Labuhan",
    "Medan Polonia", "Medan Baru", "Medan Area", "Medan Petisah"
]

# ----------------------------
#   GUI TKINTER
# ----------------------------
root = tk.Tk()
root.title("Daftar Nama Kota di Medan")
root.geometry("500x450")
root.configure(bg="#1e1e2e")

title_label = tk.Label(root, text="📍 Daftar Kota/Kecamatan di Medan",
                       font=("Arial", 16, "bold"), fg="#89b4fa", bg="#1e1e2e")
title_label.pack(pady=15)

# FRAME LIST
frame = tk.Frame(root, bg="#313244", bd=3, relief="ridge")
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(frame, width=40, height=12, font=("Consolas", 12),
                     fg="#f5e0dc", bg="#45475a",
                     yscrollcommand=scrollbar.set)

for kota in kota_medan:
    listbox.insert(tk.END, f"• {kota}")

listbox.pack(side="left", fill="both")
scrollbar.config(command=listbox.yview)

# INPUT TAMBAHAN
input_label = tk.Label(root, text="Tambah Kota Baru:",
                       font=("Arial", 12, "bold"), fg="#cba6f7", bg="#1e1e2e")
input_label.pack(pady=5)

entry_kota = tk.Entry(root, width=30, font=("Arial", 12))
entry_kota.pack()

def tambah_kota():
    new_city = entry_kota.get()
    if new_city.strip():
        listbox.insert(tk.END, f"• {new_city}")
        entry_kota.delete(0, tk.END)

btn_add = tk.Button(root, text="Tambah", command=tambah_kota,
                    font=("Arial", 12, "bold"),
                    fg="white", bg="#74c7ec", activebackground="#89dceb")
btn_add.pack(pady=10)

root.mainloop()
