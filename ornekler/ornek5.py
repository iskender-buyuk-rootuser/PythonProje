def start():
    s=int(input("Sayı giriniz: "))
    f=1
    for i in range(1,s+1):
        f*=i
    print(f"{s} faktöriyeli = {f}")