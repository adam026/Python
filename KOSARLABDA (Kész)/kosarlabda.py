# Tóth Ádám // adamtoth4@gmail.com //

from datetime import datetime
class Csapat:

    def __init__(self,args):
        self.hazai = args[0]
        self.idegen = args[1]
        self.hazai_pont = int(args[2])
        self.idegen_pont = int(args[3])
        self.helyszin = args[4]
        self.idopont = datetime.strptime(args[5], "%Y-%m-%d")

csapatok = []

for sor in open("eredmenyek.csv", encoding="utf-8").read().splitlines()[1:]:
    csapatok.append(Csapat(sor.split(";")))


# 3 Feladat

hazai = 0
idegen = 0

for cs in csapatok:
    if cs.hazai == "Real Madrid":
        hazai += 1
    elif cs.idegen == "Real Madrid":
        idegen += 1

print(f"3. Feladat: Real Madrid: Hazai: {hazai}, Idegen: {idegen}")

# 4 Feladat
print(f"4. Feladat: ", end="")

dontetlen = 0

for cs in csapatok:
    if cs.hazai_pont == cs.idegen_pont:
        dontetlen += 1

if dontetlen > 0:
    print("Volt döntetlen")
else:
    print("Nem volt döntetlen")

# 5 Feladat

barcelonai = csapatok[0]
for cs in csapatok:
    if "Barcelona" in cs.hazai:
        barcelonai = cs

print(f"5. Barcelonai csapat neve: {barcelonai.hazai}")

# 6 Feladat
datum_csapatok = []
print("6. Feladat")
for cs in csapatok:
    if cs.idopont.year == 2004 and cs.idopont.month == 11 and cs.idopont.day == 21:
        print(f"\t{cs.hazai} - {cs.idegen} ({cs.hazai_pont}:{cs.idegen_pont})")

# 7 Feladat

print("7. Feladat")

helyszinek_szerint = {}
for cs in csapatok:
    if cs.helyszin not in helyszinek_szerint:
        helyszinek_szerint[cs.helyszin] = 1
    else:
        helyszinek_szerint[cs.helyszin] += 1
for x in helyszinek_szerint:
    if helyszinek_szerint[x] > 20:
        print(f"\t{x} - {helyszinek_szerint[x]}")



