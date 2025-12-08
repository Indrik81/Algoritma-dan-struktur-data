import tkinter as tk
from tkinter import ttk

# -------------------------------
#   FUNGSI SHELL SORT
# -------------------------------
def shell_sort():
    try:
        data = list(map(int, entry_data.get().split()))
    except:
        result_label.config(text="❌ Masukkan hanya angka yang dipisah spasi!")
        return

    for row in table.get_children():
        table.delete(row)

    gap = len(data) // 2
    langkah = 1

    # Proses shell sort
    while gap > 0:
        start_data = data.copy()    # untuk dilihat sebelum proses

        for i in range(gap, len(data)):
            temp = data[i]
            j = i

            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap

            data[j] = temp

        # MENAMPILKAN INFORMASI GAP SECARA DETAIL
        penjelasan_gap = f"GAP {gap} → elemen dengan jarak {gap} dibandingkan."

        table.insert("", "end", values=(
            langkah,
            gap,
            " | ".join(map(str, data))
        ))

        langkah += 1
        gap //= 2

    result_label.config(text="✔ Pengurutan Selesai!")

# -------------------------------
#   UI TKINTER
# -------------------------------
root = tk.Tk()
root.title("Program Shell Sort - Dengan Tabel dan Penjelasan GAP")
root.geometry("750x450")
root.configure(bg="#1e1e1e")

title = tk.Label(root, text="🔷 PROGRAM SHELL SORT 🔷",
                 font=("Arial", 20, "bold"), fg="#00eaff", bg="#1e1e1e")
title.pack(pady=10)

frame_input = tk.Frame(root, bg="#1e1e1e")
frame_input.pack(pady=5)

label_data = tk.Label(frame_input, text="Masukkan Angka (pisahkan dengan spasi):",
                      font=("Arial", 12), fg="white", bg="#1e1e1e")
label_data.grid(row=0, column=0, padx=10)

entry_data = tk.Entry(frame_input, width=45, font=("Arial", 12))
entry_data.grid(row=1, column=0, pady=5)

btn_sort = tk.Button(root, text="Mulai Shell Sort", font=("Arial", 12, "bold"),
                     bg="#00b7ff", fg="black", width=20, command=shell_sort)
btn_sort.pack(pady=10)

columns = ("langkah", "gap", "hasil")
table = ttk.Treeview(root, columns=columns, show="headings", height=9)

table.heading("langkah", text="Langkah")
table.heading("gap", text="Gap")
table.heading("hasil", text="Hasil Pengurutan (Setiap Pengurangan Gap)")

table.column("langkah", width=70, anchor="center")
table.column("gap", width=70, anchor="center")
table.column("hasil", width=520, anchor="w")

table.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"),
                        fg="#00ff6a", bg="#1e1e1e")
result_label.pack()

root.mainloop()
