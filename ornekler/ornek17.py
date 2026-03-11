def start():
    ogrenciler=[]
    print("[1] öğrenci kaydı")
    print("[2] yoklama başlat")
    menusecimi = input("seçiminiz: ")

    if menusecimi=="1":
        isim =input("öğrenci ismi: ")
        ogrenciler.append(isim)
    elif menusecimi=="2":
        for i in ogrenciler:
            vy = input(i + " burdamı?[0/1] : ")
            if vy == "1":
                print(i + " derste")
            elif vy == "0":
                print(i + " derste değil")
            else:
                print("yanlış tuş")

