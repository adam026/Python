# Tóth Ádám // adamtoth4@gmail.com //

class Fogadas:

    def __init__(self,args):
        self.ev = args[0]
        self.het = args[1]
        self.fordulo = args[2]
        self.telitalalat = int(args[3])
        self.telitalalatnyeremeny = int(args[4])
        self.eredmenyek = args[5]

fogadasok = []

for sor in open("toto.txt", encoding="utf8").read().splitlines()[1:]:
    fogadasok.append(Fogadas(sor.split(";")))

# 3 Feladat

print(f"3. Feladat: Fordulók száma: {len(fogadasok)}")

# 4 Feladat

teli = 0

for f in fogadasok:
    if f.telitalalat > 0:
        teli += f.telitalalat

print(f"4. Feladat: Telitalálatos szelvények száma: {teli} db")

# 5 Feladat

ossznyeremeny = 0

for f in fogadasok:
    if f.telitalalat > 0 or f.telitalalatnyeremeny > 0:
        ossznyeremeny += (f.telitalalat * f.telitalalatnyeremeny)

print(f"5. Feladat: Átlag: {round(ossznyeremeny/len(fogadasok))} Ft")

# 6 Feladat


fogadasok2 = []
for f in fogadasok:
    if f.telitalalatnyeremeny != 0 and f.telitalalat != 0:
        fogadasok2.append(f)

mini = fogadasok2[0]
for f in fogadasok2:
    if f.telitalalatnyeremeny < mini.telitalalatnyeremeny:
        mini = f


maxi = fogadasok[0]

for f in fogadasok:
    if f.telitalalatnyeremeny > maxi.telitalalatnyeremeny:
        maxi = f

print(f"6. Feladat:")
print(f"\tLegnagyobb:\n\tÉv: {maxi.ev}\n\tHét: {maxi.het}\n\tForduló: {maxi.fordulo}\n\tTelitalálat: {maxi.telitalalat}\n\tNyeremény: {maxi.telitalalatnyeremeny}\n\tEredmények: {maxi.eredmenyek}\n")
print(f"\tLegkisebb:\n\tÉv: {mini.ev}\n\tHét: {mini.het}\n\tForduló: {mini.fordulo}\n\tTelitalálat: {mini.telitalalat}\n\tNyeremény: {mini.telitalalatnyeremeny}\n\tEredmények: {mini.eredmenyek}")

