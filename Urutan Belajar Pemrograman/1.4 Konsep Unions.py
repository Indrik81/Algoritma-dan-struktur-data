# Program konsep UNION sederhana di Python
# Satu variabel (value) bisa menyimpan tipe data apa saja

class UnionSederhana:
    def __init__(self):
        self.value = None   # tempat data union

# Membuat objek union
data = UnionSederhana()

print("=== PROGRAM UNION ===")
print("Pilih tipe data yang ingin dimasukkan:")
print("1. Angka (int)")
print("2. Desimal (float)")
print("3. Teks (string)")
print("4. Ya/Tidak (boolean)")
print("======================")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

if pilihan == "1":
    data.value = int(input("Masukkan angka (int): "))
elif pilihan == "2":
    data.value = float(input("Masukkan angka desimal (float): "))
elif pilihan == "3":
    data.value = input("Masukkan teks: ")
elif pilihan == "4":
    teks = input("Masukkan (ya/tidak): ").lower()
    data.value = (teks == "ya")
else:
    print("Pilihan tidak valid!")
    exit()

# Output union
print("\n=== HASIL UNION ===")
print("Isi data:", data.value)
print("Tipe data:", type(data.value))


print("==SETELAH DI MODIFIKASI==")

# Program Konsep UNION Keren dengan Tampilan Berwarna
# Tidak menggunakan import apa pun

# ========== WARNA ==========
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
CYAN    = "\033[36m"
MAGENTA = "\033[35m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

# ========== CLASS UNION ==========
class UnionKeren:
    def __init__(self):
        self.value = None   # satu variabel untuk semua jenis data

# Membuat objek union
data = UnionKeren()

# ========== HEADER ==========
print(BOLD + CYAN + "╔══════════════════════════════════════╗")
print("║        PROGRAM UNION BERWARNA        ║")
print("╚══════════════════════════════════════╝" + RESET)

print(BLUE + "Pilih tipe data yang ingin Anda masukkan:" + RESET)
print(GREEN + "1. Angka Bulat (int)")
print("2. Angka Desimal (float)")
print("3. Teks (string)")
print("4. Ya / Tidak (boolean)" + RESET)
print(CYAN + "──────────────────────────────────────────" + RESET)

pilihan = input(YELLOW + "Masukkan pilihan (1/2/3/4): " + RESET)

# ========== LOGIKA UNION ==========
if pilihan == "1":
    data.value = int(input(GREEN + "Masukkan angka bulat: " + RESET))

elif pilihan == "2":
    data.value = float(input(GREEN + "Masukkan angka desimal: " + RESET))

elif pilihan == "3":
    data.value = input(GREEN + "Masukkan teks: " + RESET)

elif pilihan == "4":
    masuk = input(GREEN + "Masukkan (ya/tidak): " + RESET).lower()
    data.value = (masuk == "ya")

else:
    print(RED + "Pilihan tidak valid!" + RESET)
    exit()

# ========== HASIL OUTPUT ==========
print()
print(BOLD + MAGENTA + "╔══════════════════════════════╗")
print("║          HASIL UNION          ║")
print("╚══════════════════════════════╝" + RESET)

print(CYAN + "Isi Data  : " + RESET + f"{data.value}")
print(CYAN + "Tipe Data : " + RESET + f"{type(data.value)}")

print(MAGENTA + "----------------------------------------" + RESET)
print(GREEN + BOLD + "Data berhasil disimpan dalam satu variabel UNION!" + RESET)

