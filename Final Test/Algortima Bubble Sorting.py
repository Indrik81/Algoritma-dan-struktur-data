import tkinter as tk
from tkinter import messagebox

def bubble_sort(numbers):
    arr = numbers.copy()
    n = len(arr)

    # Proses bubble sort
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def sort_numbers():
    data = entry.get()

    if not data:
        messagebox.showerror("Error", "Masukkan angka terlebih dahulu!")
        return

    try:
        # Convert input menjadi list integer
        numbers = list(map(int, data.split()))
    except:
        messagebox.showerror("Error", "Input harus berupa angka dipisah spasi!")
        return

    sorted_result = bubble_sort(numbers)

    result_label.config(text=f"Hasil Sorting: {sorted_result}")

# ========================
# GUI TKINTER
# ========================

root = tk.Tk()
root.title("Bubble Sort Tkinter")
root.geometry("400x250")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text="PROGRAM BUBBLE SORT", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

label = tk.Label(root, text="Masukkan Angka (pisahkan dengan spasi):", bg="#f0f0f0", font=("Arial", 10))
label.pack()

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

sort_button = tk.Button(root, text="Sort Sekarang", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                        command=sort_numbers)
sort_button.pack(pady=10)

result_label = tk.Label(root, text="Hasil Sorting: -", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

root.mainloop()
