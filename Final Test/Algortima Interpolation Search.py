import tkinter as tk
from tkinter import messagebox

# ==============================
#      INTERPOLATION SEARCH
# ==============================
def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:

        if low == high:
            if arr[low] == x:
                return low
            return -1

        # Rumus posisi interpolasi
        pos = low + int(((x - arr[low]) * (high - low)) / (arr[high] - arr[low]))

        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# ==============================
#       TKINTER GUI
# ==============================
def lakukan_pencarian():
    try:
        x = int(entry_cari.get())
    except:
        messagebox.showerror("Error", "Masukkan angka yang valid!")
        return

    hasil = interpolation_search(data_array, x)

    if hasil != -1:
        label_hasil.config(text=f"✔ Data ditemukan pada index ke-{hasil}", fg="green")
    else:
        label_hasil.config(text="✖ Data tidak ditemukan", fg="red")


# ==============================
#         DATA ARRAY
# ==============================
data_array = [5, 9, 13, 21, 28, 33, 41, 57, 62, 70, 88, 95]


# ==============================
#         GUI TKINTER
# ==============================
root = tk.Tk()
root.title("Interpolation Search")
root.geometry("420x300")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="INTERPOLATION SEARCH", fg="white",
                 bg="#1e1e1e", font=("Arial", 18, "bold"))
title.pack(pady=10)

label_data = tk.Label(root, text=f"Data Array : {data_array}",
                      fg="lightblue", bg="#1e1e1e", font=("Arial", 12))
label_data.pack(pady=10)

entry_cari = tk.Entry(root, font=("Arial", 14), justify="center")
entry_cari.pack(pady=5)

btn_cari = tk.Button(root, text="Cari Data", font=("Arial", 12, "bold"),
                     bg="#4CAF50", fg="white", width=12, command=lakukan_pencarian)
btn_cari.pack(pady=10)

label_hasil = tk.Label(root, text="", fg="white", bg="#1e1e1e",
                       font=("Arial", 14, "bold"))
label_hasil.pack(pady=10)

root.mainloop()
