# SELECT ALL DATA FAUNA
import sqlite3
koneksi = sqlite3.connect('database_fauna.db.')
kursor = koneksi.cursor()

# Mengambil semua data dalam table dan tampilkan 
kursor.execute("SELECT * FROM FAUNA")

# Tampilkan dalam bentuk baris
baris_tabel = kursor.fetchall()

# Membuat format table dengan method format()
print("Tabel FAUNA :")
print("="*120)
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID FAUNA", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("="*120)

# Tampilkan data sesuai format table dengan perulangan
for baris in baris_tabel:
    print("{:<10} {:<19} {:<20} {:<25} {:<22} {:<22}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

# Tutup Koneksi
koneksi.close()