# Tóth Ádám // adamtoth4@gmail.com //

class Csapat:

    def __init__(self, args):
        self.orszag = args[0]
        self.reszvetelek_szama = int(args[1])
        self.legelso_indulas = int(args[2])
        self.legutolso_indulas = int(args[3])
        self.legjobb_eredmeny = args[4]
        self.elsoOtaEltelEv = 2021 - self.legelso_indulas

csapatok = []

for sor in open("fociVBk.csv", encoding="utf8").read().splitlines()[1:]:
    csapatok.append(Csapat(sor.split(";")))

# 1 Feladat

print(f"1. Feladat:\n\t A versenysorozat indulása óta {len(csapatok)} csapat képviseltette magát")

# 2 Feladat
legutolsó = []
db = 0

for csapat in csapatok:
    if csapat.legutolso_indulas == 2018:
        db += 1
        legutolsó.append(csapat)

print(f"2. Feladat:\n\tA legutolsó VB-n {db} csapat vett részt")
print(f"\tAz országok: ")
for csapat in legutolsó:
    print(f"\t{csapat.orszag}")

# 3 Feladat
db = 0

for csapat in csapatok:
    if csapat.orszag == "Belgium" or csapat.orszag == "Luxemburg" or csapat.orszag == "Hollandia":
        db += csapat.reszvetelek_szama

print(f"3.Feladat:\n\tA BeNeLux országok {db} alkalommal vettek részt a VB-n")

# 4 Feladat

elsoVB = csapatok[0]

for csapat in csapatok:
    if csapat.legelso_indulas < elsoVB.legelso_indulas:
        elsoVB = csapat

print(f"4 Feladat:\n\tA lgelső VB-t {elsoVB.legelso_indulas}-ben rendezték")

# 5 Feladat

nyertes_csapatok = 0

for csapat in csapatok:
    if "Világbajnok" in csapat.legjobb_eredmeny:
        nyertes_csapatok += 1

print(f"5. Feladat:\n\tA világbajnokságot eddig {nyertes_csapatok} db csapat nyerte meg")

# 6 Feladat

legjobb = []

for cs in csapatok:
    if "Szlovákia" in cs.orszag:
        legjobb.append(cs)

print(f"6. Feladat:\n\tSzlovákia legjobb helyezései: ")

for cs in legjobb:
    print(f"\t{cs.legjobb_eredmeny}")

# 7 Feladat
print(f"7. Feladat:")
i = 0
while i < len(csapatok):
    if csapatok[i].orszag == "Magyarország":
        if csapatok[i].legelso_indulas == elsoVB.legelso_indulas:
            print("\tMagyarország kint volt az első VB-n!")
        else:
            print("\tMagyarország nem jutott ki az első VB-re!")
        break
    i += 1
else:
    print("\tMagyarország sosem jutott ki VB-re!")

# 8 Feladat

file = open("legtobbszor.txt", "w", encoding="UTF-8")
for cs in csapatok:
    if(cs.reszvetelek_szama >= 10):
        file.write(f"{cs.orszag} {cs.elsoOtaEltelEv}-éve indult először\n") # Nyit egy txt-t és ha egy csapat részvételeinek száma >10 beleírja az Országot és az első olimpia óta eltelt időt
file.close()

print("\n8. Feladat: legtobbszor.txt kész!")

