# ======================================
# PROGRAM PERANCANGAN STRUKTUR
# Analisis Nilai Akhir Siswa
# ======================================

print("=== PROGRAM NILAI AKHIR SISWA ===")

# ---- INPUT ----
nama = input("Masukkan nama siswa : ")
tugas = float(input("Masukkan nilai tugas : "))
uts = float(input("Masukkan nilai UTS   : "))
uas = float(input("Masukkan nilai UAS   : "))

# ---- PROSES ----
# Rumus nilai akhir (contoh)
nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

# Menentukan grade
if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 75:
    grade = "B"
elif nilai_akhir >= 65:
    grade = "C"
elif nilai_akhir >= 55:
    grade = "D"
else:
    grade = "E"

# ---- OUTPUT ----
print("\n=== HASIL PERHITUNGAN ===")
print("+-----------------------------+")
print(f"| Nama Siswa : {nama}")
print(f"| Nilai Akhir: {nilai_akhir:.2f}")
print(f"| Grade      : {grade}")
print("+-----------------------------+")

print ("==SETELAH DI MODIFIKASI==")

# ============================================================
# 🌟 PROGRAM NILAI AKHIR SISWA - Versi Super Detail & Berwarna
# ============================================================

# KODE WARNA ANSI
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[96m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
RED     = "\033[91m"
MAGENTA = "\033[95m"
BLUE    = "\033[94m"
WHITE   = "\033[97m"

# ============================================================
# HEADER PROGRAM
# ============================================================
print(f"{BOLD}{CYAN}==============================================================")
print(f"                🌟 PROGRAM PERHITUNGAN NILAI AKHIR 🌟")
print(f"=============================================================={RESET}")

print(f"{BLUE}Program ini digunakan untuk menghitung nilai akhir siswa")
print("dengan bobot penilaian sebagai berikut:")
print(f" - {GREEN}Tugas 30%")
print(f" - {YELLOW}UTS   30%")
print(f" - {MAGENTA}UAS   40%{RESET}")

print(f"{CYAN}--------------------------------------------------------------{RESET}")

# ============================================================
# INPUT DATA
# ============================================================
print(f"{BOLD}{WHITE}📥 MASUKKAN DATA SISWA:{RESET}")

nama  = input(f"{GREEN}• Nama siswa          : {RESET}")
tugas = float(input(f"{GREEN}• Nilai tugas (0-100) : {RESET}"))
uts   = float(input(f"{GREEN}• Nilai UTS   (0-100) : {RESET}"))
uas   = float(input(f"{GREEN}• Nilai UAS   (0-100) : {RESET}"))

print(f"{CYAN}--------------------------------------------------------------{RESET}")

# ============================================================
# PROSES PERHITUNGAN
# ============================================================
nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

# MENENTUKAN GRADE + WARNA
if nilai_akhir >= 85:
    grade = f"{GREEN}A{RESET}"
    keterangan = f"{GREEN}Istimewa — Pertahankan prestasimu!{RESET}"
elif nilai_akhir >= 75:
    grade = f"{CYAN}B{RESET}"
    keterangan = f"{CYAN}Baik — Masih bisa ditingkatkan.{RESET}"
elif nilai_akhir >= 65:
    grade = f"{YELLOW}C{RESET}"
    keterangan = f"{YELLOW}Cukup — Perlu usaha lebih.{RESET}"
elif nilai_akhir >= 55:
    grade = f"{MAGENTA}D{RESET}"
    keterangan = f"{MAGENTA}Kurang — Harus belajar lebih giat.{RESET}"
else:
    grade = f"{RED}E{RESET}"
    keterangan = f"{RED}Sangat Kurang — Bimbingan diperlukan.{RESET}"

# ============================================================
# OUTPUT TABEL HASIL
# ============================================================
print(f"{BOLD}{CYAN}========================= HASIL AKHIR ========================={RESET}")
print(f"{BOLD}{WHITE}+------------------------------------------------------------+{RESET}")
print(f"| {YELLOW}Nama Siswa {RESET:14}: {nama:<30} |")
print(f"| {YELLOW}Nilai Tugas{RESET:14}: {tugas:<30} |")
print(f"| {YELLOW}Nilai UTS  {RESET:14}: {uts:<30} |")
print(f"| {YELLOW}Nilai UAS  {RESET:14}: {uas:<30} |")
print(f"+------------------------------------------------------------+")
print(f"| {GREEN}Nilai Akhir{RESET:13}: {nilai_akhir:<30.2f} |")
print(f"| {GREEN}Grade       {RESET:13}: {grade:<30} |")
print(f"+------------------------------------------------------------+")

# ============================================================
# KETERANGAN TAMBAHAN
# ============================================================
print(f"\n{BOLD}{BLUE}📘 KETERANGAN:{RESET}")
print(f"{keterangan}")

# ============================================================
# FOOTER
# ============================================================
print(f"\n{CYAN}--------------------------------------------------------------{RESET}")
print(f"{BOLD}{MAGENTA}Terima kasih telah menggunakan program ini! Semangat belajar! ✨{RESET}")
print(f"{CYAN}=============================================================={RESET}")
