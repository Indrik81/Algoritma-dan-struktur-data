# Program Pengurutan Data (Bubble Sort) STRING dengan Tampilan Berwarna
# Menggunakan ANSI Color (tanpa import)

# Warna ANSI
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(CYAN + "===============================================" + RESET)
print(BIRU + "   PROGRAM PENGURUTAN STRING - BUBBLE SORT    " + RESET)
print(CYAN + "===============================================" + RESET)

# Input jumlah data
jumlah = int(input(KUNING + "Masukkan jumlah data: " + RESET))

data = []

# Input data bertipe STRING
print(HIJAU + "\n=== Masukkan Data (STRING) ===\n" + RESET)
for i in range(jumlah):
    teks = input(f"{CYAN}Data ke-{i+1}: {RESET}")
    data.append(teks)

print(MERAH + "\nData sebelum diurutkan:" + RESET, data)

# ===========================
#        BUBBLE SORT
# ===========================
print(KUNING + "\n>>> Proses Pengurutan Bubble Sort STRING...\n" + RESET)

for i in range(len(data) - 1):
    for j in range(0, len(data) - i - 1):
        
        print(f"{BIRU}Membandingkan{RESET} '{data[j]}' {MERAH}dengan{RESET} '{data[j+1]}'")

        # Perbandingan string (alfabetis)
        if data[j].lower() > data[j + 1].lower():
            print(HIJAU + "   → Ditukar!" + RESET)
            data[j], data[j + 1] = data[j + 1], data[j]
        else:
            print(MERAH + "   → Tidak perlu ditukar" + RESET)

        print("   Kondisi sementara:", data)
    print()

print(CYAN + "===============================================" + RESET)
print(HIJAU + "Data setelah diurutkan (Bubble Sort STRING):" + RESET, data)
print(CYAN + "===============================================" + RESET)
