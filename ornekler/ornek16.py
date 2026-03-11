def start():
    liste =[]
    toplam =0
    for i in range(1,5):
        s = input(f"sayi {i} giriniz: ")
        liste.append(s)
    for sayi in liste:
        toplam+=int(sayi)
    print("oluşan liste: ",liste)
    print(toplam)