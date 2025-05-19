# Fungsi untuk menghitung hasil berdasarkan operator
def hitung(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Pembagian dengan nol!"
    else:
        return "Operator tidak dikenal!"

# Program utama
while True:
    print("\n=== KALKULATOR SEDERHANA ===")
    
    try:
        # Input angka
        a = float(input("Masukkan nilai a: "))
        b = float(input("Masukkan nilai b: "))
        
        # Input operator
        op = input("Masukkan operator (+, -, *, /): ")

        # Hitung dan tampilkan hasil
        hasil = hitung(a, b, op)
        print("Hasil:", hasil)
        
    except ValueError:
        print("Input tidak valid! Harus berupa angka.")

    # Tanya apakah mau lanjut
    lagi = input("\nHitung lagi? (y/n): ")
    if lagi.lower() != 'y':
        print("Program selesai. Terima kasih!")
        break
