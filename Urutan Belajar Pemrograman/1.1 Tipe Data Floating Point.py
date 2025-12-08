# Program untuk menghitung diskon harga barang menggunakan tipe data floating point

# Input harga asli barang (dalam float)
harga_asli = float(input("Masukkan harga asli barang: "))

# Input persentase diskon (dalam float)
persentase_diskon = float(input("Masukkan persentase diskon (contoh: 10 untuk 10%): "))

# Hitung jumlah diskon
jumlah_diskon = harga_asli * (persentase_diskon / 100)

# Hitung harga setelah diskon
harga_setelah_diskon = harga_asli - jumlah_diskon

# Tampilkan hasil
print(f"Harga asli: {harga_asli}")
print(f"Persentase diskon: {persentase_diskon}%")
print(f"Jumlah diskon: {jumlah_diskon}")
print(f"Harga setelah diskon: {harga_setelah_diskon}")

print ("==SETELAH DI MODIFIKASI==")

# Program perhitungan diskon harga barang (tanpa import, memakai ANSI color)

# Kode warna ANSI
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(CYAN + "="*50 + RESET)
print(KUNING + "   PROGRAM PERHITUNGAN DISKON HARGA BARANG" + RESET)
print(CYAN + "="*50 + RESET)

# Input harga asli
harga_asli = float(input(HIJAU + "Masukkan harga asli barang: " + RESET))

# Input persentase diskon
persentase_diskon = float(input(HIJAU + "Masukkan persentase diskon (contoh: 10 untuk 10%): " + RESET))

print(CYAN + "\nMenghitung diskon...\n" + RESET)

# Hitung jumlah diskon
jumlah_diskon = harga_asli * (persentase_diskon / 100)

# Hitung harga setelah diskon
harga_setelah_diskon = harga_asli - jumlah_diskon

# Tampilkan hasil
print(MAGENTA + "-"*50 + RESET)
print(KUNING + f"Harga asli          : Rp {harga_asli:,.2f}" + RESET)
print(KUNING + f"Persentase diskon   : {persentase_diskon}%" + RESET)
print(KUNING + f"Jumlah diskon       : Rp {jumlah_diskon:,.2f}" + RESET)
print(HIJAU + f"Harga setelah diskon: Rp {harga_setelah_diskon:,.2f}" + RESET)
print(MAGENTA + "-"*50 + RESET)

print(CYAN + "\nTerima kasih telah belanja disini!" + RESET)

