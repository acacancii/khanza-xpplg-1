

# ====== DATA PASIEN RAWAT INAP ======
# Setiap pasien: nama, hari rawat inap, tarif per hari
pasien_list = [
    {"nama": "Ahmad", "hari": 3, "tarif": 250000},
    {"nama": "Budi", "hari": 5, "tarif": 300000},
    {"nama": "Citra", "hari": 2, "tarif": 200000},
]

# ====== LOOP FOR: MENAMPILKAN DATA PASIEN ======

print("=== DATA PASIEN RAWAT INAP ===")
for pasien in pasien_list:
    total = pasien["hari"] * pasien["tarif"]
    print(f"Nama    : {pasien['nama']}")
    print(f"Durasi  : {pasien['hari']} hari")
    print(f"Tarif   : Rp {pasien['tarif']:,} /hari")
    print(f"Total   : Rp {total:,}")
    print("-" * 30)

# ====== LOOP WHILE: HITUNG JUMLAH PASIEN DENGAN BIAYA > 600 RIBU ======

index = 0
pasien_mahal = 0

while index < len(pasien_list):
    pasien = pasien_list[index]
    total = pasien["hari"] * pasien["tarif"]
    if total > 600000:
        pasien_mahal += 1
    index += 1

print(f"\nJumlah pasien dengan biaya > Rp600.000: {pasien_mahal}")
