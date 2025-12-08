# =======================================================
#                PROGRAM MERGE SORT BERWARNA
# =======================================================

# WARNA-WARNA (TANPA IMPORT)
MERAH   = "\033[31m"
HIJAU   = "\033[32m"
KUNING  = "\033[33m"
BIRU    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
PUTIH   = "\033[37m"
RESET   = "\033[0m"

# GARIS FRAME
def garis():
    print(MAGENTA + "=" * 55 + RESET)

# -------------------------------------------------------
#                FUNGSI MERGE SORT
# -------------------------------------------------------
def merge_sort(data, depth=0):
    indent = "   " * depth  # indentasi untuk tampilan bertingkat

    # Jika hanya satu elemen → sudah terurut
    if len(data) <= 1:
        print(indent + HIJAU + f"✓ Data {data} sudah terurut (basis)" + RESET)
        return data

    # Tentukan titik tengah
    mid = len(data) // 2
    kiri = data[:mid]
    kanan = data[mid:]

    # Tampilkan proses pemisahan
    print(indent + BIRU + f"Memisahkan: {data}" + RESET)
    print(indent + CYAN + f" → Kiri : {kiri}" + RESET)
    print(indent + CYAN + f" → Kanan: {kanan}" + RESET)

    # Rekursif pada kiri & kanan
    kiri_sorted = merge_sort(kiri, depth + 1)
    kanan_sorted = merge_sort(kanan, depth + 1)

    # Proses penggabungan
    print(indent + KUNING + f"Menggabungkan {kiri_sorted} + {kanan_sorted}" + RESET)

    merged = []
    i = j = 0

    # Bandingkan & masukkan nilai
    while i < len(kiri_sorted) and j < len(kanan_sorted):
        if kiri_sorted[i] < kanan_sorted[j]:
            merged.append(kiri_sorted[i])
            print(indent + HIJAU + f" - Ambil {kiri_sorted[i]} dari kiri" + RESET)
            i += 1
        else:
            merged.append(kanan_sorted[j])
            print(indent + HIJAU + f" - Ambil {kanan_sorted[j]} dari kanan" + RESET)
            j += 1

    # Masukkan sisa elemen
    while i < len(kiri_sorted):
        merged.append(kiri_sorted[i])
        print(indent + MERAH + f" - Sisa kiri → {kiri_sorted[i]}" + RESET)
        i += 1

    while j < len(kanan_sorted):
        merged.append(kanan_sorted[j])
        print(indent + MERAH + f" - Sisa kanan → {kanan_sorted[j]}" + RESET)
        j += 1

    print(indent + MAGENTA + f"✔ Hasil gabungan: {merged}" + RESET)
    return merged


# -------------------------------------------------------
#                        MAIN
# -------------------------------------------------------
garis()
print(CYAN + "           PROGRAM MERGE SORT — BERWARNA" + RESET)
garis()

print(HIJAU + "Masukkan beberapa angka acak, pisahkan dengan spasi." + RESET)
data = list(map(int, input(MAGENTA + "Input data: " + RESET).split()))

garis()
print(BIRU + "Data sebelum diurutkan: " + RESET, data)
garis()

# Jalankan merge sort dengan tampilan detail
hasil = merge_sort(data)

garis()
print(KUNING + "HASIL AKHIR SETELAH MERGE SORT:" + RESET, hasil)
garis()
print(CYAN + "                 S E L E S A I" + RESET)
garis()
