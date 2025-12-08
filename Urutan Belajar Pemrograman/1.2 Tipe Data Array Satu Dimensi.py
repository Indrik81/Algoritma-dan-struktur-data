# Array untuk menyimpan daftar harga
harga_barang = []

# Input jumlah barang
jumlah = int(input("Masukkan jumlah barang: "))

# Input nama dan harga barang
for i in range(jumlah):
    nama = input(f"Masukkan nama barang ke-{i+1}: ")
    harga = float(input("Masukkan harga barang: "))
    
    # Gabungkan nama + harga jadi satu string
    data = f"{nama} - Rp{harga}"
    harga_barang.append(data)

# Tampilkan hasil
print("\nDaftar Harga Barang:")
for item in harga_barang:
    print(item)

print ("==SETELAH DI MODIFIKASI==")

# Warna teks menggunakan ANSI Escape
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Array untuk menyimpan daftar harga
harga_barang = []

print(f"{CYAN}=== DAFTAR HARGA BARANG ==={RESET}")

# Input jumlah barang
jumlah = int(input(f"{BIRU}Masukkan jumlah barang: {RESET}"))

# Input nama dan harga barang
for i in range(jumlah):
    print(f"\n{KUNING}--- Input Barang ke-{i+1} ---{RESET}")
    
    nama = input(f"{BIRU}Masukkan nama barang: {RESET}")
    harga = float(input(f"{BIRU}Masukkan harga barang: Rp {RESET}"))
    
    # Simpan sebagai tuple (nama, harga)
    data = (nama, harga)
    harga_barang.append(data)

# Tampilkan hasil
print(f"\n{CYAN}======= DAFTAR HARGA BARANG ======={RESET}")

for nama, harga in harga_barang:
    print(f"{HIJAU}{nama:<15}{RESET} : {MERAH}Rp{harga:,.0f}{RESET}")

print(f"{CYAN}===================================={RESET}")
print(f"\n{CYAN}======= TOKO SYUKUR SELALU ======={RESET}")


