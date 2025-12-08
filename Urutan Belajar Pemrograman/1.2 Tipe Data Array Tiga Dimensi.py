# Deklarasikan array 3D dengan ukuran 2x2x2 (misalnya, kubus kecil)
array_3d = [
    [
        [1, 2],  # Layer 0, Baris 0
        [3, 4]   # Layer 0, Baris 1
    ],
    [
        [5, 6],  # Layer 1, Baris 0
        [7, 8]   # Layer 1, Baris 1
    ]
]

# Cetak elemen array
print("Elemen array 3D:")
for i in range(2):  # Loop untuk layer (dimensi pertama)
    for j in range(2):  # Loop untuk baris (dimensi kedua)
        for k in range(2):  # Loop untuk kolom (dimensi ketiga)
            print(f"array_3d[{i}][{j}][{k}] = {array_3d[i][j][k]}")

print ("==SETELAH DI MODIFIKASI==")

import colorama
from colorama import Fore, Style

# Inisialisasi colorama untuk warna di terminal
colorama.init(autoreset=True)

# Deklarasikan array 3D dengan ukuran 2x2x2 (misalnya, kubus kecil)
array_3d = [
    [
        [1, 2],  # Layer 0, Baris 0
        [3, 4]   # Layer 0, Baris 1
    ],
    [
        [5, 6],  # Layer 1, Baris 0
        [7, 8]   # Layer 1, Baris 1
    ]
]

# Fungsi untuk mencetak header yang menarik
def print_header():
    print(Fore.CYAN + Style.BRIGHT + "🌟 Eksplorasi Array 3D: Kubus Ajaib! 🌟" + Style.RESET_ALL)
    print(Fore.YELLOW + "Bayangkan ini sebagai kubus 2x2x2 di ruang 3D.\n" + Style.RESET_ALL)

# Cetak header
print_header()

# Cetak elemen array dengan warna-warni dan format menarik
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.MAGENTA]  # Warna untuk setiap layer
for i in range(2):  # Loop untuk layer (dimensi pertama)
    print(Fore.WHITE + Style.BRIGHT + f"\n--- Layer {i} ---" + Style.RESET_ALL)
    for j in range(2):  # Loop untuk baris (dimensi kedua)
        row = ""
        for k in range(2):  # Loop untuk kolom (dimensi ketiga)
            value = array_3d[i][j][k]
            color = colors[i % len(colors)]  # Ganti warna per layer
            row += f"{color}[{j}][{k}]={value}{Style.RESET_ALL} "
        print(row.strip())
