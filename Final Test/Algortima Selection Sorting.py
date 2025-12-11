import tkinter as tk
from tkinter import messagebox


# =======================================================
#               FUNGSI SELECTION SORT
# =======================================================
def selection_sort(arr, log_widget):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        log_widget.insert(tk.END, f"Mulai dari index {i}, nilai awal minimum: {arr[min_index]}\n")

        for j in range(i + 1, n):
            log_widget.insert(tk.END, f"  Bandingkan {arr[j]} dengan {arr[min_index]}\n")

            if arr[j] < arr[min_index]:
                min_index = j
                log_widget.insert(tk.END, f"   → Update nilai minimum: {arr[min_index]}\n")

        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
        log_widget.insert(tk.END, f"Tukar posisi {arr[min_index]} dengan {arr[i]}\n")
        log_widget.insert(tk.END, f"Hasil sementara: {arr}\n\n")

    return arr


# =======================================================
#               FUNGSI TOMBOL PROSES
# =======================================================
def proses_sort():
    data_input = entry_data.get()

    if not data_input:
        messagebox.showwarning("Peringatan", "Masukkan data terlebih dahulu!")
        return

    try:
        arr = list(map(int, data_input.split()))
    except:
        messagebox.showerror("Error", "Masukkan angka dengan spasi!\nContoh: 5 2 9 1 3")
        return

    text_log.delete("1.0", tk.END)
    hasil = selection_sort(arr, text_log)
    label_hasil.config(text=f"Hasil Akhir: {hasil}")


# =======================================================
#               GUI TKINTER
# =======================================================
root = tk.Tk()
root.title("Selection Sort - Tkinter")
root.geometry("520x480")
root.configure(bg="#222")

# Judul
title = tk.Label(root, text="SELECTION SORT", fg="white",
                 bg="#222", font=("Arial", 20, "bold"))
title.pack(pady=10)

# Input data
frame_input = tk.Frame(root, bg="#222")
frame_input.pack()

label_data = tk.Label(frame_input, text="Masukkan angka (pisahkan spasi):",
                      fg="white", bg="#222", font=("Arial", 11))
label_data.grid(row=0, column=0, padx=5)

entry_data = tk.Entry(frame_input, width=40, font=("Arial", 12))
entry_data.grid(row=1, column=0, pady=5)

# Tombol proses
btn_proses = tk.Button(root, text="PROSES SELECTION SORT",
                       command=proses_sort, width=30, bg="#4CAF50",
                       fg="white", font=("Arial", 12, "bold"))
btn_proses.pack(pady=10)

# Log Proses
text_log = tk.Text(root, width=60, height=15, font=("Consolas", 11))
text_log.pack(pady=10)

# Hasil akhir
label_hasil = tk.Label(root, text="Hasil Akhir: -",
                       fg="yellow", bg="#222", font=("Arial", 14, "bold"))
label_hasil.pack(pady=5)

root.mainloop()
