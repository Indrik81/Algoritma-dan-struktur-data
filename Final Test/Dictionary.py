import tkinter as tk
from tkinter import messagebox

# ===========================
#    DICTIONARY KAMUS
# ===========================
kamus = {
    "apel": "Buah berwarna merah atau hijau yang manis dan segar.",
    "buku": "Kumpulan lembaran berisi tulisan atau gambar.",
    "cahaya": "Energi yang membuat benda-benda dapat terlihat.",
    "datar": "Permukaan yang rata, tidak bergelombang.",
    "emas": "Logam mulia berwarna kuning dan bernilai tinggi.",
    "kucing": "Hewan peliharaan berbulu yang sering mengeong.",
    "rumah": "Bangunan tempat tinggal manusia."
}

# ===========================
#     FUNGSI PENCARIAN
# ===========================
def cari_kata():
    kata = entry_kata.get().lower().strip()

    if kata == "":
        messagebox.showwarning("Peringatan", "Masukkan kata yang ingin dicari!")
        return

    if kata in kamus:
        hasil = f"Kata ditemukan!\n\n{kata} : {kamus[kata]}"
        label_hasil.config(text=hasil, fg="green")
    else:
        label_hasil.config(
            text="Kata tidak ditemukan dalam kamus.\nPeriksa kembali ejaan Anda.",
            fg="red"
        )

def tampilkan_semua():
    listbox.delete(0, tk.END)
    for k, v in kamus.items():
        listbox.insert(tk.END, f"{k} : {v}")

# ===========================
#       GUI TKINTER
# ===========================
window = tk.Tk()
window.title("Pencarian Ejaan dalam Kamus")
window.geometry("520x500")
window.config(bg="#E3F2FD")

title = tk.Label(window, text="📘 KAMUS MINI — Cek Ejaan Kata", 
                 font=("Arial", 16, "bold"), bg="#E3F2FD", fg="#1565C0")
title.pack(pady=10)

# Input kata
frame_input = tk.Frame(window, bg="#E3F2FD")
frame_input.pack(pady=5)

tk.Label(frame_input, text="Masukkan Kata:", font=("Arial", 12), bg="#E3F2FD").grid(row=0, column=0, padx=5)
entry_kata = tk.Entry(frame_input, font=("Arial", 12), width=25)
entry_kata.grid(row=0, column=1, padx=5)

btn_cari = tk.Button(window, text="Cari Ejaan", font=("Arial", 12), width=20,
                     command=cari_kata, bg="#64B5F6", fg="white")
btn_cari.pack(pady=10)

# Hasil pencarian
label_hasil = tk.Label(window, text="Hasil pencarian akan muncul di sini.",
                       font=("Arial", 12), bg="#E3F2FD")
label_hasil.pack(pady=10)

# Tombol tampilkan semua
btn_all = tk.Button(window, text="Tampilkan Semua Kata", font=("Arial", 12),
                    command=tampilkan_semua, bg="#90CAF9")
btn_all.pack(pady=5)

# Listbox isi kamus
listbox = tk.Listbox(window, width=60, height=10, font=("Arial", 11))
listbox.pack(pady=10)

window.mainloop()
