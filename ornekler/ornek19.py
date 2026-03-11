def start():
    sayilar = [1, 2, 3, 4]
    aranan_veri = int(input("Aranan sai verisini giriniz: "))
    i=0
    for sayi in sayilar:
        if sayi == aranan_veri:
            print("Veri bulundu index numarası: ",i)
            break
        
        i+=1
    
    else:
            print("Veri bulunamadı")