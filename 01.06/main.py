# Tóth Ádám // adamtoth4@gmail.com //

print("1. Feladat: Kisebb nagyobb meghatározása")
a = int(input("Kérem az első számot: "))
b = int(input("Kérem a második számot: "))

if a == b:
    print(f"A két szám egyenlő.")
elif a > b:
    print(f"A nagyobb szám: {a} a kisebb szám {b}.")
else:
    print(f"A nagyobb szám: {b} a kisebb szám {a}.")

def szokoev(ev: int) -> bool:
    return ev % 400 == 0 or ev % 4 == 0 and ev % 100 != 0


print("2. Feladat: Szökőév listázó")
sz1 = int(input("Kérem az egyik évszámot: "))
sz2 = int(input("Kérem a másik évszámot: "))

k_ev = min(sz1,sz2)
b_ev = max(sz1,sz2)

szokoevek = []
for ev in range(k_ev, b_ev):
    if szokoev(ev):
        szokoevek.append(ev)

if len(szokoevek) > 0:
    print(f"Szökőévek: {szokoevek}")
else:
    print("Nincs szökőév a megadott tartományban")

class Epulet:
    def __init__(self, sor):
        self.nev = sor[0]
        self.varos = sor[1]
        self.orszag = sor[2]
        self.magassag = float(sor[3].replace(",", ".")) # Float mert valós szám
        self.emelet = int(sor[4])
        self.ev = int(sor[5])

epuletek = []
for sor in open("legmagasabb.txt", encoding="UTF-8").read().splitlines()[1:]: # Megnyitom, olvasom, sorokra vágom és a 2 sortól csinálom
    epuletek.append(Epulet(sor.split(";"))) # Az Epulet class alapján az epuletek listahoz adom splitelve a ; mentén az adatokat

# 3.2 Feladat

print(f"3.2 feladat: Épületek száma: {len(epuletek)}")

# 3.3 Feladat

sum = 0
for e in epuletek:
    sum += e.emelet

print(f"3.3 feladat: Emeletek összege: {sum}")

# 3.4 Feladat

maxi = 0

for i in range(1, len(epuletek)):
    if(epuletek[i].magassag > epuletek[maxi].magassag): maxi = i
print(f"\tNév: {epuletek[maxi].nev}")
print(f"\tVáros: {epuletek[maxi].varos}")
print(f"\tOrszág: {epuletek[maxi].orszag}")
print(f"\tMagasság: {epuletek[maxi].magassag}")
print(f"\tEmeletek száma: {epuletek[maxi].emelet}")
print(f"\tÉpítés éve: {epuletek[maxi].ev}")

# 3.5 Feladat
i = 0
print("3.5 Feladat: ", end="") # Az end csak azért van, hogy a print ne törjön sort és egymás után írja a dolgokat
while(i < len(epuletek) and epuletek[i].orszag != "Olasz*"):
    if(epuletek[i].orszag == "Olaszország"):
        print("Van ", end="") 
        break
    i += 1
else:
    print("Nincs ", end="")

print("olasz épület az adatok között!")
