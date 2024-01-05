# Import module dan Buat koneksi database untuk pertama kali
import sqlite3
conn = sqlite3.connect('database_fauna.db')
cursor = conn.cursor()

# Jalankan Query CREATE TABLE
cursor.execute
('''
                CREATE TABLE Fauna(
                id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_fauna VARCHAR(50),
                jenis VARCHAR(50),
                asal VARCHAR(50),
                jml_skrng INTEGER(10),
                thn_ditemukan INTEGER(10)
                )
            ''')
print("Tabel Database Berhasil Dibuat")

# Tutup koneksi
conn.close()