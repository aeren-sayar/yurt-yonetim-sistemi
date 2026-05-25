from fonksiyonlar import *

kullanicilar = {"admin": "1234", "ogrenci": "1111"}

menu = [
    "1- Oda ekle",
    "2- Öğrenci ekle",
    "3- Öğrencileri göster",
    "4- Odaları göster",
    "5- Çıkış"
]

print("Yurt Yönetim Sistemine Hoşgeldiniz")

kullanici = input("Kullanıcı adı: ")
sifre = input("Şifre: ")

if kullanici in kullanicilar and kullanicilar[kullanici] == sifre:

    print("\nGiriş başarılı!")

    while True:

        print("\n--- MENÜ ---")

        for i in menu:
            print(i)

        secim = input("Seçiminiz: ")

        if secim == "1":
            oda_ekle()

        elif secim == "2":
            ogrenci_ekle()

        elif secim == "3":
            ogrencileri_goster()

        elif secim == "4":
            odalari_goster()

        elif secim == "5":
            print("Program kapatılıyor...")
            break

        else:
            print("Hatalı seçim!")

else:
    print("Kullanıcı adı veya şifre yanlış!")