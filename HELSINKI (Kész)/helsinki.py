# Tóth Ádám // adamtoth4@gmail.com //

class Sportolo:

    def __init__(self, args):
        self.helyezes = int(args[0])
        self.szam = int(args[1])
        self.sportag = args[2]
        self.versenyszam = args[3]

sportolok = []
for sor in open("helsinki.txt", encoding="ISO 8859-1").read().splitlines():
    sportolok.append(Sportolo(sor.split(" ")))

# 3 Feladat

print(f"3. Feladat: Pontszerző helyezések száma: {len(sportolok)}")

# 4 Feladat

arany = 0
ezust = 0
bronz = 0

for s in sportolok:
    if s.helyezes == 1:
        arany += 1
    elif s.helyezes == 2:
        ezust += 1
    else:
        if s.helyezes == 3:
            bronz += 1

print(f"4 Feladat:")
print(f"Arany: {arany}\nEzüst: {ezust}\nBronz: {bronz}\nÖsszesen: {arany+ezust+bronz}")

# 5 Feladat

pontok = 0

for s in sportolok:
    if s.helyezes == 1:
        pontok += 7
    if s.helyezes == 2:
        pontok += 5
    if s.helyezes == 3:
        pontok += 4
    if s.helyezes == 4:
        pontok += 3
    if s.helyezes == 5:
        pontok += 2
    if s.helyezes == 6:
        pontok += 1

print(f"5. feladat:\nOlimpiai pontok száma: {pontok}")

# 6 Feladat

uszas = 0
torna = 0

for s in sportolok:
    if s.sportag == "uszas":
        uszas += 1
    elif s.sportag == "torna":
        torna += 1

if uszas == torna:
    print("Egyenlő volt az érmek száma")
elif uszas > torna:
    print("Úszás sportágban szereztek több érmet")
else:
    print("Torna sportágban szereztek több érmet")

# 7 Feladat

file = open("helsinki2.txt", "w", encoding="ISO 8859-1")

for s in sportolok:
    if s.sportag == "kajakkenu":
        file.write(f"{s.helyezes} {s.szam} kajak-kenu {s.versenyszam}\n")
    else:
        file.write(f"{s.helyezes} {s.szam} {s.sportag} {s.versenyszam}\n")
file.close()

# 8 Feldat

pontszerzokalapjan = {}

for s in sportolok:
    if s.helyezes not in pontszerzokalapjan:
        pontszerzokalapjan[s.helyezes] = 1
    else:
        pontszerzokalapjan[s.helyezes] += 1

for x in pontszerzokalapjan:
    print(f"{x} helyezést ért el: {pontszerzokalapjan[x]} versenyző")

legtobb_sportolo = sportolok[0]

for s in sportolok:
    if s.szam > legtobb_sportolo.szam:
        legtobb_sportolo = s

print(f"8 feladat: \nHelyezés: {legtobb_sportolo.helyezes}\nSportág: {legtobb_sportolo.sportag}\nVersenyszám: {legtobb_sportolo.versenyszam}\nSportolók száma: {legtobb_sportolo.szam}")



ermekszerint = {}

for sporto in sportolok:
    if sporto.helyezes not in ermekszerint:
        ermekszerint[sporto.helyezes] = sporto.
