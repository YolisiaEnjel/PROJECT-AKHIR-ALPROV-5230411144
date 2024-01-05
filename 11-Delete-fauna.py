# Impor module dan Cek koneksi database
import sqlite3
koneksi = sqlite3.connect('database_fauna.db.')
cursor = koneksi.cursor()

# Jalankan Query DELETE dan simpan perubahan
cursor.execute("DELETE FROM Fauna WHERE asal = 'Kalimantan'")
koneksi.commit()

# Jalankan Query SELECT
cursor.execute("SELECT * FROM Fauna")
dataFauna = cursor.fetchall()

# Tampilkan data dalam format tabel setelah di hapus
if len(dataFauna) > 0:
    print("="*100)
    print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format("ID", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAT INI", "TAHUN DITEMUKAN"))
    print("="*100)
    for value in dataFauna:
        print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(value[0], value[1], value[2], value[3], value[4],value[5]))
    else:
        print("="*100)
        print("Data Fauna Yang berasal dari Kalimantan Berhasil Di hapus")

# Tutup Koneksi
koneksi.close()