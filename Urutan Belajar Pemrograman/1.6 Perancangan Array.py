# Program Perancangan Array 1 Dimensi (Barang Gudang)

print("=== Program Pendataan Barang Gudang ===")

barang = []

jumlah = int(input("Masukkan jumlah barang: "))

for i in range(jumlah):
    nama_barang = input(f"Nama barang ke-{i+1}: ")
    barang.append(nama_barang)

print("\n=== Daftar Barang ===")
for i in range(len(barang)):
    print(f"{i+1}. {barang[i]}")
print("\nTerima kasih telah menggunakan program ini!")

print ("==SETELAH DI MODIFIKASI==")

# ============================================================
#        PROGRAM PERANCANGAN ARRAY 1 DIMENSI (BERWARNA)
# ============================================================

# Warna ANSI
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
UNGU = "\033[95m"
CYAN = "\033[96m"
PUTIH = "\033[97m"
RESET = "\033[0m"

# Judul Program
print(CYAN + "===========================================================" + RESET)
print(HIJAU + "               PROGRAM PENDATAAN BARANG GUDANG" + RESET)
print(CYAN + "===========================================================" + RESET)

# Array Barang
barang = []

# Input jumlah barang
print()
jumlah = int(input(KUNING + "Masukkan jumlah barang yang ingin dicatat: " + RESET))

print()
for i in range(jumlah):
    print(BIRU + f"--- Input Barang ke-{i+1} ---" + RESET)
    nama_barang = input(HIJAU + "Nama barang : " + RESET)
    barang.append(nama_barang)
    print(CYAN + "Barang berhasil ditambahkan!\n" + RESET)

# Tampilkan daftar barang
print(UNGU + "\n===================== DAFTAR BARANG =====================" + RESET)

# Header tabel
print(BIRU + "+---------+------------------------------+" + RESET)
print(
    BIRU + "|" + RESET +
    PUTIH + " No".ljust(7) + RESET +
    BIRU + "|" + RESET +
    PUTIH + " Nama Barang".ljust(28) + RESET +
    BIRU + "|" + RESET
)
print(BIRU + "+---------+------------------------------+" + RESET)

# Isi tabel
for i in range(len(barang)):
    print(
        BIRU + "|" + RESET +
        KUNING + f" {i+1}".ljust(7) + RESET +
        BIRU + "|" + RESET +
        HIJAU + f" {barang[i]}".ljust(28) + RESET +
        BIRU + "|" + RESET
    )

# Footer tabel
print(BIRU + "+---------+------------------------------+" + RESET)

# Pesan akhir
print(CYAN + "\nTerima kasih telah menggunakan program ini!" + RESET)
