# Tóth Ádám // adamtoth4@gmail.com //

class Utas:

    def __init__(self,args):
        self.kategoria = args[0]
        self.tulelo = int(args[1])
        self.eltunt = int(args[2])

utasok = []

for sor in open("titanic.txt", encoding="UTF-8"):
    utasok.append(Utas(sor.split(";")))

# 2 Feladat

print(f"2. Feladat: {len(utasok)}")

# 3 Feladat

osszes = 0

for u in utasok:
    osszes += u.tulelo
    osszes += u.eltunt

print(f"3. Feladat: {osszes} fő") 

# 4 Feladat

ksz = input("Kulcsszó: ")

talalat = []

for u in utasok:
    if ksz.lower() in u.kategoria.lower():
        talalat.append(u)

if len(talalat) == 0:
    print("Nincs találat!")
else:
    print(f"Van találat!")

# 5 Feladat
print("5. Feladat: ")
for t in talalat:
    print(f"\t{t.kategoria} {t.tulelo + t.eltunt}")

# 6 Feladat

tobbmint60 = []


print("6. Feladat: ")
for u in utasok:
    if (u.eltunt * 100) / u.tulelo > 60:
        print(f"\t{u.kategoria}")

# 7 Feladat

legtobbtulelo = utasok[0]

for u in utasok:
    if u.tulelo > legtobbtulelo.tulelo:
        legtobbtulelo = u

print(f"7. Feladat: {legtobbtulelo.kategoria}")
    


