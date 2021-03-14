# Tóth Ádám // adamtoth4@gmail.com //

class Orszag:

    def __init__(self,args):
        self.nev = args[0]
        self.fovaros = args[1]
        self.terulet = int(args[2])
        self.lakossag = float(args[3].replace(",","."))
        self.egtaj = args[4]

    def nepsuruseg(self):
        return (self.lakossag * 1000000) / self.terulet

orszagok = []

for sor in open("europa.txt", encoding="ISO 8859-1").read().splitlines()[1:]:
    orszagok.append(Orszag(sor.strip().split("\t"))) # Tabulátorok mentén

print(len(orszagok))

# 1 Feladat
print("1. Feladat: A betüvel kezdődő országok: ")
for orszag in orszagok:
    if orszag.nev[0] == "A":
        print(f"\t{orszag.nev}")

# 2 feladat

print("2. Feladat: Északi országok: ")
for orszag in orszagok:
    if orszag.egtaj == "Észak":
        print(f"\t{orszag.nev} - {orszag.fovaros}")

# 3 feladat

print("3. Feladat: Déli és Nyugati országok: ")

for orszag in orszagok:
    if orszag.egtaj == "Dél" or orszag.egtaj == "Nyugat":
        print(f"\tNeve: {orszag.nev} - Fővárosa: {orszag.fovaros} - Területe: {orszag.terulet} - Lakossága: {orszag.lakossag} millió fő - Égtája: {orszag.egtaj}")

# 4 feladat

print("4. Feladat: 90.000 nél kisebb területű országok: ")

for o in orszagok:
    if o.terulet < 90000:
        print(f"\t{o.nev}")

# 5 feladat

print(f"5. Feladat: Országok, melyek területe hasonló Magyarország területéhez: ")

for o in orszagok:
    if 50000 <= o.terulet <= 200000:
        print(f"\t{o.nev}")

# 6 feladat

print(f"6. Feladat: Legkisebb lakosságú ország: ")

legkisebb = orszagok[0]

for o in orszagok:
    if o.lakossag < legkisebb.lakossag:
        legkisebb = o

print(f"\t{legkisebb.nev}")

# 7 feladat
orszagok2 = []
for o in orszagok:
    orszagok2.append(o) # Ha nem hozunk létre egy plusz listát a remova-al csökkentjük az eredeti lista hosszát

legkisebbek = []


while len(legkisebbek) < 5: # Ezzel választjuk ki azt, hogy az 5 legkisebbet keressük
    legkisebb = orszagok2[0]
    for o in orszagok2:
        if o.lakossag < legkisebb.lakossag:
            legkisebb = o
    legkisebbek.append(legkisebb)
    orszagok2.remove(legkisebb)

print(f"7. Feladat: 5 legkisebb ország: ")

for o in legkisebbek:
    print(f"\t{o.nev}")

# 8 feladat

osszterulet = 0

for o in orszagok:
    osszterulet += o.terulet

print(f"8. Feladat: Európa összterülete: {osszterulet} km2")

# 9 feladat

osszlakossagok = {}

for o in orszagok:
    if o.egtaj not in osszlakossagok:
        osszlakossagok[o.egtaj] = o.lakossag
    else:
        osszlakossagok[o.egtaj] += o.lakossag

print(f" 9. Feladat: Égtájanként csoportosítva a lakosság: ")
for x in osszlakossagok:
    print(f"\t{x} - {osszlakossagok[x]} millió fő")

# 10 Feladat
"""
lakossagok = {}

for o in orszagok:
    if o.egtaj not in osszlakossagok:
        lakossagok[o.egtaj] = [o.lakossag, 1]
    else:
        lakossagok[o.egtaj][0] += o.lakossag
        lakossagok[o.egtaj][1] += 1
"""

egtajankent = {}

for o in orszagok:
    if o.egtaj not in egtajankent:
        egtajankent[o.egtaj] = 1
    else:
        egtajankent[o.egtaj] += 1

print("10. Feladat: Átlaglakosságok: ")

for x in egtajankent:
    print(f"\t {x} - Átlaglakossága {round(osszlakossagok[x] / egtajankent[x])} millió fő")

# 11 feladat

ossznepsuruseg = 0

for o in orszagok:
    ossznepsuruseg += o.nepsuruseg()

print(f"11. Feladat: Népsűrüségek átlaga: \n\tA népsűrüségek átlaga: {round(ossznepsuruseg / len(orszagok))}")

# 12 feladat

print(f"12. Feladat: Európa országainak száma: \n\t {len(orszagok)}")

# 13 feladat

print(f'13. Feladat: Keleti országok száma: \n\t{egtajankent["Kelet"]}')

# 14 feladat
b_fovarosok = 0

for o in orszagok:
    if o.fovaros[0] == "B":
        b_fovarosok += 1

print(f"14. feladat: B-vel kezdődő országok száma:\n\t{b_fovarosok}")

