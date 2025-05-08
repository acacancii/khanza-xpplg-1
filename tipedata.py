"""
Simulasi Tipe Data pada Sistem KHANZA (SIMRS)
Topik      : Tipe Data Python
Deskripsi  : Menyimpan dan menampilkan data pasien menggunakan berbagai tipe data.
Tanggal    : 5 Mei 2025
"""

# ======== TIPE DATA DASAR ========

# String (str): Menyimpan nama pasien
nama_pasien = "Andi Pratama"

# Integer (int): Menyimpan umur pasien
umur_pasien = 29

# Float: Menyimpan suhu tubuh pasien
suhu_tubuh = 37.5

# Boolean (bool): Status kepesertaan BPJS
bpjs_aktif = True

# ======== TIPE DATA MAJEMUK ========

# List: Riwayat penyakit pasien
riwayat_penyakit = ["Diabetes", "Asma"]

# Tuple: Data vital pasien (tekanan darah, denyut jantung)
data_vital = (120, 80)  # (sistolik, diastolik)

# Dictionary: Data lengkap pasien
data_pasien = {
    "nama": nama_pasien,
    "umur": umur_pasien,
    "suhu": suhu_tubuh,
    "bpjs": bpjs_aktif,
    "riwayat": riwayat_penyakit,
    "vital": data_vital
}

# ======== OUTPUT PROGRAM ========

print("=== DATA PASIEN ===")
print(f"Nama           : {data_pasien['nama']}")
print(f"Umur           : {data_pasien['umur']} tahun")
print(f"Suhu Tubuh     : {data_pasien['suhu']} °C")
print(f"BPJS Aktif     : {'Ya' if data_pasien['bpjs'] else 'Tidak'}")
print("Riwayat Penyakit:")
for penyakit in data_pasien["riwayat"]:
    print(" -", penyakit)

print(f"Tekanan Darah  : {data_pasien['vital'][0]}/{data_pasien['vital'][1]} mmHg")
