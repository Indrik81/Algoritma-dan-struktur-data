from tkinter import *
from tkinter import messagebox, simpledialog
import random

# Fungsi untuk mendapatkan nama pemain via dialog Tkinter
def get_player_names():
    root_temp = Tk()
    root_temp.withdraw()  # Sembunyikan jendela utama sementara
    name1 = simpledialog.askstring("Nama Pemain", "Masukkan nama Player 1 (default: Player 1):", initialvalue="Player 1") or "Player 1"
    name2 = simpledialog.askstring("Nama Pemain", "Masukkan nama Player 2 (default: Player 2):", initialvalue="Player 2") or "Player 2"
    root_temp.destroy()  # Tutup jendela sementara
    return name1, name2

Player1_name, Player2_name = get_player_names()
Player1 = random.choice(["O", "X"])  # Pilih simbol awal acak
stop_game = False
score = {"O": 0, "X": 0}  # Skor kemenangan

def clicked(r, c):
    global Player1
    if Player1 == "O" and states[r][c] == 0 and not stop_game:
        b[r][c].configure(text="O", fg="#0000ff", bg="#ffffff")  # O biru di bg putih
        states[r][c] = 'O'
        Player1 = 'X'
        status_label.config(text=f"Giliran: {Player2_name}", fg="#ffffff")
    elif Player1 == 'X' and states[r][c] == 0 and not stop_game:
        b[r][c].configure(text="X", fg="#ffffff", bg="#000080")  # X putih di bg biru gelap
        states[r][c] = "X"
        Player1 = "O"
        status_label.config(text=f"Giliran: {Player1_name}", fg="#0000ff")
    check_if_win()

def check_if_win():
    global stop_game
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            highlight_winner([(i,0),(i,1),(i,2)])
            stop_game = True
            winner = states[i][0]
            score[winner] += 1
            update_score()
            messagebox.showinfo("Winner", f"{Player1_name if winner == 'O' else Player2_name} Menang! 🎉")
            return
        elif states[0][i] == states[1][i] == states[2][i] != 0:
            highlight_winner([(0,i),(1,i),(2,i)])
            stop_game = True
            winner = states[0][i]
            score[winner] += 1
            update_score()
            messagebox.showinfo("Winner", f"{Player1_name if winner == 'O' else Player2_name} Menang! 🎉")
            return
    if states[0][0] == states[1][1] == states[2][2] != 0:
        highlight_winner([(0,0),(1,1),(2,2)])
        stop_game = True
        winner = states[0][0]
        score[winner] += 1
        update_score()
        messagebox.showinfo("Winner", f"{Player1_name if winner == 'O' else Player2_name} Menang! 🎉")
        return
    if states[0][2] == states[1][1] == states[2][0] != 0:
        highlight_winner([(0,2),(1,1),(2,0)])
        stop_game = True
        winner = states[0][2]
        score[winner] += 1
        update_score()
        messagebox.showinfo("Winner", f"{Player1_name if winner == 'O' else Player2_name} Menang! 🎉")
        return
    if all(states[i][j] != 0 for i in range(3) for j in range(3)):
        stop_game = True
        messagebox.showinfo("Tie", "Permainan Seri! 🤝")

def highlight_winner(coords):
    for r, c in coords:
        b[r][c].configure(bg="#4169e1")  # Biru terang highlight

def update_score():
    score_label.config(text=f"Skor: {Player1_name} ({score['O']}) - {Player2_name} ({score['X']})")

def reset_game():
    global Player1, stop_game, states
    Player1 = random.choice(["O", "X"])
    stop_game = False
    states = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            b[i][j].configure(text="", bg="#ffffff", fg="#000000")  # Reset ke putih
    if Player1 == "O":
        status_label.config(text=f"Giliran: {Player1_name}", fg="#0000ff")
    else:
        status_label.config(text=f"Giliran: {Player2_name}", fg="#ffffff")

def reset_score():
    global score
    score = {"O": 0, "X": 0}
    update_score()

def reset_all():
    reset_score()
    reset_game()

# Design window
root = Tk()
root.title("Biru Putih Tic Tac Toe dengan Gambar")
root.resizable(0, 0)

# Tambahkan gambar latar belakang (pastikan file background.png ada)
try:
    bg_image = PhotoImage(file="background.png")  # Gambar latar biru-putih
    bg_label = Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)  # Cover seluruh window
except:
    root.configure(bg="#add8e6")  # Fallback jika gambar tidak ada

# Label atas: Nama pemain
title_label = Label(root, text=f"{Player1_name} (O)    vs    {Player2_name} (X)", font=("Courier", 18, "bold"), fg="#000080", bg="#add8e6")
title_label.grid(row=0, column=0, columnspan=3, pady=(10, 0))

# Label skor dengan ikon trofi
try:
    trophy_image = PhotoImage(file="trophy.png").subsample(10, 10)  # Ikon trofi kecil
    score_label = Label(root, text=f"Skor: {Player1_name} ({score['O']}) - {Player2_name} ({score['X']})", font=("Courier", 12), fg="#000080", bg="#add8e6", image=trophy_image, compound=LEFT)
except:
    score_label = Label(root, text=f"Skor: {Player1_name} ({score['O']}) - {Player2_name} ({score['X']})", font=("Courier", 12), fg="#000080", bg="#add8e6")
score_label.grid(row=1, column=0, columnspan=3)

# Button grid
b = [[0,0,0],[0,0,0],[0,0,0]]
states = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(
            height=5, width=10,
            font=("Courier", "24", "bold"),
            bg="#ffffff",  # Putih
            fg="#000000",
            activebackground="#e0e0e0",
            relief="ridge", borderwidth=3,  # Border biru-putih
            command=lambda r=i, c=j: clicked(r, c))
        b[i][j].grid(row=i+2, column=j, padx=3, pady=3)

# Status giliran dengan ikon pemain
if Player1 == "O":
    status_text = f"Giliran: {Player1_name}"
    status_color = "#0000ff"
else:
    status_text = f"Giliran: {Player2_name}"
    status_color = "#ffffff"

try:
    player_image = PhotoImage(file="player_icon.png").subsample(10, 10)  # Ikon pemain kecil
    status_label = Label(root, text=status_text, font=("Courier", "14", "bold"), fg=status_color, bg="#add8e6", image=player_image, compound=LEFT)
except:
    status_label = Label(root, text=status_text, font=("Courier", "14", "bold"), fg=status_color, bg="#add8e6")
status_label.grid(row=5, column=0, columnspan=3)

# Tombol reset (tiga opsi) dengan ikon
try:
    reset_image = PhotoImage(file="reset_icon.png").subsample(10, 10)  # Ikon reset kecil
    reset_game_btn = Button(root, text="Reset Game", font=("Courier", "10", "bold"), command=reset_game, bg="#ffffff", fg="#000080", relief="raised", image=reset_image, compound=LEFT)
    reset_score_btn = Button(root, text="Reset Skor", font=("Courier", "10", "bold"), command=reset_score, bg="#ffffff", fg="#000080", relief="raised", image=reset_image, compound=LEFT)
    reset_all_btn = Button(root, text="Reset Semua", font=("Courier", "10", "bold"), command=reset_all, bg="#4169e1", fg="#ffffff", relief="raised", image=reset_image, compound=LEFT)
except:
    reset_game_btn = Button(root, text="Reset Game", font=("Courier", "10", "bold"), command=reset_game, bg="#ffffff", fg="#000080", relief="raised")
    reset_score_btn = Button(root, text="Reset Skor", font=("Courier", "10", "bold"), command=reset_score, bg="#ffffff", fg="#000080", relief="raised")
    reset_all_btn = Button(root, text="Reset Semua", font=("Courier", "10", "bold"), command=reset_all, bg="#4169e1", fg="#ffffff", relief="raised")

reset_game_btn.grid(row=6, column=0, pady=10)
reset_score_btn.grid(row=6, column=1, pady=10)
reset_all_btn.grid(row=6, column=2, pady=10)

root.mainloop()
