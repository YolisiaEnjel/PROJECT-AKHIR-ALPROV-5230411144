# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('database_fauna.db.')
cursor = koneksi.cursor()

# Data yang ingin diubah

# Menjalankan query UPDATE
cursor.execute(f"UPDATE FAUNA SET asal = 'Kalimantan Timur' WHERE nama_fauna = 'Pesut Mahakam'")
koneksi.commit()

# Menampilkan pesan setelah update berhasil
if cursor.rowcount > 0:
    print(f"Data fauna berhasil diupdate")
else:
    print(f"Tidak ada data fauna")

# Menutup koneksi
koneksi.close()