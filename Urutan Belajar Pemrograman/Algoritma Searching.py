# =============================================
#        PROGRAM PENCARIAN BUKU DI RAK
# =============================================

print("============================================")
print("        PROGRAM PENCARIAN BUKU")
print("============================================")

# Input jumlah buku di rak
jumlah = int(input("Masukkan jumlah buku di rak: "))

rak_buku = []

# Input judul buku
print("\n=== INPUT JUDUL BUKU ===")
for i in range(jumlah):
    judul = input(f"Masukkan judul buku ke-{i+1}: ")
    rak_buku.append(judul)

# Tampilkan semua buku
print("\n=== DAFTAR BUKU DI RAK ===")
for i in range(len(rak_buku)):
    print(f"[{i}] -> {rak_buku[i]}")

# Input buku yang ingin dicari
cari = input("\nMasukkan judul buku yang ingin dicari: ")

# Algoritma Searching
print("\n=== PROSES MENCARI BUKU ===")
ditemukan = False

for i in range(len(rak_buku)):
    print(f"Mengecek buku di index {i}: {rak_buku[i]}")
    if rak_buku[i].lower() == cari.lower():   # agar tidak sensitif huruf besar/kecil
        ditemukan = True
        posisi = i
        break

# Hasil
print("\n============================================")
if ditemukan:
    print(f"Buku DITEMUKAN! '{cari}' berada pada rak ke-{posisi}")
else:
    print(f"Buku '{cari}' TIDAK ADA di rak!")
print("============================================")

print ("==SETELAH DI MODIFIKASI==")

import tkinter as tk
from tkinter import messagebox

# ============================
# DATA RAK
# ============================
rak_buku = {
    "Rak 1": [],
    "Rak 2": [],
    "Rak 3": []
}

# ============================
# FUNGSI
# ============================

def tambah_buku():
    judul = entry_buku.get()
    rak = rak_var.get()

    if judul.strip() == "":
        messagebox.showwarning("Peringatan", "Judul buku tidak boleh kosong!")
        return

    rak_buku[rak].append(judul)
    update_listbox()
    entry_buku.delete(0, tk.END)

def update_listbox():
    listbox_rak1.delete(0, tk.END)
    for i in rak_buku["Rak 1"]:
        listbox_rak1.insert(tk.END, i)

    listbox_rak2.delete(0, tk.END)
    for i in rak_buku["Rak 2"]:
        listbox_rak2.insert(tk.END, i)

    listbox_rak3.delete(0, tk.END)
    for i in rak_buku["Rak 3"]:
        listbox_rak3.insert(tk.END, i)

def cari_buku():
    cari = entry_cari.get()

    if cari.strip() == "":
        messagebox.showwarning("Peringatan", "Masukkan judul buku!")
        return

    for rak in rak_buku:
        for i in range(len(rak_buku[rak])):
            if rak_buku[rak][i].lower() == cari.lower():
                messagebox.showinfo(
                    "Ditemukan!",
                    f"Buku '{cari}' ditemukan di {rak} pada posisi ke-{i}"
                )
                return

    messagebox.showerror("Tidak ditemukan", f"Buku '{cari}' tidak ada.")

# ============================
# GUI 3D “FIXED”
# ============================

window = tk.Tk()
window.title("Pencarian Buku Per Rak - 3D UI")
window.geometry("740x600")
window.configure(bg="#dfe6e9")

# Judul
title = tk.Label(window,
                 text="📚 SISTEM PENCARIAN BUKU PER RAK 📚",
                 bg="#74b9ff",
                 fg="white",
                 font=("Helvetica", 16, "bold"),
                 bd=4,
                 relief="ridge")
title.pack(fill="x", pady=10)

# Frame utama
main = tk.Frame(window, bg="#ffffff", bd=5, relief="ridge")
main.pack(fill="both", expand=True, padx=15, pady=10)

# ---------------------------------------
# INPUT BUKU
# ---------------------------------------
frame_input = tk.Frame(main, bg="#ecf0f1", bd=4, relief="groove")
frame_input.pack(padx=10, pady=10, fill="x")

tk.Label(frame_input, text="Masukkan Judul Buku:", bg="#ecf0f1", font=("Arial", 11)).pack()
entry_buku = tk.Entry(frame_input, width=40, font=("Arial", 11))
entry_buku.pack(pady=3)

tk.Label(frame_input, text="Pilih Rak:", bg="#ecf0f1", font=("Arial", 11)).pack()

rak_var = tk.StringVar(value="Rak 1")
tk.OptionMenu(frame_input, rak_var, "Rak 1", "Rak 2", "Rak 3").pack()

btn_tambah = tk.Button(frame_input,
                       text="Tambah Buku ke Rak",
                       bg="#55efc4",
                       font=("Arial", 11, "bold"),
                       relief="raised",
                       command=tambah_buku)
btn_tambah.pack(pady=7)

# ---------------------------------------
# 3 RAK (DISPLAY)
# ---------------------------------------
frame_rak = tk.Frame(main, bg="#ffffff")
frame_rak.pack(padx=10, pady=10)

# Rak 1
rak1 = tk.Frame(frame_rak, bg="#ffeaa7", bd=4, relief="ridge")
rak1.grid(row=0, column=0, padx=10)
tk.Label(rak1, text="Rak 1", bg="#ffeaa7", font=("Arial", 12, "bold")).pack()
listbox_rak1 = tk.Listbox(rak1, width=23, height=10, bd=4, relief="sunken")
listbox_rak1.pack()

# Rak 2
rak2 = tk.Frame(frame_rak, bg="#fab1a0", bd=4, relief="ridge")
rak2.grid(row=0, column=1, padx=10)
tk.Label(rak2, text="Rak 2", bg="#fab1a0", font=("Arial", 12, "bold")).pack()
listbox_rak2 = tk.Listbox(rak2, width=23, height=10, bd=4, relief="sunken")
listbox_rak2.pack()

# Rak 3
rak3 = tk.Frame(frame_rak, bg="#81ecec", bd=4, relief="ridge")
rak3.grid(row=0, column=2, padx=10)
tk.Label(rak3, text="Rak 3", bg="#81ecec", font=("Arial", 12, "bold")).pack()
listbox_rak3 = tk.Listbox(rak3, width=23, height=10, bd=4, relief="sunken")
listbox_rak3.pack()

# ---------------------------------------
# PENCARIAN BUKU (DI FIX)
# ---------------------------------------
frame_search = tk.Frame(main, bg="#ffeaa7", bd=4, relief="ridge")
frame_search.pack(padx=10, pady=10, fill="x")

tk.Label(frame_search, text="Masukkan Judul Buku yang Dicari:",
         bg="#ffeaa7", font=("Arial", 11)).pack()

# FIX: Entry pencarian tidak tertutup apa pun
entry_cari = tk.Entry(frame_search, width=60, font=("Arial", 11))
entry_cari.pack(pady=5)

btn_cari = tk.Button(frame_search,
                     text="Cari Buku",
                     bg="#fab1a0",
                     font=("Arial", 11, "bold"),
                     relief="raised",
                     command=cari_buku)
btn_cari.pack(pady=5)

window.mainloop()
