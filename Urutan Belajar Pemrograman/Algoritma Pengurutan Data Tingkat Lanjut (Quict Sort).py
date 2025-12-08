# =======================================================
#                PROGRAM QUICK SORT BERWARNA
# =======================================================

# WARNA (TANPA IMPORT)
MERAH   = "\033[31m"
HIJAU   = "\033[32m"
KUNING  = "\033[33m"
BIRU    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
RESET   = "\033[0m"


# -------------------------------------------------------
#                 FUNGSI QUICK SORT
# -------------------------------------------------------
def quick_sort(data, depth=0):
    indent = "   " * depth  # indentasi tampilan rekursi

    # Basis: jika hanya 1 elemen, langsung kembalikan
    if len(data) <= 1:
        print(indent + HIJAU + f"✓ Data {data} sudah terurut (basis)" + RESET)
        return data

    # Ambil pivot (pakai elemen terakhir)
    pivot = data[-1]

    print(indent + BIRU + f"Memproses: {data}" + RESET)
    print(indent + KUNING + f"Pivot dipilih: {pivot}" + RESET)

    kiri = []   # elemen < pivot
    tengah = [] # elemen == pivot
    kanan = []  # elemen > pivot

    # Pemisahan data
    for angka in data:
        if angka < pivot:
            kiri.append(angka)
            print(indent + CYAN + f" → {angka} masuk ke kiri" + RESET)
        elif angka == pivot:
            tengah.append(angka)
            print(indent + MAGENTA + f" → {angka} sama dengan pivot" + RESET)
        else:
            kanan.append(angka)
            print(indent + MERAH + f" → {angka} masuk ke kanan" + RESET)

    print(indent + HIJAU + f"Hasil pemisahan:" + RESET)
    print(indent + CYAN + f" Kiri  : {kiri}" + RESET)
    print(indent + MAGENTA + f" Tengah: {tengah}" + RESET)
    print(indent + MERAH + f" Kanan : {kanan}" + RESET)
    print()

    # Rekursif Quick Sort
    kiri_sorted = quick_sort(kiri, depth + 1)
    kanan_sorted = quick_sort(kanan, depth + 1)

    # Gabungkan seluruh bagian
    hasil = kiri_sorted + tengah + kanan_sorted

    print(indent + HIJAU + f"✔ Gabungan akhir level ini: {hasil}" + RESET)
    return hasil


# -------------------------------------------------------
#                        MAIN
# -------------------------------------------------------
print(MAGENTA + "=" * 55 + RESET)
print(CYAN + "           PROGRAM QUICK SORT — BERWARNA" + RESET)
print(MAGENTA + "=" * 55 + RESET)

print(HIJAU + "Masukkan angka dipisah spasi untuk diurutkan." + RESET)
data = list(map(int, input(BIRU + "Input data: " + RESET).split()))

print(MAGENTA + "=" * 55 + RESET)
print(KUNING + "Data sebelum diurutkan:" + RESET, data)
print(MAGENTA + "=" * 55 + RESET)

# Proses Quick Sort
hasil = quick_sort(data)

print(MAGENTA + "=" * 55 + RESET)
print(CYAN + "HASIL AKHIR QUICK SORT:" + RESET, hasil)
print(MAGENTA + "=" * 55 + RESET)
print(BIRU + "                    S E L E S A I" + RESET)
print(MAGENTA + "=" * 55 + RESET)
