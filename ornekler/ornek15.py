def start():
    print("cumle giriniz o cumledekli harf sayısı yazılacaktır")
    cumle = input("cumle giriniz: ")
    harf = 0
    for i in cumle:
        harf+=1
    print(f"bu cumlede şu kadar harf var : {harf}")