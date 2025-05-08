def tampilkan_menu():
    print("\n=== KALKULATOR ARITMATIKA SEDERHANA ===")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pembagian Bulat (//)")
    print("6. Modulus (%)")
    print("7. Pangkat (**)")
    print("8. Keluar")

while True:
    tampilkan_menu()
    pilihan = input("Pilih operasi (1-8): ")

    if pilihan == '8':
        print("Terima kasih! Program selesai.")
        break

    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input harus berupa angka!")
        continue

    if pilihan == '1':
        print("Hasil:", angka1 + angka2)
    elif pilihan == '2':
        print("Hasil:", angka1 - angka2)
    elif pilihan == '3':
        print("Hasil:", angka1 * angka2)
    elif pilihan == '4':
        if angka2 != 0:
            print("Hasil:", angka1 / angka2)
        else:
            print("Error: Tidak bisa dibagi dengan nol!")
    elif pilihan == '5':
        if angka2 != 0:
            print("Hasil:", angka1 // angka2)
        else:
            print("Error: Tidak bisa dibagi dengan nol!")
    elif pilihan == '6':
        if angka2 != 0:
            print("Hasil:", angka1 % angka2)
        else:
            print("Error: Tidak bisa dibagi dengan nol!")
    elif pilihan == '7':
        print("Hasil:", angka1 ** angka2)
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1 sampai 8.")
