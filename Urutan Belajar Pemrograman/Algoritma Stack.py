# =======================================
#  PROGRAM SEDERHANA ALGORITMA STACK
# =======================================

stack = []  # struktur data stack (LIFO)

def push(data):
    stack.append(data)
    print(f"Data '{data}' berhasil ditambahkan ke stack.")

def pop_data():
    if len(stack) == 0:
        print("Stack kosong! Tidak ada data untuk dihapus.")
    else:
        removed = stack.pop()
        print(f"Data '{removed}' berhasil dihapus dari stack.")

def tampilkan_stack():
    if len(stack) == 0:
        print("Stack kosong.")
    else:
        print("Isi Stack (atas ke bawah):")
        for item in reversed(stack):
            print(f"- {item}")

# =============================
#  PROGRAM UTAMA
# =============================
while True:
    print("\n=== MENU STACK ===")
    print("1. Push Data")
    print("2. Pop Data")
    print("3. Tampilkan Stack")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        data = input("Masukkan data: ")
        push(data)

    elif pilihan == "2":
        pop_data()

    elif pilihan == "3":
        tampilkan_stack()

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")

print ("==SETELAH DI MODIFIKASI==")

# ================================
#  PROGRAM STACK SEDERHANA
#  DENGAN TAMPILAN MENARIK & BERWARNA
# ================================

# Warna ANSI
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
CYAN    = "\033[96m"
MAGENTA = "\033[95m"
RESET   = "\033[0m"

# Judul Program
print(CYAN + "="*45)
print("      PROGRAM STRUKTUR DATA STACK")
print("="*45 + RESET)

stack = []

def tampilkan_stack():
    print(MAGENTA + "\nIsi Stack Saat Ini:" + RESET)
    if len(stack) == 0:
        print(RED + "[STACK KOSONG]\n" + RESET)
    else:
        for i in range(len(stack)-1, -1, -1):
            print(GREEN + f" → {stack[i]}" + RESET)
        print(YELLOW + "----- TOP -----" + RESET)

while True:
    print(BLUE + """
Menu Pilihan:
1. Push (Menambah Data)
2. Pop  (Mengambil Data Teratas)
3. Lihat Isi Stack
4. Keluar
""" + RESET)

    pilihan = input(YELLOW + "Masukkan pilihan (1-4): " + RESET)

    # PUSH
    if pilihan == "1":
        data = input(GREEN + "Masukkan data yang akan di-push: " + RESET)
        stack.append(data)
        print(GREEN + f"✓ Data '{data}' berhasil ditambahkan ke stack!" + RESET)
        tampilkan_stack()

    # POP
    elif pilihan == "2":
        if len(stack) == 0:
            print(RED + "✗ Stack masih kosong, tidak dapat melakukan pop!" + RESET)
        else:
            dikeluarkan = stack.pop()
            print(GREEN + f"✓ Data '{dikeluarkan}' berhasil di-pop!" + RESET)
        tampilkan_stack()

    # TAMPILKAN STACK
    elif pilihan == "3":
        tampilkan_stack()

    # KELUAR
    elif pilihan == "4":
        print(CYAN + "Terima kasih! Program selesai." + RESET)
        break

    else:
        print(RED + "✗ Pilihan tidak valid! Silakan coba lagi." + RESET)

