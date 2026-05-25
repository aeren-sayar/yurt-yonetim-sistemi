def log_yaz(mesaj):

    dosya = open("log.txt", "a", encoding="utf-8")

    dosya.write(mesaj + "\n")

    dosya.close()