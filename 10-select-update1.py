# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
import sqlite3

# Membuat koneksi ke database atau membuat database baru jika belum ada
koneksi = sqlite3.connect('database_fauna.db.')
cursor = koneksi.cursor()

# Data yang ingin diubah
id_fauna = 10
jml_skrng_baru = 650

# Menjalankan query UPDATE
cursor.execute(f"UPDATE FAUNA SET jml_skrng = {jml_skrng_baru} WHERE id_fauna = {id_fauna}")
koneksi.commit()

# Menampilkan pesan setelah update berhasil
if cursor.rowcount > 0:
    print(f"Data fauna dengan ID {id_fauna} berhasil diupdate.")
else:
    print(f"Tidak ada data fauna dengan ID {id_fauna}.")

# Menutup koneksi
koneksi.close()
