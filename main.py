try:
    import os
    import time
    import colorama
    from ornekler import ornek1,ornek2,ornek3,ornek4,ornek5,ornek6,ornek7,ornek8,ornek9,ornek10,ornek11,ornek12,ornek13,ornek14,ornek15,ornek16,ornek17,ornek18,ornek19,ornek20

    colorama.init()
    def main():
        while True:
            print(colorama.Fore.CYAN+"Hoşgeldiniz Lütfen seçim yapınız.")

            print(colorama.Fore.RESET+"1-For döngüsü nedir")
            print("2- For dögusu kullanımı")
            print("3-Çıkmak")
            prompt = input("Seçim yapınız :: ")
            if prompt == "1":
                os.system("cls")
                print(colorama.Fore.GREEN+"For döngüsü, kod dünyasının her işe koşan İsviçre çakısı gibidir. Hem sayısal hem metinsel ifadeleri, hem de liste içindeki elemanları tek tek ayıklamak için kullanılır.\n\nÖrneğin bir galericisiniz ve onlarca arabanız var, ancak hepsini akılda tutmak imkansız. İşte burada For devreye girer: Arabalar listenizi baştan sona tek tek sayar ve her saydığı arabayı o anlık bir değişkenin içine atar. Siz bu döngüye 10 saniyelik bir gecikme koyarsanız, her 10 saniyede bir o anki araba değişir ve siz de bu değişkeni web sitenizin vitrinine 'Elimizdeki Arabalar' diye yansıtabilirsiniz. Yani gerçek hayattaki kullanımı tam olarak budur; kalabalık bir grubu sıraya dizip her biriyle sırayla ilgilenmenizi sağlar.")
                input(colorama.Fore.WHITE+"-------------------Bir tuşa basınız")
                os.system("cls")
            elif prompt == "2":
                while True:
                    os.system("cls")
                    print("For döngüsü için kullanımlar aşağıdaki rehberlerde mevcuttur.")
                    print("[1] 1-19'a kadar sayma ornekler/ornek1.py")
                    print("[2] 20-1'e kadar geri sayma ornekler/ornek2.py")
                    print("[3] liste sayma ornekler/ornek3.py")
                    print("[4] kelime harf sayma ornekler/ornek4.py")
                    print("[5] Faktöriyel hesaplama ornekler/ornek5.py")
                    print("[6] Çift sayıları listeleme ornekler/ornek6.py")
                    print("[7] 3 şanslı giriş paneli ornekler/ornek7.py")
                    print("[8] ismini tekrarlatma ornekler/ornek8.py")
                    print("[9] Bilgisayar simulasyonu ornekler/ornek9.py")
                    print("[10] Yıldızlarla üçgen yapımı ornekler/ornek10.py")
                    print("[11] Ters yıldızlarla üçgen yapımı ornekler/ornek11.py")
                    print("[12] Rastgele yıldız ornekler/ornek12.py")
                    print("[13] verilen sayının toplamı ornekler/ornek13.py")
                    print("[14] Girilen sayıya kadar küp hesaplama ornekler/ornek14.py")
                    print("[15] cümlede harf sayısı bulma ornekler/ornek15.py")
                    print("[16] Liste elemanlarını toplama ornekler/ornek16.py")
                    print("[17] yoklama programı ornekler/ornek17.py")
                    print("[18] rastgele not hesaplama ornekler/ornek18.py")
                    print("[19] Listede veri varmı kontrolu ornekler/ornek19.py")
                    print("[20] verilen sayıya kadar gelen sayiları listeye ekleme ornekler/ornek20.py")
                    
                    prompt2=input("Hangi rehberi istiyorsunuz (Çıkmak için 'q'):: ")

                    if prompt2 == "1":
                        os.system("cls")
                        ornek1.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek1.py")
                    elif prompt2 == "2":
                        os.system("cls")
                        ornek2.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek2.py")
                    elif prompt2 == "3":
                        os.system("cls")
                        ornek3.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek3.py")
                    elif prompt2 == "4":
                        os.system("cls")
                        ornek4.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek4.py")
                    elif prompt2 == "5":
                        os.system("cls")
                        ornek5.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek5.py")
                    elif prompt2 == "6":
                        os.system("cls")
                        ornek6.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek6.py")
                    elif prompt2 == "7":
                        os.system("cls")
                        ornek7.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek7.py")
                    elif prompt2 == "8":
                        os.system("cls")
                        ornek8.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek8.py")
                    elif prompt2 == "9":
                        os.system("cls")
                        ornek9.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek9.py")
                    elif prompt2 == "10":
                        os.system("cls")
                        ornek10.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek10.py")
                    elif prompt2 == "11":
                        os.system("cls")
                        ornek11.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek11.py")
                    elif prompt2 == "12":
                        os.system("cls")
                        ornek12.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek12.py")
                    elif prompt2 == "13":
                        os.system("cls")
                        ornek13.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek13.py")
                    elif prompt2 == "14":
                        os.system("cls")
                        ornek14.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek14.py")
                    elif prompt2 == "15":
                        os.system("cls")
                        ornek15.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek15.py")
                    elif prompt2 == "16":
                        os.system("cls")
                        ornek16.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek16.py")
                    elif prompt2 == "17":
                        os.system("cls")
                        ornek17.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek17.py")
                    elif prompt2 == "18":
                        os.system("cls")
                        ornek18.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek18.py")
                    elif prompt2 == "19":
                        os.system("cls")
                        ornek19.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek19.py")
                    elif prompt2 == "20":
                        os.system("cls")
                        ornek20.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        os.system(f"notepad ornekler/ornek20.py")
                    elif prompt2.lower() == "q":
                        break
                    else:
                        print("Yanlış Komut")
                        time.sleep(1)
            elif prompt == "3":
                print("Görüşmek Üzere..")
                time.sleep(2)
                break
            else:
                print("Yanlış Komut")

    main()
except ImportError as error:
    print(error.name," Bulunamadı! Otomatik indirme süreci başlıyor...")
    import os
    os.system(f"pip install {error.name}")
    os.system(f"py -m pip install {error.name}")
    print("Kurulum tamamlandı. Eğer sorun oluştuysa lütfen manuel olarak indiriniz.")
    input("---Enter'a Basın---")