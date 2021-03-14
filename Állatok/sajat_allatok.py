# Tóth Ádám // adamtoth4@gmail.com //

from datetime import datetime
import random

class Allatok:

    def __init__(self, args):
        self.nev = args[0]
        self.faj = args[1]
        self.szulev = datetime.strptime(args[2].strip(), "%Y-%m-%d")

    def Primszám(num):
        for n in range(2,num):
            if num % n == 0:
                print("Nem primszám") 
                break
            else:
                print("Primszám!") 

allatok = []

for sor in open("forras.txt", encoding="utf8").read().splitlines()[1:]:
    allatok.append(Allatok(sor.split(";")))

# 3 Feladat

print(f"A forrásállomány {len(allatok)} db állatot tartalmaz")

# 4 Feladat:
betu = input("Kérek egy betüt: ")
count = 0
for allat in allatok:
    for karakter in allat.nev:
        if karakter.lower == betu.lower:
            count += 1

print(f"A bekért betü az összes állat nevében {count}-szor szerepel")

# 5 Feladat:

random_allat = random.choice(allatok)
print (f"A random kiválaszott állat \n\tNeve: {random_allat.nev}, \n\tFaja: {random_allat.faj}, \n\tSzületési ideje: {random_allat.szulev}")

# 6 Feladat:

kor = 2021 - random_allat.szulev.year
db = 0

for szam in range(1, kor + 1):
    if kor % szam == 0:
        db += 1
if db == 2:
    print(f"{random_allat.nev} kora primszám")
else:
    print(f"{random_allat.nev} kora nem primszam")

# 7 Feladat:

oteves = []

for allat in allatok:
    if 2021-allat.szulev.year == 5:
        oteves.append(allat.nev)

print (f"Ötéves állatok száma: {len(oteves)}")
print(f"Az ötéves állatok: {oteves}")

# 8 Feladat:

allatnev = 0

kivnev = input("Kérek egy nevet: ")
for allat in allatok:
    if allat.nev.lower() == kivnev.lower():
        allatnev += 1

print(f"A nevet {allatnev} állat viseli")

# 9 Feladat

lista_1 = []
bekert_szam = int(input("Kérek egy számot "))

for allat in allatok:
    if 2021-allat.szulev.year == bekert_szam:
        lista_1.append(allat)

print(f"{bekert_szam} éves állatok: ")

for allat in lista_1:
    print(f"Az állat neve: {allat.nev}, kora: {2021-allat.szulev.year}\t")

# 10 Feladat

legidosebbek = []
legidosebb = allatok[0]

for allat in allatok:
    if allat.szulev < legidosebb.szulev:
        legidosebb = allat


for allat in allatok:
    if allat.szulev.year == legidosebb.szulev.year:
        legidosebbek.append(allat)

for allat in legidosebbek:
    print(f"{allat.nev}, aki egy {allat.faj}. Születési éve: {allat.szulev}")
# Kell egy olyan funkció ami a többi állatot is beleteszi, mert van még egyidős vele

# 11 Feladat:

db = 0

for allat in allatok:
    if allat.faj.lower() == "kutya":
        db += 1

print(f"Az állatok közt {db} db kutya van")

# 12 Feladat:

leghosszabb_nevuek = []
maximum = 0

for allat in allatok:
    if len(allat.nev) > maximum:
        maximum = (len(allat.nev))

for allat in allatok:
    if len(allat.nev) == maximum:
        leghosszabb_nevuek.append(allat)

print(f"A leghosszabb nevűek: ")
for allat in leghosszabb_nevuek:
    print(allat.nev)

# 13 Feladat:

kétezretizenot = 0

for allat in allatok:
    if allat.szulev.year == 2015:
        kétezretizenot += 1

print(f"2015-ben született állatok száma: {kétezretizenot}")

# 14 Feladat:

korosszeg = 0

for allat in allatok:
    korosszeg += 2021-allat.szulev.year

print(f"Az állatok korátlaga: {korosszeg / len(allatok)}")

# 15 Feladat:

allatok_csop = {}

for allat in allatok:
    if allat.szulev.year not in allatok_csop:
        allatok_csop[allat.szulev.year] = 1
    else:
        allatok_csop[allat.szulev.year] += 1

for x in allatok_csop:
    print(f"\t{x} - {allatok_csop[x]} állat született")


        







