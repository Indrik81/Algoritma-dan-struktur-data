# Program Analisis Siswa Menggunakan Array 2 Dimensi dengan Tabel Kotak

# Array 2 dimensi
data_siswa = []

# Input jumlah siswa
jumlah = int(input("Masukkan jumlah siswa: "))

# Input data siswa
for i in range(jumlah):
    print(f"\nData siswa ke-{i+1}")
    nama = input("Masukkan nama siswa: ")
    nilai = float(input("Masukkan nilai siswa: "))

    # Keterangan berdasar nilai
    if nilai >= 90:
        ket = "Sangat Baik"
    elif nilai >= 75:
        ket = "Baik"
    elif nilai >= 60:
        ket = "Cukup"
    else:
        ket = "Kurang"

    data_siswa.append([nama, nilai, ket])

# Membuat tabel kotak
print("\n┌────────────────┬──────────┬──────────────────┐")
print("│     NAMA       │  NILAI   │   KETERANGAN     │")
print("├────────────────┼──────────┼──────────────────┤")

for siswa in data_siswa:
    print(f"│ {siswa[0]:<14} │ {siswa[1]:<8} │ {siswa[2]:<16} │")

print("└────────────────┴──────────┴──────────────────┘")

print ("==SETELAH DI MODIFIKASI==")

# ============================================
#   PROGRAM ANALISIS DATA SISWA (ARRAY 2D)
#   Tabel Garis Rapi & Berwarna
# ============================================

# Kode warna ANSI
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

# Header Program
print(BOLD + CYAN + "✦✦✦ PROGRAM ANALISIS DATA SISWA ✦✦✦" + RESET)

# Array 2D
data_siswa = []

# Input jumlah siswa
jumlah = int(input(YELLOW + "Masukkan jumlah siswa: " + RESET))

# Input data siswa
print(BLUE + "\nMulai input data...\n" + RESET)
for i in range(jumlah):
    print(GREEN + f"➤ Data siswa ke-{i+1}" + RESET)
    nama = input("   Nama siswa  : ")
    nilai = input("   Nilai       : ")
    kelas = input("   Kelas       : ")
    data_siswa.append([nama, nilai, kelas])
    print()

# ============================================
#   MENAMPILKAN TABEL DATA (GARIS RAPI)
# ============================================

print(BOLD + CYAN + "\n✦✦✦ TABEL DATA SISWA ✦✦✦" + RESET)

# Panjang kolom
kol_nama  = 15
kol_nilai = 7
kol_kelas = 8

# Header Tabel
print(BLUE + "┌" + "─"*kol_nama + "┬" + "─"*kol_nilai + "┬" + "─"*kol_kelas + "┐" + RESET)
print(BLUE + "│" + RESET +
      BOLD + WHITE + f"{'NAMA':<{kol_nama}}" + RESET +
      BLUE + "│" + RESET +
      BOLD + WHITE + f"{'NILAI':<{kol_nilai}}" + RESET +
      BLUE + "│" + RESET +
      BOLD + WHITE + f"{'KELAS':<{kol_kelas}}" + RESET +
      BLUE + "│" + RESET)
print(BLUE + "├" + "─"*kol_nama + "┼" + "─"*kol_nilai + "┼" + "─"*kol_kelas + "┤" + RESET)

# Isi tabel
for siswa in data_siswa:
    print(BLUE + "│" + RESET +
          GREEN + f"{siswa[0]:<{kol_nama}}" + RESET +
          BLUE + "│" + RESET +
          YELLOW + f"{siswa[1]:<{kol_nilai}}" + RESET +
          BLUE + "│" + RESET +
          MAGENTA + f"{siswa[2]:<{kol_kelas}}" + RESET +
          BLUE + "│" + RESET)

# Footer
print(BLUE + "└" + "─"*kol_nama + "┴" + "─"*kol_nilai + "┴" + "─"*kol_kelas + "┘" + RESET)

# ============================================
#   ANALISIS DATA SEDERHANA
# ============================================

print(BOLD + CYAN + "\n✦✦✦ HASIL ANALISIS DATA SISWA ✦✦✦" + RESET)

nilai_angka = []
for d in data_siswa:
    try:
        nilai_angka.append(int(d[1]))
    except:
        nilai_angka.append(0)

tertinggi = max(nilai_angka)
index_tinggi = nilai_angka.index(tertinggi)
nama_tertinggi = data_siswa[index_tinggi][0]

print(GREEN + f"✔ Siswa dengan nilai tertinggi : {nama_tertinggi} ({tertinggi})" + RESET)
print(YELLOW + f"✔ Total siswa: {len(data_siswa)}" + RESET)
print(CYAN + "✔ Analisis selesai.\n" + RESET)

print(BOLD + CYAN + "✦ Terima kasih! ✦" + RESET)
