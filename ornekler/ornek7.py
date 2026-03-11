import os
def start():
    sifre = input("şifre oluşturunuz: ")
    os.system("cls")
    for i in range(3):
        Giris=input("şifrenizi giriniz: ")
        if Giris == sifre:
            print("hoşgeldiniz")
            break
        else:
            print("yanlış şifre kalan hak: ",2-i)