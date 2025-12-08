# Program Pengurutan Data (Selection Sort) dengan Tampilan Berwarna
# Menggunakan ANSI Color (tanpa import)

# Warna ANSI
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(CYAN + "===============================================" + RESET)
print(BIRU + "        PROGRAM PENGURUTAN DATA - SELECTION SORT" + RESET)
print(CYAN + "===============================================" + RESET)

# Input jumlah data
n = int(input(KUNING + "Masukkan jumlah data: " + RESET))

data = []

print(HIJAU + "\n=== Masukkan Data ===\n" + RESET)
for i in range(n):
    angka = int(input(f"{CYAN}Data ke-{i+1}: {RESET}"))
    data.append(angka)

print(MERAH + "\nData sebelum diurutkan:" + RESET, data)
print(KUNING + "\n>>> Proses Selection Sort sedang berlangsung...\n" + RESET)

# ===========================
#      SELECTION SORT
# ===========================
for i in range(len(data)):
    min_index = i
    print(BIRU + f"Langkah {i+1}: Mencari nilai terkecil dari indeks {i} ke akhir" + RESET)

    for j in range(i+1, len(data)):
        print(f"  Membandingkan {data[min_index]} {MERAH}dengan{RESET} {data[j]}")
        if data[j] < data[min_index]:
            print(HIJAU + f"   → {data[j]} menjadi nilai terkecil baru" + RESET)
            min_index = j

    # Tukar jika ada nilai lebih kecil
    if min_index != i:
        print(KUNING + f"   >>> Menukar {data[i]} dengan {data[min_index]}" + RESET)
        data[i], data[min_index] = data[min_index], data[i]
    else:
        print(HIJAU + "   Tidak ada nilai yang lebih kecil, tidak perlu ditukar" + RESET)

    print("  Kondisi sementara:", data, "\n")

print(CYAN + "===============================================" + RESET)
print(HIJAU + "Data setelah diurutkan (Selection Sort):" + RESET, data)
print(CYAN + "===============================================" + RESET)
