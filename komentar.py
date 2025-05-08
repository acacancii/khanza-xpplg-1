"""
Nama Aplikasi : Pengecekan Suhu Tubuh
Versi         : 1.0
Tujuan        : Menentukan apakah suhu tubuh seseorang normal, demam, atau hipotermia.
Dibuat oleh   : Tim Sistem Informasi RS (SimRS)
Tanggal       : 5 Mei 2025
"""

# Fungsi untuk mengevaluasi suhu tubuh
def cek_suhu(suhu):
    """
    Fungsi ini mengevaluasi suhu tubuh pasien
    Input  : suhu (float)
    Output : status suhu (string)
    """
    if suhu >= 38:
        return "Demam"
    elif suhu < 36:
        return "Hipotermia"
    else:
        return "Normal"

# Input dari pengguna
try:
    suhu_pasien = float(input("Masukkan suhu tubuh pasien (°C): "))  # Input suhu dalam derajat Celcius
    status = cek_suhu(suhu_pasien)  # Panggil fungsi untuk menentukan status suhu
    print("Status suhu tubuh:", status)  # Tampilkan hasil
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
