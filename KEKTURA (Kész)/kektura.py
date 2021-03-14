# Tóth Ádám // adamtoth4@gmail.com //

TFM = 192

class Allomas:

    def __init__(self,args):
        self.kiindulo = args[0]
        self.vegpont = args[1]
        self.hossz = float(args[2].replace(",","."))
        self.emelkedes = int(args[3])
        self.lejtes = int(args[4])
        self.pecsetelohely = args[5]
        self.legmagasabb = int(TFM + self.emelkedes - self.lejtes)

def HianyosNev(self):
    if self.pecsetelohely == "i" and "pecsetelohely" not in self.vegpont:
        return True
    else:
        return False

# 3 Feladat
allomasok = []

for sor in open("kektura.csv", encoding="utf8").read().splitlines()[1:]:
    allomasok.append(Allomas(sor.split(";")))

print(f"3. Feladat: Szakaszok száma: {len(allomasok)} db")

# 4 Feladat

ossz = 0

for allomas in allomasok:
    ossz += allomas.hossz

print(f"4. Feladat: A túra teljes hossza: {round(ossz, 3)} km")

# 5 Feladat

mini = allomasok[0]

for allomas in allomasok:
    if allomas.hossz < mini.hossz:
        mini = allomas

print(f"5. Feladat: A legrövidebb szakasz adatai:\n\tKezdete: {mini.kiindulo}\n\tVége: {mini.vegpont}\n\tTávolság: {mini.hossz} km")

# 7 Feladat

print(f"7. Feladat: Hiányos állomásnevek:")

for allomas in allomasok:
    if HianyosNev(allomas) == True:
        print(f"\t{allomas.vegpont}")

# 8 feladat

maxi = 192
maxika = {}

for allomas in allomasok:
    aktualis = maxi + allomas.emelkedes - allomas.lejtes
    maxi = aktualis
    if maxi not in maxika:
        maxika[maxi] = allomas.vegpont
    else:
        maxika[maxi] += 1

legtobb = max(maxika.items(), key = lambda k : k[0])
print(f"8. feladat: A túra legmagasabban fekvő pontja:\n\tA végpont neve: {legtobb[1]}\n\tA végpont tengerszint feletti magassága:{legtobb[0]} m")


