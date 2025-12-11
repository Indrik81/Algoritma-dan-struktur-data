import tkinter as tk
from tkinter import messagebox

# ======================================================
#                FUNGSI PROSES DATA
# ======================================================
def proses_data():
    nama = entry_nama.get()
    umur = entry_umur.get()
    tinggi = entry_tinggi.get()

    if nama == "" or umur == "" or tinggi == "":
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")
        return

    try:
        umur = int(umur)          # integer
        tinggi = float(tinggi)    # float
    except ValueError:
        messagebox.showerror("Error", "Umur harus integer dan tinggi harus float!")
        return

    hasil = f"Nama : {nama}\nUmur : {umur} tahun\nTinggi : {tinggi} cm"
    label_hasil.config(text=hasil)


# ======================================================
#               GUI TKINTER — TEMA MODERN
# ======================================================
window = tk.Tk()
window.title("Form Data Modern")
window.geometry("400x480")
window.configure(bg="#B39DDB")   # Ungu soft background

# FRAME PUTIH (Card)
frame = tk.Frame(window, bg="white", bd=0, relief="raised")
frame.place(relx=0.5, rely=0.5, anchor="center", width=310, height=380)

# JUDUL
title = tk.Label(frame, text="Input Data", font=("Arial", 18, "bold"),
                 bg="white", fg="#512DA8")
title.pack(pady=15)

# ================= Field Nama (String) =================
tk.Label(frame, text="Nama (String):", font=("Arial", 12), bg="white").pack()
entry_nama = tk.Entry(frame, font=("Arial", 12), width=25)
entry_nama.pack(pady=5)

# ================= Umur (Integer) =================
tk.Label(frame, text="Umur (Integer):", font=("Arial", 12), bg="white").pack()
entry_umur = tk.Entry(frame, font=("Arial", 12), width=25)
entry_umur.pack(pady=5)

# ================= Tinggi (Float) =================
tk.Label(frame, text="Tinggi Badan (Float):", font=("Arial", 12), bg="white").pack()
entry_tinggi = tk.Entry(frame, font=("Arial", 12), width=25)
entry_tinggi.pack(pady=5)

# ================= Tombol =================
btn = tk.Button(
    frame, text="Proses Data",
    font=("Arial", 12, "bold"),
    bg="#7E57C2", fg="white",
    activebackground="#5E35B1",
    width=20, pady=5,
    command=proses_data
)
btn.pack(pady=15)

# ================= Hasil =================
label_hasil = tk.Label(
    frame, text="Hasil akan muncul di sini.",
    font=("Arial", 12),
    bg="white", fg="#1A237E"
)
label_hasil.pack(pady=10)

window.mainloop()
