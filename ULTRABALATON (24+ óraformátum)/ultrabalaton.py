# Tóth Ádám // adamtoth4@gmail.com //

from datetime import datetime
class Versenyzo:

    def __init__(self, args):
        self.nev = args[0]
        self.rajtszam = args[1]
        self.kategoria = args[2]
        self.elert_eredmeny = args[3]
        self.befejezes = int(args[4])
        

        



versenyzok = []
for sor in open("ub2017egyeni.txt", encoding="UTF8").read().splitlines()[1:]:
    versenyzok.append(Versenyzo(sor.split(";")))

# 3 Feladat

print(f"3. Feladat: Egyéni indulók: {len(versenyzok)} fő")

# 4 Feladat
noi = 0
for v in versenyzok:
    if v.kategoria == "Noi" and v.befejezes == 100:
        noi += 1

print(f"4. Feladat: Célba érkező női sportolók: {noi} fő")

# 5 Feladat

nev = input("Kérem a sportoló nevét: ")

print("\tIndult egyéniben a sportoló? ", end="")
igen = 0
teljesitoversenyzo = versenyzok[0]
for v in versenyzok:
    if nev.lower() == v.nev.lower():
        igen += 1
        teljesitoversenyzo = v
        print("Igen")
        break
if igen == 0:
    print("Nem")

print(f"\tTeljesítette a teljes távot? ", end="")

if teljesitoversenyzo.befejezes == 100:
    if igen > 0:
        print("Igen")
    else:
        print("Nem")

print(versenyzok[1].idooraban)