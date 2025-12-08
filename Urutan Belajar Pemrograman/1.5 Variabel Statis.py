# Program variabel statis sederhana

class Siswa:
    # Variabel statis (dimiliki oleh class, bukan oleh objek)
    jumlah_siswa = 0

    def __init__(self, nama):
        self.nama = nama
        Siswa.jumlah_siswa += 1   # setiap objek baru menambah jumlah siswa

# Program utama
print("=== PROGRAM VARIABEL STATIS ===")

jumlah = int(input("Masukkan jumlah siswa: "))

daftar = []

for i in range(jumlah):
    nama = input(f"Masukkan nama siswa ke-{i+1}: ")
    daftar.append(Siswa(nama))

# Output
print("\n=== DAFTAR SISWA ===")
for i, s in enumerate(daftar, 1):
    print(f"{i}. {s.nama}")

print("\nTotal siswa (dari variabel statis):", Siswa.jumlah_siswa)

print ("==SETELAH DI MODIFIKASI==")

# =================== WARNA ===================
RESET   = "\033[0m"
BOLD    = "\033[1m"

RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
CYAN    = "\033[36m"
MAGENTA = "\033[35m"
WHITE   = "\033[37m"


# =================== CLASS VARIABEL STATIS ===================
class Siswa:
    jumlah_siswa = 0  # Variabel statis

    def __init__(self, nama):
        self.nama = nama
        Siswa.jumlah_siswa += 1


# =================== HEADER SEDERHANA ===================
print(BOLD + CYAN + "========================================")
print("        PROGRAM VARIABEL STATIS         ")
print("========================================" + RESET)

# =================== INPUT ===================
jumlah = int(input(YELLOW + "Masukkan jumlah siswa: " + RESET))
print()

daftar = []

for i in range(jumlah):
    print(GREEN + f"► Masukkan nama siswa ke-{i+1}:" + RESET)
    nama = input("   → ")
    daftar.append(Siswa(nama))
    print(CYAN + "   ✔ Data ditambahkan!" + RESET)
    print()

# =================== DAFTAR SISWA ===================
print(BOLD + MAGENTA + "========== DAFTAR SISWA ==========" + RESET)

for i, s in enumerate(daftar, 1):
    print(CYAN + f"{i}. {s.nama}" + RESET)

print()

# =================== TOTAL ===================
print(BOLD + GREEN)
print("========== RINGKASAN ==========")
print(f"Total Siswa : {Siswa.jumlah_siswa}")
print("Tipe Variabel    : STATIs")
print("================================" + RESET)

print(BOLD + BLUE + "Program selesai dijalankan!" + RESET)
