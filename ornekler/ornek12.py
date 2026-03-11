import random
def start():
    for i in range(1,50):
        bosluk = " "*random.randint(1,i)
        yildiz = "*"*random.randint(1,i)
        print(bosluk+yildiz)
