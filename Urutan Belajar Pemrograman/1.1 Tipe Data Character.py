# Program sederhana menggunakan tipe data string (karakter)

# Meminta input nama pengguna (string)
nama = input("Masukkan nama Anda: ")

# Mengubah nama menjadi huruf besar
nama_besar = nama.upper()

# Menghitung panjang string (jumlah karakter)
panjang_nama = len(nama)

# Mencetak hasil
print(f"Nama asli: {nama}")
print(f"Nama dalam huruf Kapital: {nama_besar}")
print(f"Panjang nama: {panjang_nama} karakter")

print ("==SETELAH DI MODIFIKASI==")

# Modifikasi: Menambahkan fitur lebih menarik seperti reverse, hitung vokal, cek palindrom, validasi input, dan WARNA pada teks output

# Fungsi untuk menghitung jumlah vokal dalam string
def hitung_vokal(teks):
    vokal = "aeiouAEIOU"
    return sum(1 for char in teks if char in vokal)

# Kode ANSI untuk warna (bekerja di terminal Unix/Linux/Mac; untuk Windows, install colorama jika perlu)
class Warna:
    MERAH = '\033[31m'
    HIJAU = '\033[32m'
    KUNING = '\033[33m'
    BIRU = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    PUTIH = '\033[37m'
    RESET = '\033[0m'

# Meminta input nama pengguna dengan validasi
while True:
    nama = input("Masukkan nama Anda (minimal 2 karakter): ").strip()
    if len(nama) >= 2 and nama.isalpha():
        break
    else:
        print(f"{Warna.MERAH}Nama harus berupa huruf saja dan minimal 2 karakter. Coba lagi!{Warna.RESET}")

# Manipulasi string
nama_besar = nama.upper()
nama_kecil = nama.lower()
nama_kapital = nama.capitalize()
nama_reverse = nama[::-1]
panjang_nama = len(nama)
jumlah_vokal = hitung_vokal(nama)

# Cek apakah nama adalah palindrom (sama jika dibalik, tanpa memperhatikan huruf besar/kecil)
is_palindrom = nama.lower() == nama_reverse.lower()

# Mencetak hasil dengan format yang menarik dan BERWARNA
print("\n" + Warna.BIRU + "="*50 + Warna.RESET)
print(Warna.CYAN + "ANALISIS NAMA ANDA" + Warna.RESET)
print(Warna.BIRU + "="*50 + Warna.RESET)
print(f"{Warna.HIJAU}Nama asli: {nama}{Warna.RESET}")
print(f"{Warna.KUNING}Nama dalam huruf besar: {nama_besar}{Warna.RESET}")
print(f"{Warna.KUNING}Nama dalam huruf kecil: {nama_kecil}{Warna.RESET}")
print(f"{Warna.KUNING}Nama dengan huruf pertama kapital: {nama_kapital}{Warna.RESET}")
print(f"{Warna.MAGENTA}Nama dibalik: {nama_reverse}{Warna.RESET}")
print(f"{Warna.PUTIH}Panjang nama: {panjang_nama} karakter{Warna.RESET}")
print(f"{Warna.PUTIH}Jumlah huruf vokal: {jumlah_vokal}{Warna.RESET}")
print(f"{Warna.PUTIH}Apakah palindrom? {'Ya' if is_palindrom else 'Tidak'}{Warna.RESET}")
print(Warna.BIRU + "="*50 + Warna.RESET)
print(Warna.HIJAU + "Terima kasih telah menggunakan program ini! 😊" + Warna.RESET)
