# Tóth Ádám // adamtoth4@gmail.com //

class Ember:

    def __init__(self,args):
        self.nev = args[0]
        self.kategoria = args[1]
        self.egyesulet = args[2]
        self.f1 = int(args[3])
        self.f2 = int(args[4])
        self.f3 = int(args[5])
        self.f4 = int(args[6])
        self.f5 = int(args[7])
        self.f6 = int(args[8])
        self.f7 = int(args[9])
        self.f8 = int(args[10])
        self.osszpont = self.f1 + self.f2 + self.f3 + self.f4 + self.f5 + self.f6 + self.f7 + self.f8

emberek = []

for sor in open("fob2016.txt", encoding="utf8").read().splitlines():
    emberek.append(Ember(sor.split(";")))

# 3 Feladat

print(f"3. Feladat: Versenyzők száma: {len(emberek)}")

# 4 Feladat

nok = 0

for ember in emberek:
    if ember.kategoria == "Noi":
        nok += 1

print(f"4. Feladat: A női versenyzők aránya {round((nok * 100)/len(emberek), 2)}%")

# 6 Feladat

maxi = emberek[0]

for ember in emberek:
    if ember.osszpont > maxi.osszpont and ember.kategoria == "Noi":
        maxi = ember

print(f"6. feladat: A bajnok női versenyző\n\tNév: {maxi.nev}\n\tEgyesület:{maxi.egyesulet}\n\t{maxi.osszpont}")

# 7 Feladat
file = open("osszpontFF.txt", "w", encoding="UTF-8")
for ember in emberek:
    if ember.kategoria == "Felnott ferfi":
        file.write(f"{ember.nev};{ember.osszpont}\n")
file.close()

# 8 Feladat

statisztika = {}

for ember in emberek:
    if ember.egyesulet not in statisztika:
        statisztika[ember.egyesulet] = 1
    else:
        statisztika[ember.egyesulet] += 1

for x in statisztika:
    if x != "n.a." and statisztika[x] > 2:
        print(f"{x} - {statisztika[x]} fő")