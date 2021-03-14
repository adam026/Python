# Tóth Ádám // adamtoth4@gmail.com //

from pathlib import Path

abc = {}

class Idezet:
    def __init__(self,args): # Az init függvénnyel definiálom a class részeit. Van egy szerző és egy idézet, melyet ; jel választ el. Ezt később definiáljuk.
        self.szerzo = args[0]
        self.idezet = args[1]

    def get_szerzo(self):
        eredmeny = ""
        szavak = self.szerzo.split("       ")
        for szo in szavak:
            betuk = szo.split("   ")
            for betu in betuk:
                if betu in abc:
                    eredmeny += abc[betu]
            eredmeny += " "
        return eredmeny[:-1]

    def get_idezet(self):
        eredmeny = ""
        szavak = self.idezet.split("       ")
        for szo in szavak:
            betuk = szo.split("   ")
            for betu in betuk:
                if betu in abc:
                    eredmeny += abc[betu]
            eredmeny += " "
        return eredmeny[:-1]



#abc = {}
abc_fajl = Path("morzeabc.txt").open()

elso_sor = True # Ezzel a fejlécsort vágom ki
for sor in abc_fajl:
    if not elso_sor:
        adatok = sor.split("\t") # Tabulátor mentén van tagolva
        abc[adatok[1].strip()] = adatok[0]
    else:
        elso_sor = False

 # 3. feladat
print(f"3. Feladat:\n\tA morze ABC-ben {len(abc)} karakter található")

# 4 feladat
print("4. Feladat: ")

karakter = input("\tKérek egy karaktert: ")

van_e = False
if karakter in abc.values():
    for x in abc: # a klucsokat járjuk be ezzel a dictionaryben
        if karakter == abc[x]:
            print(f"\tA megadott karakter morzekódja: {x}")
            break
else: 
    print("\tA megadott karakter nem található.")

# 5 feladat

fajl = Path("morze.txt").open()
idezetek = []
for sor in fajl:
    idezetek.append(Idezet(sor.split(";")))

# 7 Feladat

print(f"7. Feladat:\n\tAz első idézet szerzője: {idezet[0].get_szerzo}")

# 8 Feladat
maximum = 0
idezet = idezetek[0]
for x in idezetek:
    if len(x.get_idezet()) > maximum:
        maximum = len(x.get_idezet())
        idezet = x

print(f"8. Feladat:\n\tA leghosszabb idézet:\n{idezet.get_szerzo()}: {idezet.get_idezet()}")

# 9 feladat
print("9. Feladat: Arisztotelész idézetei: ")
for x in idezetek:
    if x.get_szerzo() == "ARISZTOTELÉSZ":
        print(f"\t- {x.get_idezet()}")

# 10 Feladat
uj_fajl = Path("forditas.txt").open(mode="w", encoding="utf8")
for x in idezetek:
    uj_fajl.write(f"{x.get_szerzo()}: {x.get_idezet()}\n")



