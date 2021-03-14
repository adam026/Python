# Tóth Ádám // adamtoth4@gmail.com //

from datetime import datetime

class Diak:

    def __init__(self, args):
        self.om = args[0]
        self.vezeteknev = args[1]
        self.keresztnev = args[2]
        self.szulnap = datetime.strptime(args[3], "%Y.%m.%d")
        self.kor = int(args[4])
        self.nem = args[5]
        self.magassag = float(args[6].replace(",","."))
        self.suly = float(args[7].replace(",", "."))
        self.hajszin = args[8]
        self.BMI = round(self.suly / ((self.magassag / 100) ** 2))

diakok = []

for sor in open("forras.csv", encoding="utf8").read().splitlines()[1:]:
    diakok.append(Diak(sor.split(";")))

# 3 Feladat:

print(f"A forrásállomány összesen {len(diakok)} diák adatait tartalmazza")

# 4 Feladat:

nev = input("Kérek egy keresztnevet: ")

db = 0

for diak in diakok:
    if diak.keresztnev.lower() == nev.lower():
        db += 1

print(f"A megadott keresztnevet {db} diák viseli")

# 5 Feladat:

osszmagassag = 0

for diak in diakok:
    osszmagassag += diak.magassag

print(f"A diákok átlagmagassága {round(osszmagassag / len(diakok))}")

# 6 Feladat:

osszsuly = 0

for diak in diakok:
    osszsuly += diak.suly

print(f"A diákok összslya {round(osszsuly)}")

# 7 Feladat:

legalacsonyabb_lány = diakok[0]

for diak in diakok:
    if diak.magassag < legalacsonyabb_lány.magassag and diak.nem.lower() == "nő":
        legalacsonyabb_lány = diak

print(f"A lgalacsonyabb lány: {legalacsonyabb_lány.vezeteknev} {legalacsonyabb_lány.keresztnev}")

# 8 Feladat

legnehezebb_fiu = diakok[0]

for diak in diakok:
    if diak.suly > legnehezebb_fiu.suly and diak.nem.lower() == "férfi":
        legnehezebb_fiu = diak

print(f"A legnehezebb fiú: {legnehezebb_fiu.vezeteknev} {legnehezebb_fiu.keresztnev} OM azonosítója: {legnehezebb_fiu.om}")

# 9 Feladat:

rossz = 0

for diak in diakok:
    if 2021 - diak.szulnap.year != diak.kor:
        rossz += 1

print(f"A listában {rossz} db diáknak szerepel helytelenül a kora")

# 10 Feladat:

betu = input("Kérek egy betüt: ")

keresztnevekben = 0

for diak in diakok:
    for karakter in diak.keresztnev:
        if karakter.lower() == betu.lower():
            keresztnevekben += 1

vezeteknevekben = 0

for diak in diakok:
    for karakter in diak.vezeteknev:
        if karakter.lower() == betu.lower():
            vezeteknevekben += 1

print(f"Vezetéknevekben {vezeteknevekben} alkalommal, keresztnevekben {keresztnevekben} alkalommal szerepel a betű")

# 11 Feladat:

legfiatalabb = diakok[0]

for diak in diakok:
    if diak.kor < legfiatalabb.kor:
        legfiatalabb = diak

legidosebb = diakok[0]

for diak in diakok:
    if diak.kor > legidosebb.kor:
        legidosebb = diak

lkkt = 0
i = legidosebb.kor
while i <= legfiatalabb.kor * legidosebb.kor:
    if i % legfiatalabb.kor == 0 and i % legidosebb.kor == 0:
        lkkt = i
        break
    i += 1

print(f"lkkt: {lkkt}\n")

# 12 Feladat:

diakok_evenkent = {}

for diak in diakok:
    if diak.szulnap.year not in diakok_evenkent:
        diakok_evenkent[diak.szulnap.year] = 1
    else:
        diakok_evenkent[diak.szulnap.year] += 1
        
for x in diakok_evenkent:
    print(f"\t{x} - összesen {diakok_evenkent[x]} diák született")

# 13 Feladat:

diakok_hajszinenkent = {}

for diak in diakok:
    if diak.hajszin not in diakok_hajszinenkent:
        diakok_hajszinenkent[diak.hajszin] = 1
    else:
        diakok_hajszinenkent[diak.hajszin] += 1

for x in diakok_hajszinenkent:
    print(f"\t\t{x} - hajszínnel összesen {diakok_hajszinenkent[x]} diák rendelkezik")

# 14 Feladat:

diakok_vezeteknevenkent = {}

for diak in diakok:
    if diak.vezeteknev not in diakok_vezeteknevenkent:
        diakok_vezeteknevenkent[diak.vezeteknev] = 1
    else:
        diakok_vezeteknevenkent[diak.vezeteknev] += 1

for x in diakok_vezeteknevenkent:
    print(f"\t{x} - vezetéknevű diákből {diakok_vezeteknevenkent[x]} db van")

diakok_BMIkent = {}

for diak in diakok:
    if diak.BMI not in diakok_BMIkent:
        diakok_BMIkent[diak.BMI] = 1
    else:
        diakok_BMIkent[diak.BMI] += 1
    
for x in diakok_BMIkent:
    print(f"\t\t{diakok_BMIkent[x]} diáknak {x} a BMI-je")