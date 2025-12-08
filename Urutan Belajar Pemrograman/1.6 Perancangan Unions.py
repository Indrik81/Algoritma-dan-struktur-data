# Program sederhana menggunakan Union Type (tanpa import)

def tampilkan_data(data: int | float | str):
    print("Data yang diterima berdasarkan tipe =", data)


# Contoh penggunaan
tampilkan_data(25)        # int
tampilkan_data(3.14)      # float
tampilkan_data("Halo")    # string

print ("==SETELAH DI MODIFIKASI==")

# ==========================================================
# 🌈 PROGRAM UNION PYTHON (Tanpa Import) — Versi Berwarna
# ==========================================================

# Warna ANSI
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[96m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
MAGENTA = "\033[95m"
BLUE    = "\033[94m"
RED     = "\033[91m"

# ----------------------------------------------------------
# Fungsi menggunakan Union Type (tanpa import typing)
# ----------------------------------------------------------
def tampilkan_data(data: int | float | str):
    print(f"{CYAN}{BOLD}========================================{RESET}")
    print(f"{YELLOW}{BOLD}        DATA UNION DI PROSES{RESET}")
    print(f"{CYAN}{BOLD}========================================{RESET}")

    if isinstance(data, int):
        tipe = "INTEGER (Angka Bulat)"
        warna = GREEN
    elif isinstance(data, float):
        tipe = "FLOAT (Angka Desimal)"
        warna = BLUE
    else:
        tipe = "STRING (Teks)"
        warna = MAGENTA

    print(f"{warna}Tipe Data   : {tipe}{RESET}")
    print(f"{warna}Isi Data    : {data}{RESET}")
    print(f"{CYAN}{BOLD}========================================{RESET}\n")

# ----------------------------------------------------------
# PROGRAM UTAMA
# ----------------------------------------------------------
print(f"{BOLD}{GREEN}=== PROGRAM DEMO UNION TYPE PYTHON ==={RESET}")
print(f"{BLUE}Pilih jenis data yang ingin dimasukkan:{RESET}")
print("1. Angka Bulat (int)")
print("2. Angka Desimal (float)")
print("3. Teks / String (str)\n")

pilihan = input(f"{YELLOW}Masukkan pilihan (1/2/3): {RESET}")

if pilihan == "1":
    nilai = int(input(f"{GREEN}Masukkan nilai integer: {RESET}"))
    tampilkan_data(nilai)

elif pilihan == "2":
    nilai = float(input(f"{GREEN}Masukkan nilai float: {RESET}"))
    tampilkan_data(nilai)

elif pilihan == "3":
    nilai = input(f"{GREEN}Masukkan teks/string: {RESET}")
    tampilkan_data(nilai)

else:
    print(f"{RED}Pilihan tidak valid! Program dihentikan.{RESET}")
