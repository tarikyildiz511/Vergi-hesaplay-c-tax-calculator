def vergileri_hesapla():
    maas = int(input("bir maas giriniz"))    
    if maas >=10000:
        print("vergileriniz yüzde 25 ")
    elif maas>3000:
        print("vergileriniz yüzde 15")
    else:
        print("vergilerden muafsiniz")    

def isim_giriniz():
    ad = input("Adınızı giriniz")
    soyad = input("Soyadınızı giriniz")
    with open("vergi_kayit.txt","w", encoding="utf-8") as file:
        file.write(ad+ " " + soyad)
def musteri_kayit():
    ad = input("adinizi giriniz")
    soyad = input("soyadinizi giriniz")
    print(f"hoşgeldiniz {ad},{soyad} Tarikbank olarak sizi görmekten mutluluk duyarız")
    with open("vergi_kayit.txt","a", encoding="utf-8") as file:
        file.write(ad+ " " + soyad)
while True:

    islem = input("1. vergileri hesapla 2. vergi giriniz 3.musterileri kayit et 4.cikis")
    if islem =="1":
        vergileri_hesapla()
    elif islem=="2":
        isim_giriniz()
    elif islem=="3":
        musteri_kayit()
    else:
        break








