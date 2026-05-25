from database import baglanti, imlec
from dosyalama import log_yaz

def oda_ekle():
    oda_no = input("Oda numarası: ")

    imlec.execute("SELECT * FROM odalar WHERE oda_no = ?", (oda_no,))
    kontrol = imlec.fetchone()

    if kontrol:
        print("Bu oda zaten mevcut!")

    else:
        imlec.execute("INSERT INTO odalar VALUES(?, ?)", (oda_no, "boş"))
        baglanti.commit()

        log_yaz(f"{oda_no} numaralı oda eklendi.")

        print("Oda eklendi.")


def ogrenci_ekle():
    ad = input("Öğrenci adı: ").lower()
    oda = input("Oda numarası: ")

    imlec.execute("SELECT durum FROM odalar WHERE oda_no = ?", (oda,))
    sonuc = imlec.fetchone()

    if sonuc is None:
        print("Böyle bir oda yok!")
        return

    if sonuc[0] == "dolu":
        print("Oda dolu!")
        return

    try:
        aidat = int(input("Aidat borcu: "))

    except:
        print("Aidat sayı olmalı!")
        return

    imlec.execute("INSERT INTO ogrenciler VALUES(?, ?, ?)", (ad, oda, aidat))

    imlec.execute("UPDATE odalar SET durum = 'dolu' WHERE oda_no = ?", (oda,))

    baglanti.commit()

    log_yaz(f"{ad} isimli öğrenci eklendi.")

    print("Öğrenci eklendi.")


def ogrencileri_goster():
    imlec.execute("SELECT * FROM ogrenciler")

    veriler = imlec.fetchall()

    print("\n--- Öğrenciler ---")

    for ogrenci in veriler:
        print("Ad:", ogrenci[0], "| Oda:", ogrenci[1], "| Aidat:", ogrenci[2])


def odalari_goster():
    imlec.execute("SELECT * FROM odalar")

    veriler = imlec.fetchall()

    print("\n--- Odalar ---")

    for oda in veriler:
        print("Oda:", oda[0], "| Durum:", oda[1])