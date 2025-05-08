"""
Topik      : Operator dalam Python
Konteks    : Sistem Informasi Rumah Sakit (KHANZA)
Deskripsi  : Menggunakan berbagai operator untuk pengolahan data pasien dan layanan.
Tanggal    : 5 Mei 2025
"""

# ======== OPERATOR ARITMATIKA ========

# Data biaya rawat inap
lama_inap = 5  # dalam hari
tarif_per_hari = 300000  # dalam rupiah

# Hitung total biaya
total_biaya = lama_inap * tarif_per_hari  # operator perkalian
diskon = 50000
biaya_setelah_diskon = total_biaya - diskon  # operator pengurangan

print("=== OPERATOR ARITMATIKA ===")
print("Total Biaya Rawat Inap     : Rp", total_biaya)
print("Diskon                     : Rp", diskon)
print("Biaya Setelah Diskon       : Rp", biaya_setelah_diskon)

# ======== OPERATOR PERBANDINGAN ========

# Cek apakah pasien termasuk lansia (umur >= 60)
umur_pasien = 65
is_lansia = umur_pasien >= 60  # operator relasional

print("\n=== OPERATOR PERBANDINGAN ===")
print("Umur Pasien :", umur_pasien)
print("Apakah Lansia? :", is_lansia)

# ======== OPERATOR LOGIKA ========

# Cek apakah pasien butuh rujukan (demam tinggi DAN belum vaksin)
suhu_tubuh = 38.5
belum_vaksin = True

butuh_rujukan = suhu_tubuh > 37.5 and belum_vaksin  # operator logika AND

print("\n=== OPERATOR LOGIKA ===")
print("Suhu Tubuh Pasien :", suhu_tubuh)
print("Belum Vaksin      :", belum_vaksin)
print("Perlu Rujukan?    :", butuh_rujukan)

# ======== OPERATOR PENUGASAN ========

# Tambahkan biaya pemeriksaan laboratorium
biaya_lab = 150000
biaya_setelah_diskon += biaya_lab  # operator penugasan +=

print("\n=== OPERATOR PENUGASAN ===")
print("Biaya + Pemeriksaan Lab    : Rp", biaya_setelah_diskon)
