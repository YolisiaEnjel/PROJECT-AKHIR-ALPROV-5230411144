# Impor Module dan Cek koneksi database
import sqlite3
koneksi = sqlite3.connect('database_fauna.db.')
kursor = koneksi.cursor()

# Menjalankan query SELECT dengan ORDER BY
kursor.execute("SELECT * FROM FAUNA ORDER BY jml_skrng DESC") #DESC
baris_table = kursor.fetchall()

# Membuat format table dengan method format()
print("Table fauna :")
print("=======================================================================================================================")
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID FAUNA", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN TERAKHIR DITEMUKAN"))
print("=======================================================================================================================")

# Tampilkan data sesuai format table dengan perulangan
for baris in baris_table:
    print("{:<10} {:<19} {:<20} {:<25} {:<22} {:<22}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))

# Tutup Koneksi
koneksi.close()