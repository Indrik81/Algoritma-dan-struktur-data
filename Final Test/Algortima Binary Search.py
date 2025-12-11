import tkinter as tk
from tkinter import messagebox

# =======================================================
#                 FUNGSI BINARY SEARCH
# =======================================================
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # ditemukan
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # tidak ditemukan


# =======================================================
#                 FUNGSI TOMBOL CARI
# =======================================================
def cari():
    try:
        # ambil input array dan ubah jadi list integer
        arr = list(map(int, entry_array.get().split(",")))
        arr.sort()  # Binary search wajib urut
        target = int(entry_cari.get())
    except:
        messagebox.showerror("Error", "Masukkan angka dengan benar!")
        return

    hasil = binary_search(arr, target)

    label_sorted.config(text=f"Array Terurut : {arr}")

    if hasil != -1:
        messagebox.showinfo("Hasil", f"Angka {target} ditemukan di index ke-{hasil}")
    else:
        messagebox.showwarning("Hasil", f"Angka {target} TIDAK ditemukan")


# =======================================================
#                 GUI TKINTER
# =======================================================
root = tk.Tk()
root.title("Binary Search Tkinter")
root.geometry("450x300")
root.config(bg="#e3f2fd")

title = tk.Label(root, text="Binary Search Menggunakan Tkinter",
                 font=("Arial", 14, "bold"), bg="#e3f2fd")
title.pack(pady=10)

frame = tk.Frame(root, bg="#e3f2fd")
frame.pack()

# Input array
tk.Label(frame, text="Masukkan Angka (pisah koma):", font=("Arial", 11),
         bg="#e3f2fd").grid(row=0, column=0, sticky="w")
entry_array = tk.Entry(frame, width=40)
entry_array.grid(row=1, column=0, pady=5)

# Input target
tk.Label(frame, text="Angka yang Dicari:", font=("Arial", 11),
         bg="#e3f2fd").grid(row=2, column=0, sticky="w")
entry_cari = tk.Entry(frame, width=20)
entry_cari.grid(row=3, column=0, pady=5)

# Tombol cari
btn_cari = tk.Button(root, text="Cari Data", font=("Arial", 12, "bold"),
                     bg="#42a5f5", fg="white", width=15, command=cari)
btn_cari.pack(pady=10)

# Menampilkan array terurut
label_sorted = tk.Label(root, text="Array Terurut : -", font=("Arial", 11),
                        bg="#e3f2fd")
label_sorted.pack()

root.mainloop()
