# Program Variabel Dinamis Sederhana

print("=== Program Variabel Dinamis ===")

# Tempat menyimpan variabel
variabel_dinamis = {}

# Input jumlah variabel
jumlah = int(input("Masukkan jumlah variabel yang ingin dibuat: "))

# Input nama variabel dan nilainya
for i in range(jumlah):
    nama = input(f"Masukkan nama variabel ke-{i+1}: ")
    nilai = input(f"Masukkan nilai untuk '{nama}': ")
    variabel_dinamis[nama] = nilai  # menyimpan secara dinamis

print("\n=== HASIL VARIABEL DINAMIS ===")
for key, value in variabel_dinamis.items():
    print(f"{key} = {value}")

print ("==SETELAH DI MODIFIKASI==")

# ============================================================
#             PROGRAM VARIABEL DINAMIS (VERSI MENARIK)
# ============================================================

# Warna ANSI (tidak butuh import)
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
UNGU = "\033[95m"
CYAN = "\033[96m"
PUTIH = "\033[97m"
RESET = "\033[0m"

# Header Program
print(CYAN + "============================================================" + RESET)
print(HIJAU + "            PROGRAM PEMBUAT VARIABEL DINAMIS" + RESET)
print(CYAN + "============================================================" + RESET)

# Dictionary untuk menyimpan variabel
variabel_dinamis = {}

# Input jumlah
print()
jumlah = int(input(KUNING + "Masukkan jumlah variabel yang ingin dibuat: " + RESET))
print()

# Input data variabel
for i in range(jumlah):
    print(BIRU + f"--- Input Variabel ke-{i+1} ---" + RESET)
    nama = input(HIJAU + "Nama variabel  : " + RESET)
    nilai = input(HIJAU + "Nilai variabel : " + RESET)
    variabel_dinamis[nama] = nilai
    print(CYAN + "Variabel berhasil ditambahkan!\n" + RESET)

# Menampilkan hasil
print(UNGU + "\n=================== HASIL VARIABEL DINAMIS ===================" + RESET)

# Tabel header
print(BIRU + "+----------------------+--------------------------+" + RESET)
print(
    BIRU + "|" + RESET +
    PUTIH + " Nama Variabel".ljust(22) + RESET +
    BIRU + "|" + RESET +
    PUTIH + " Nilai".ljust(26) + RESET +
    BIRU + "|" + RESET
)
print(BIRU + "+----------------------+--------------------------+" + RESET)

# Isi tabel
for key, value in variabel_dinamis.items():
    print(
        BIRU + "|" + RESET +
        KUNING + f" {key}".ljust(22) + RESET +
        BIRU + "|" + RESET +
        HIJAU + f" {value}".ljust(26) + RESET +
        BIRU + "|" + RESET
    )

# Footer tabel
print(BIRU + "+----------------------+--------------------------+" + RESET)

print(CYAN + "\nSelesai! Semua variabel telah berhasil dibuat.\n" + RESET)
