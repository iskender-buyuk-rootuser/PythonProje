try:
    import os
    import time
    import colorama
    from ornekler import ornek1,ornek2,ornek3,ornek4,ornek5
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
                    
                    prompt2=input("Hangi rehberi istiyorsunuz:: ")

                    if prompt2 == "1":
                        os.system("cls")
                        ornek1.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        print("Kaynak Kodu not defterinde açılıyor")
                        os.system(f"notepad ornekler/ornek1.py")
                    elif prompt2 == "2":
                        os.system("cls")
                        ornek2.start()
                        input("bir tuşa basınız kaynak kodu açılcaktır")
                        print("Kaynak Kodu not defterinde açılıyor")
                        os.system(f"notepad ornekler/ornek1.py")
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
                    else:
                        print("Yanlış Komut")
                    pass
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