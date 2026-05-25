import sqlite3

baglanti = sqlite3.connect("yurt.db")
imlec = baglanti.cursor()

imlec.execute("""
CREATE TABLE IF NOT EXISTS ogrenciler(
    ad TEXT,
    oda TEXT,
    aidat INTEGER
)
""")

imlec.execute("""
CREATE TABLE IF NOT EXISTS odalar(
    oda_no TEXT,
    durum TEXT
)
""")

baglanti.commit()