def tambol(sayi):
    liste = []
    for i in range(1,sayi+1):
        if (sayi % i == 0):
            liste.append(i)
    return liste


while True:
    sayi=input("Sayı Giriniz: ")
    if (sayi == "q"):
        print("Programdan Çıkılıyor...")
        break
    else:
        sayi = int(sayi)
        print("Tam Bölenleri:",tambol(sayi))


