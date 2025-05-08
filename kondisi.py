"""
Topik      : Struktur Kondisi (If-Else)
Konteks    : Sistem Informasi Rumah Sakit (KHANZA)
Deskripsi  : Menentukan tindakan berdasarkan kondisi suhu dan status vaksin pasien.
Tanggal    : 5 Mei 2025
"""

# ====== INPUT DATA PASIEN ======
nama = "Khanza haura azzahadi"
umur = 34
suhu_tubuh = 38.3
sudah_vaksin = False

# ====== PENGAMBILAN KEPUTUSAN ======

print("=== ANALISIS KONDISI PASIEN ===")
print(f"Nama Pasien   : {nama}")
print(f"Umur          : {umur} tahun")
print(f"Suhu Tubuh    : {suhu_tubuh} °C")
print(f"Sudah Vaksin  : {'Ya' if sudah_vaksin else 'Belum'}")

# Pemeriksaan suhu dan vaksinasi
if suhu_tubuh >= 38 and not sudah_vaksin:
    tindakan = "Pasien demam tinggi & belum vaksin → RUJUK ke RS rujukan COVID-19"
elif suhu_tubuh >= 38 and sudah_vaksin:
    tindakan = "Pasien demam tinggi → Observasi & beri antipiretik"
elif suhu_tubuh < 36:
    tindakan = "Pasien mengalami hipotermia → Hangatkan & observasi"
else:
    tindakan = "Kondisi stabil → Lanjutkan pemantauan rutin"

# ====== OUTPUT ======
print("\nTindakan Medis :", tindakan)
