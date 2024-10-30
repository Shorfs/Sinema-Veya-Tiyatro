# Sinema veya tiyatro seçimi sunan ve öğrencilere indirim yapan Python kodu.

while True:
    try:
        secim = int(input("Sinema icin (1) Tiyatro icin (2)'yi tuslayiniz: "))
        
        if secim not in [1, 2]:
            print("Gecersiz secim. Lutfen 1 veya 2 giriniz.")
            continue  # Geçersiz seçimde döngünün başına dön

        ogrenci = input('Ogrenci misiniz (E) (H): ').strip().upper()  # Büyük harfe çevir ve boşlukları temizle
        ucret = 0

        # İndirimsiz fiyatı hesaplıyoruz
        if secim == 1:
            ucret = 220  # Sinema
        elif secim == 2:
            ucret = 200  # Tiyatro

        # Öğrenci indirimi
        if ogrenci == "E":
            ucret /= 2  # %50
        elif ogrenci != "H":
            print("Gecersiz giris. Lütfen E veya H giriniz.")
            continue  # Geçersiz girişte döngünün başına dön

        print("Odemeniz gereken ucret: {}".format(ucret))
        break  # Her şey doğruysa döngüden çık

    except ValueError:
        print("Sadece numara girisi yapilmalidir.")
