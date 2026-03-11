import random
def start():
    notlar=[random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
    ogrenci_num=0
    for nott in notlar:
        ogrenci_num +=1
        if nott>=50:
            print("Dersden geçti öğrenci numara : ",ogrenci_num," notu : ",nott)
        else:
            print("Dersten kaldı öğrenci numara : ",ogrenci_num," notu : ",nott)