# Impor Module dan Cek koneksi database
import sqlite3
koneksi = sqlite3.connect('database_fauna.db.')
cursor = koneksi.cursor()

# Menjalankan query SUM
cursor.execute("SELECT SUM(jml_skrng) FROM FAUNA")
total_populasi = cursor.fetchone()[0]

print(f"Jumlah total populasi hewan langka saat ini : {total_populasi}")

# Menutup koneksi
koneksi.close()