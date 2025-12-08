# Fungsi pencabangan sederhana untuk menentukan kategori usia
def kategori_usia(usia):
    if usia < 0:
        return "Usia tidak valid (negatif)"
    elif usia < 13:
        return "Anak-anak"
    elif usia < 20:
        return "Remaja"
    elif usia < 65:
        return "Dewasa"
    else:
        return "Lansia"

# Contoh penggunaan
usia_input = int(input("Masukkan usia Anda: "))
kategori = kategori_usia(usia_input)
print(f"Kategori usia Anda: {kategori}")

print("==SETELAH DI MODIFIKASI==")

from colorama import init, Fore, Style  # Impor untuk menambahkan warna

# Inisialisasi colorama
init(autoreset=True)

# Fungsi untuk menentukan kategori usia dengan pesan tambahan
def kategori_usia(usia):
    if usia < 0:
        return Fore.RED + "Usia tidak valid (negatif). Coba masukkan angka positif!", ""
    elif usia < 13:
        kategori = Fore.GREEN + "Anak-anak"
        pesan = Fore.BLUE + "Waktunya bermain dan belajar hal baru! Ingat, masa kecil adalah fondasi masa depan."
        return kategori, pesan
    elif usia < 20:
        kategori = Fore.GREEN + "Remaja"
        pesan = Fore.BLUE + "Energi muda untuk eksplorasi! Jaga kesehatan dan fokus pada impianmu."
        return kategori, pesan
    elif usia < 65:
        kategori = Fore.GREEN + "Dewasa"
        pesan = Fore.BLUE + "Waktunya berkontribusi! Seimbangkan karier, keluarga, dan hobi untuk hidup bahagia."
        return kategori, pesan
    else:
        kategori = Fore.GREEN + "Lansia"
        pesan = Fore.BLUE + "Pengalaman berharga! Bagikan hikmahmu dan nikmati masa pensiun dengan tenang."
        return kategori, pesan

# Loop utama untuk input berulang
print(Fore.CYAN + "Selamat datang di Program Kategori Usia!" + Style.RESET_ALL)
print("Masukkan usia Anda, atau ketik 'keluar' untuk berhenti.\n")

while True:
    usia_input = input(Fore.YELLOW + "Masukkan usia Anda: " + Style.RESET_ALL)
    
    if usia_input.lower() == 'keluar':
        print(Fore.MAGENTA + "Terima kasih. Sampai jumpa!" + Style.RESET_ALL)
        break
    
    try:
        usia = int(usia_input)
        kategori, pesan = kategori_usia(usia)
        print(f"Kategori usia Anda: {kategori}")
        if pesan:
            print(f"Pesan untuk Anda: {pesan}")
        print("-" * 50)  # Garis pemisah untuk lebih rapi
    except ValueError:
        print(Fore.RED + "Input tidak valid. Harap masukkan angka atau 'keluar'." + Style.RESET_ALL)
        print("-" * 50)


      # Fungsi perulangan untuk game menebak angka (angka rahasia tetap: 42)
def game_tebak_angka():
    print("Selamat datang di Game Tebak Angka!")
    print("Saya akan memikirkan angka antara 1 sampai 100. Coba tebak!")
    print("Petunjuk: Angka ini adalah 42 (untuk demo, tapi jangan curang ya!).\n")
    
    angka_rahasia = 42  # Angka tetap tanpa random
    percobaan = 0
    maks_percobaan = 10  # Batas percobaan
    
    while percobaan < maks_percobaan:
        try:
            tebakan = int(input(f"Tebakan Anda (percobaan {percobaan + 1}/{maks_percobaan}): "))
            percobaan += 1
            
            if tebakan < angka_rahasia:
                print("Terlalu kecil! Coba angka yang lebih besar.")
                # Loop for untuk menampilkan petunjuk angka yang mungkin lebih besar
                print("Angka yang mungkin: ", end="")
                for i in range(tebakan + 1, tebakan + 6):  # Contoh petunjuk 5 angka berikutnya
                    print(i, end=" ")
                print()
            elif tebakan > angka_rahasia:
                print("Terlalu besar! Coba angka yang lebih kecil.")
                # Loop for untuk menampilkan petunjuk angka yang mungkin lebih kecil
                print("Angka yang mungkin: ", end="")
                for i in range(max(1, tebakan - 5), tebakan):  # Contoh petunjuk 5 angka sebelumnya
                    print(i, end=" ")
                print()
            else:
                print(f"Selamat! Anda menebak benar dalam {percobaan} percobaan.")
                break
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
    
    if percobaan == maks_percobaan:
        print(f"Maaf, Anda kehabisan percobaan. Angka rahasianya adalah {angka_rahasia}.")
    
    # Opsi ulang permainan
    ulang = input("Mau main lagi? (ya/tidak): ").lower()
    if ulang == 'ya':
        print("\n" + "-" * 50)
        game_tebak_angka()  # Rekursi untuk ulang
    else:
        print("Terima kasih telah bermain! Sampai jumpa.")

# Jalankan game
game_tebak_angka()


print("==SETELAH DI MODIFIKASI==")

# Fungsi untuk menampilkan teks berwarna menggunakan ANSI codes
def warna(teks, kode):
    return f"\033[{kode}m{teks}\033[0m"  # Reset warna di akhir

# Fungsi untuk animasi typing (efek mengetik)
def animasi_teks(teks, kode_warna=0, delay=50000):
    for char in teks:
        print(warna(char, kode_warna), end="", flush=True)
        for _ in range(delay): pass  # Delay simulasi
    print()

# Fungsi untuk progress bar
def progress_bar(sekarang, maks, panjang=20):
    filled = int(panjang * sekarang / maks)
    bar = "#" * filled + "-" * (panjang - filled)
    return f"[{bar}] {sekarang}/{maks}"

# ASCII Art untuk header
def ascii_header():
    print(warna("""
    ████████╗███████╗██████╗  █████╗ ██╗  ██╗     █████╗ ███╗   ██╗ ██████╗ ██╗  ██╗ █████╗
    ╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██║ ██╔╝    ██╔══██╗████╗  ██║██╔════╝ ██║ ██╔╝██╔══██╗
       ██║   █████╗  ██████╔╝███████║█████╔╝     ███████║██╔██╗ ██║██║  ███╗█████╔╝ ███████║
       ██║   ██╔══╝  ██╔══██╗██╔══██║██╔═██╗     ██╔══██║██║╚██╗██║██║   ██║██╔═██╗ ██╔══██║
       ██║   ███████╗██████╔╝██║  ██║██║  ██╗    ██║  ██║██║ ╚████║╚██████╔╝██║  ██╗██║  ██║
       ╚═╝   ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
    """, 94))  # Biru

# ASCII Art untuk sukses
def ascii_sukses():
    print(warna("""
       🎉
     /\_/\  
    ( o.o ) 
     > ^ <
    """, 92))  # Hijau

# ASCII Art untuk gagal
def ascii_gagal():
    print(warna("""
       😢
     /\_/\  
    ( x.x ) 
     > ^ <
    """, 91))  # Merah

# List fakta angka dengan ikon
fakta_angka = [
    "🔢 Angka 42 adalah 'Jawaban untuk Semua' dari novel The Hitchhiker's Guide to the Galaxy!",
    "🔍 Angka prima adalah angka yang hanya bisa dibagi oleh 1 dan dirinya sendiri.",
    "🍀 Angka 7 sering dianggap angka keberuntungan di banyak budaya.",
    "📈 Bilangan Fibonacci dimulai dari 0, 1, 1, 2, 3, 5, dll.",
    "💯 Angka 100 adalah dasar sistem desimal kita."
]

# Fungsi utama untuk game menebak angka
def game_tebak_angka():
    ascii_header()
    animasi_teks("Selamat datang di Game Tebak Angka Super! 😊", 94, 30000)
    animasi_teks("Saya akan memikirkan angka antara 1 sampai 100. Pilih level kesulitan dulu!", 94, 30000)
    print()
    
    # Pilih level
    while True:
        level = input(warna("🎯 Pilih level (mudah/sedang/sulit): ", 93)).lower()
        if level == "mudah":
            maks_percobaan = 15
            break
        elif level == "sedang":
            maks_percobaan = 10
            break
        elif level == "sulit":
            maks_percobaan = 5
            break
        else:
            animasi_teks("❌ Level tidak valid. Pilih mudah, sedang, atau sulit.", 91, 20000)
    
    angka_rahasia = 42  # Angka tetap untuk demo
    
    # Animasi loading
    animasi_teks("🤔 Memikirkan angka...", 94, 50000)
    for i in range(3, 0, -1):
        print(warna(f"⏳ {i}...", 93), end=" ")
        for _ in range(200000): pass  # Delay
    animasi_teks("🚀 Siap! Mulai tebak! 🔥", 92, 30000)
    
    percobaan = 0
    skor = 100
    
    while percobaan < maks_percobaan:
        # Tampilkan progress bar
        print(warna(f"📊 Progress: {progress_bar(percobaan, maks_percobaan)}", 95))
        
        try:
            tebakan = int(input(warna(f"🎲 Tebakan Anda (skor: {skor}): ", 93)))
            percobaan += 1
            skor -= 5
            
            if tebakan < angka_rahasia:
                animasi_teks("⬇️ Terlalu kecil! Coba angka yang lebih besar. 😅", 91, 20000)
                # Petunjuk dalam grid sederhana
                print(warna("🔍 Angka yang mungkin:", 94))
                for i in range(tebakan + 1, min(tebakan + 11, 101), 5):  # Grid 5 kolom
                    row = " ".join(str(j) for j in range(i, min(i + 5, min(tebakan + 11, 101))))
                    print(warna(f"  {row}", 92))
            elif tebakan > angka_rahasia:
                animasi_teks("⬆️ Terlalu besar! Coba angka yang lebih kecil. 😅", 91, 20000)
                print(warna("🔍 Angka yang mungkin:", 94))
                for i in range(max(1, tebakan - 10), tebakan, 5):
                    row = " ".join(str(j) for j in range(i, min(i + 5, tebakan)))
                    print(warna(f"  {row}", 92))
            else:
                skor += 50
                ascii_sukses()
                animasi_teks(f"🎊 Selamat! Anda menebak benar dalam {percobaan} percobaan. Skor akhir: {skor} 🏆", 92, 30000)
                break
            
            # Tampilkan fakta
            fakta = fakta_angka[percobaan % len(fakta_angka)]
            animasi_teks(f"💡 {fakta}", 94, 40000)
            print("-" * 60)
        
        except ValueError:
            animasi_teks("❌ Input tidak valid. Harap masukkan angka. 🔢", 91, 20000)
    
    if percobaan == maks_percobaan:
        skor = max(0, skor - 20)
        ascii_gagal()
        animasi_teks(f"😔 Maaf, Anda kehabisan percobaan. Angka rahasianya adalah {angka_rahasia}. Skor akhir: {skor}", 91, 30000)
    
    # Statistik akhir
    print(warna(f"\n📈 Statistik: Percobaan: {percobaan}, Level: {level.capitalize()}, Skor: {skor}", 95))
    
    # Opsi ulang
    ulang = input(warna("🔄 Mau main lagi? (ya/tidak): ", 93)).lower()
    if ulang == 'ya':
        print("\n" + "=" * 60)
        game_tebak_angka()
    else:
        animasi_teks("👋 Terima kasih telah bermain! Sampai jumpa. 🌟", 95, 30000)

# Jalankan game
game_tebak_angka()

