import json
import re
import os
import math

def kayit_ol():
    print("Kayıt Ol")
    while True:
        kullanici_adi = input("Kullanıcı Adı: ")
        sifre = input("Şifre: ")

        if not re.search(r"[A-Za-z]", sifre) or not re.search(r"\d", sifre) or not re.search(r"[A-Za-z0-9]", sifre):
            print("Şifre en az bir büyük harf, bir küçük harf ve bir sayı içermeli!")
            continue

        email = input("E-posta: ")
        if "@" not in email:
            print("Geçersiz e-posta adresi! '@' işareti içermelidir.")
            continue

        # Kullanıcı bilgilerini sözlük olarak saklayalım
        kullanici_bilgisi = {
            "kullanici_adi": kullanici_adi,
            "sifre": sifre,
            "email": email
        }

        # Kullanıcı bilgisini JSON formatında dosyaya kaydediyoruz
        with open("kullanici_veritabani.json", "a") as dosya:
            json.dump(kullanici_bilgisi, dosya)
            dosya.write("\n")  # Her kullanıcı bilgisi sonunda satır sonu ekleyelim

        print("Kayıt işlemi başarılı!")
        break

def hesap_sil(kullanici_adi):
    # Geçici bir dosya oluşturuyoruz
    gecici_dosya = "gecici_kullanici_veritabani.json"

    with open("kullanici_veritabani.json", "r") as kaynak_dosya, open(gecici_dosya, "w") as hedef_dosya:
        for satir in kaynak_dosya:
            kullanici_bilgisi = json.loads(satir)
            if kullanici_adi != kullanici_bilgisi["kullanici_adi"]:
                # Silinecek hesabı atlayıp diğer hesapları geçici dosyaya kopyalıyoruz
                json.dump(kullanici_bilgisi, hedef_dosya)
                hedef_dosya.write("\n")

    # Geçici dosyayı orijinal dosyanın yerine kopyalıyoruz
    os.remove("kullanici_veritabani.json")
    os.rename(gecici_dosya, "kullanici_veritabani.json")

    print(f"{kullanici_adi} kullanıcı adına sahip hesap başarıyla silindi!")

def giris_yap():
    print("Giriş Yap")
    while True:
        kullanici_adi = input("Kullanıcı Adı: ")
        sifre = input("Şifre: ")

        # Kullanıcı bilgilerini dosyadan okuyup kontrol ediyoruz
        with open("kullanici_veritabani.json", "r") as dosya:
            for satir in dosya:
                kullanici_bilgisi = json.loads(satir)
                if kullanici_adi == kullanici_bilgisi["kullanici_adi"] and sifre == kullanici_bilgisi["sifre"]:
                    print("Giriş Başarılı!")
                    return

        print("Kullanıcı adı veya şifre hatalı!")
        tekrar = input("Yeniden denemek istiyor musunuz? (Evet/Hayır): ")
        if tekrar.lower() != "evet":
            break

def ana_menu():
    while True:
        print("\nAna Menü")
        print("1. Kayıt Ol")
        print("2. Giriş Yap")
        print("3. Hesabı Sil")
        print("4. Çıkış")
        secim = input("Seçiminizi yapın (1/2/3/4): ")

        if secim == "1":
            kayit_ol()
        elif secim == "2":
            giris_yap()
        elif secim == "3":
            kullanici_adi = input("Silmek istediğiniz hesabın kullanıcı adını girin: ")
            hesap_sil(kullanici_adi)
        elif secim == "4":
            print("Uygulamadan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Tekrar deneyin.")

if __name__ == "__main__":
    ana_menu()