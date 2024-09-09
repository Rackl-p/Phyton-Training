liste =[]

def listenfueller(anzahl):
    for i in range(anzahl):
        liste.append([1,3,4,5])

def loop(name):
    for i in name:
        print(i)
        for j in i:
            print(j)

listenfueller(10)
loop(liste)
#print(liste)