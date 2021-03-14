# Tóth Ádám // adamtoth4@gmail.com //

class Jatekos:

    def __init__(self, args):
        self.mez = int(args[0])
        self.nev = args[1]
        self.nemzet = args[2]
        self.poszt = args[3]
        self.szulev = int(args[4])
        self.kor = 2021 - self.szulev

jatekosok = []

for sor in open("juve.txt", encoding="utf8").read().splitlines():
    jatekosok.append(Jatekos(sor.split(";")))

# 1 Feladat

print(f"1. Feladat: A csapatnak jelenleg {len(jatekosok)} db igazolt játékosa van!")

# 2 Feladat

db = 0

for jatekos in jatekosok:
    if jatekos.nemzet == "magyar":
        db += 1

if db > 0:
    print(f"2. Feladat: A csapatnak {db} db magyar játékosa van!")
else:
    print("2. Feladat: A csapatnak nincs magyar játékosa!")

# 3 Feladat

db = 0

for jatekos in jatekosok:
    if jatekos.nemzet == "olasz":
        db += 1

if db > 0:
    print(f"3. Feladat: A csapatnak {db} db olasz játékosa van!")
else:
    print("3. Feladat: A csapatnak nincs olasz játékosa!")

# 4 Feladat

mini = jatekosok[0]

for jatekos in jatekosok:
    if jatekos.kor < mini.kor:
        mini = jatekos

print(f"4. Feladat: A legfiatalabb játékos:\n\t{mini.nev}, aki {mini.kor} éves") 

# 5 Feladat

osszkor = 0

for jatekos in jatekosok:
    osszkor += jatekos.kor

print(f"5. Feladat: A csapat átlagéletkora: {round(osszkor / len(jatekosok))}")

# 6 Feladat

posztok_szerint = {}

for jatekos in jatekosok:
    if jatekos.poszt not in posztok_szerint:
        posztok_szerint[jatekos.poszt] = 1
    else:
        posztok_szerint[jatekos.poszt] += 1

print("6. Feladat:")

for x in posztok_szerint:
    print(f"\t{x} poszton {posztok_szerint[x]} db játékos játszik")

# 7 Feladat

maxi = jatekosok[0]

for jatekos in jatekosok:
    if jatekos.kor > maxi.kor and jatekos.poszt == "csatár":
        maxi = jatekos

print(f"7. Feladat: A legidősebb csatár: {maxi.nev} aki {maxi.kor} éves")

# 8 Feladat

evek_szerint = {}

for jatekos in jatekosok:
    if jatekos.szulev not in evek_szerint:
        evek_szerint[jatekos.szulev] = 1
    else:
        evek_szerint[jatekos.szulev] += 1

print(f"8. Feladat: Évek, amikor pontosan 3 játékos született:")
for x in evek_szerint:
    if evek_szerint[x] == 3:
        print(f"\t{x} - {evek_szerint[x]} db játékos")

# 9 Feladat

val = int(input("Kérek egy számot: "))

for jatekos in jatekosok:
    try:
        if val == jatekos.mez:
            print(f"9. Feladat: Az általad megadott {val} számú mezt {jatekos.nev} viseli")
    except:
        print(f"9. Feladat: Az általad megadott mezszámot egyik játékos sem viseli")
   
# 10 Feladat

file = open("hatvedek.txt", "w", encoding="utf8")

for jatekos in jatekosok:
    if jatekos.poszt == "hátvéd":
        file.write(f"{jatekos.nev} - {jatekos.kor}\n")
file.close
                
            