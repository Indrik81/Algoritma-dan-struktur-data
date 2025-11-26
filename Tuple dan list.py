#Perbedaan tuple dan lis yaitu tuple tidak dapat diubah setelah dibuat, tuple ini menggunakan tanda ( )
sementara list dapat diubah dan menggunakan tanda [ ]

# Membuat tuple
koordinat = (10, 20, 30)

# Mengakses elemen (hanya baca)
print(koordinat[0])  # Output: 10

# Tidak bisa mengubah elemen (akan error jika dicoba)
# koordinat[0] = 15  # TypeError: 'tuple' object does not support item assignment

# Tuple bisa di-unpack
x, y, z = koordinat
print(x, y, z)  # Output: 10 20 30

# Membuat list
buah = ["apel", "pisang", "jeruk"]

# Menambah elemen
buah.append("mangga")
print(buah)  # Output: ['apel', 'pisang', 'jeruk', 'mangga']

# Mengubah elemen
buah[1] = "anggur"
print(buah)  # Output: ['apel', 'anggur', 'jeruk', 'mangga']

# Menghapus elemen
del buah[0]
print(buah)  # Output: ['anggur', 'jeruk', 'mangga']
