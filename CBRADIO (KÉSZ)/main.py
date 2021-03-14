# Tóth Ádám // adamtoth4@gmail.com //

import operator

class Radio:

    def __init__(self, args):
        self.ora = int(args[0])
        self.perc = int(args[1])
        self.adasdb = int(args[2])
        self.nev = args[3]
        self.AtszamolPercre = int((self.ora * 60) + self.perc)

radiok = []

for sor in open("cb.txt", encoding="utf8").read().splitlines()[1:]:
    radiok.append(Radio(sor.split(";")))

print(f"3. Feladat: Bejegyzések száma: {len(radiok)}")

# 4 Feladat

print("4. Feladat:", end=" ")
for radio in radiok:
    if radio.adasdb >= 4:
        print(f"Volt négy adást indító sofőr")
        break
    else:
        continue

# 5 Feladat

nev = input("5. Feladat: Kérek egy nevet: ")
db = 0
for radio in radiok:
    if nev == radio.nev:
        db += radio.adasdb
    
if db > 0:
    print(f"{nev} {db}X használta a CB rádiót")
else:
    print("Nincs ilyen nevű sofőr!")

# 6 Feladat

file = open("cb2.txt", "w", encoding="utf8")

for radio in radiok:
    elso_sor = True
    if elso_sor == True:
        file.write("Kezdes;Nev;Adasdb\n")
        elso_sor = False
    for radio in radiok:
        file.write(f"{radio.AtszamolPercre};{radio.nev};{radio.adasdb}\n")

# 8 Feladat

soforok_szama = []

for radio in radiok:
    if radio.nev not in soforok_szama:
        soforok_szama.append(radio.nev)

print(f"8. Feladat: Sofőrök száma: {len(soforok_szama)} fő")

# 9 Feladat

print(f"9. Feladat: A legtöbb adást indító sofőr")

szelektált = {}

for radio in radiok:
    if radio.nev not in szelektált:
        szelektált[radio.nev] = radio.adasdb
    else:
        szelektált[radio.nev] += radio.adasdb

legtobb = max(szelektált.items(), key = lambda k : k[1])
print(f"\tNév: {legtobb[0]}\n\tAdások száma: {legtobb[1]} alkalom")







    