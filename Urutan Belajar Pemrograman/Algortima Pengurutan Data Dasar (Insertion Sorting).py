import tkinter as tk
from tkinter import messagebox

# ===============================
#      WATER SORT – MODERN UI
# ===============================

root = tk.Tk()
root.title("Game Tuang Air Berwarna - Modern Version")
root.geometry("700x500")
root.configure(bg="#1a1a1a")

# -------------------------
# Warna air modern
# -------------------------
COLOR_MAP = {
    "red": "#ff4d4d",
    "blue": "#4d79ff",
    "green": "#33cc33",
    "yellow": "#ffe066",
    "purple": "#cc66ff",
}

# LEVEL default (bisa diselesaikan)
botol_data = [
    ["red", "blue", "red", "blue"],
    ["blue", "red", "blue", "red"],
    [],
    []
]

MAKS = 4

selected = None
botol_canvas = []


# ============================
#   FUNGSI GAMBAR BOTOL
# ============================
def gambar_botol():
    """Menggambar botol dengan efek 3D dan glossy"""
    for i, kanvas in enumerate(botol_canvas):
        kanvas.delete("all")

        w = 80
        h = 250
        x0 = 20
        y0 = 20

        # Shadow belakang botol
        kanvas.create_rectangle(
            x0 + 5, y0 + 10, x0 + w + 5, y0 + h + 10,
            fill="#111", outline="", stipple="gray50"
        )

        # Botol utama (rounded effect custom)
        kanvas.create_rectangle(
            x0, y0, x0 + w, y0 + h,
            fill="#e6e6e6", outline="#ffffff",
            width=3
        )

        # Efek glossy kiri botol
        kanvas.create_rectangle(
            x0 + 5, y0 + 5, x0 + 15, y0 + h - 5,
            fill="#f2f2f2", outline="", stipple="gray25"
        )

        # Isi air
        if botol_data[i]:
            tinggi = h // MAKS
            for layer in range(len(botol_data[i])):
                warna = COLOR_MAP.get(botol_data[i][layer], botol_data[i][layer])

                kanvas.create_rectangle(
                    x0 + 5,
                    y0 + h - (layer + 1) * tinggi,
                    x0 + w - 5,
                    y0 + h - (layer * tinggi),
                    fill=warna,
                    outline=warna
                )

        # Jika dipilih → glow effect
        if selected == i:
            kanvas.create_rectangle(
                x0 - 5, y0 - 5, x0 + w + 5, y0 + h + 5,
                outline="#00e6e6", width=4
            )


# ============================
#   LOGIKA GAME
# ============================
def pilih_botol(idx):
    """Memilih botol dan menumpahkan"""
    global selected

    if selected is None:
        if not botol_data[idx]:
            return
        selected = idx
    else:
        if selected != idx:
            tuang(selected, idx)
        selected = None

    gambar_botol()


def tuang(dari, ke):
    """Menuang isi botol dengan logika valid"""
    if not botol_data[dari]:
        return
    if len(botol_data[ke]) >= MAKS:
        return

    warna_tuang = botol_data[dari][-1]

    if not botol_data[ke]:
        botol_data[ke].append(botol_data[dari].pop())
    else:
        warna_atas = botol_data[ke][-1]
        if warna_atas != warna_tuang:
            return
        botol_data[ke].append(botol_data[dari].pop())

    # Tuang beruntun
    while botol_data[dari] and \
          len(botol_data[ke]) < MAKS and \
          botol_data[dari][-1] == botol_data[ke][-1]:
        botol_data[ke].append(botol_data[dari].pop())

    cek_menang()


def cek_menang():
    for b in botol_data:
        if len(b) == 0:
            continue
        if len(b) != MAKS:
            return
        if len(set(b)) != 1:
            return

    messagebox.showinfo("SELAMAT!", "Puzzle Berhasil Diselesaikan!")


# ============================
#   HEADER TITLE
# ============================
judul = tk.Label(
    root,
    text="WATER SORT PUZZLE",
    font=("Arial Black", 26),
    fg="#00e6e6",
    bg="#1a1a1a"
)
judul.pack(pady=10)

# Garis neon
tk.Canvas(root, width=400, height=3, bg="#00e6e6", highlightthickness=0).pack()


# ============================
#   FRAME BOTOL
# ============================
frame = tk.Frame(root, bg="#1a1a1a")
frame.pack(pady=20)

for i in range(len(botol_data)):
    c = tk.Canvas(frame, width=120, height=300, bg="#1a1a1a", highlightthickness=0)
    c.grid(row=0, column=i, padx=20)
    c.bind("<Button-1>", lambda e, idx=i: pilih_botol(idx))

    botol_canvas.append(c)

gambar_botol()


# ============================
#   TOMBOL RESET / NEXT LEVEL
# ============================
def reset_level():
    global botol_data
    botol_data = [
        ["red", "blue", "red", "blue"],
        ["blue", "red", "blue", "red"],
        [],
        []
    ]
    gambar_botol()


tk.Button(
    root,
    text="Reset Level",
    font=("Arial", 12, "bold"),
    bg="#00e6e6",
    fg="black",
    width=12,
    command=reset_level
).pack(pady=10)

root.mainloop()
