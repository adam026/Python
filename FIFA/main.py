class Csapat:
    def __init__(self, sor):
        self.orszag = sor[0]
        self.reszvetelekSzama = int(sor[1])
        self.elsoIndulas = int(sor[2])
        self.legutobbiIndulas = int(sor[3])
        self.legjobbEredmeny = sor[4]
        self.elsoOtaEltelEv = 2021 - self.elsoIndulas

csapatok = []
# 0 feladat

for sor in open("fociVBk.csv", encoding="UTF-8").read().splitlines()[1:]: # Megnyitom, olvasom, a line-okat splitelem, és az elsőt, a fejlécet kihagyom
    csapatok.append(Csapat(sor.split(";"))) #hozzáadom a Csapatok konstruktorával a listához. ; mentén splitel és szépen index szerint különszedi őket

# 1 Feladat
print(f"1. Feladat: csapatok száma: {len(csapatok)}") # A csapatok száma. Mennyi elem van a listában.

# 2 Feladat
print("\n2. Feladat: 2018-as VB csapatai:")
i = 1 # 1-től indulva végigmegy a csapat listában lévő csapatokon, és ha talál olyat ami 2018-ban indult kiírja
for cs in csapatok:
    if cs.legutobbiIndulas == 2018:
        print("%15s" % cs.orszag, end = " ")
        if i % 4 == 0: print()
        i += 1

# 3 Feladat:
sum = 0 # Kiszámolja hányszor vett részt Belgium, Hollandia és Luxemburg
for cs in csapatok:
    if cs.orszag in ["Belgium", "Hollandia", "Luxemburg"]: sum += cs.reszvetelekSzama
print(f"\n3. Feladat: A BeNeLux országok összesen {sum} alkalommal vettek részt a VB-n")

# 4 Feladat:
min = 0
i = 0 # 1-től a csapatok számáig végigmegy és megnézi melyiknek az első indulása a legkisebb
for i in range(1, len(csapatok)):
    if csapatok[i].elsoIndulas < csapatok[min].elsoIndulas: min = i

elso = csapatok[min].elsoIndulas
print(f"\n4. Feladat: Az első VBt {csapatok[min].elsoIndulas}-ban rendezték")

# 5. Feladat: 

c = 0 # Megnézi hogy a csapatok listában hány "Világbajnok" van összesen
for cs in csapatok:
    if ("Világbajnok" in cs.legjobbEredmeny): c +=1

print(f"\n5. Feladat: Eddig {c} ország csapata volt világbajnok")

# 6. Feladat:
print("\n6. Feladat: ", end = "")
i = 0
while i < len(csapatok): # 0 tól kezdve végigmegy a csapatok listán és megnézi, hogy van e Szlovákia. Ha van kiírja a legjobb eredményét és breakel. 
    if csapatok[i].orszag == "Szlovákia":
        print(f"Szlovákia legjobb eredménye: {csapatok[i].legjobbEredmeny}")
        break
    i += 1
else: print(f"Szlovákia még sosem került ki a VBre")

# 7. Feladat:
print("\n7. Feladat: ", end = "")
i = 0 # Ha a csapatok iedik elemének országa megegyezik Magyarországgal, és az első indulásának éve = az első olimpiával kiírja hogy kinn volt.
while i < len(csapatok):
    if csapatok[i].orszag == "Magyarország":
        if csapatok[i].elsoIndulas == elso:
            print("Magyarország kint volt az első VB-n!")
        else:
            print("Magyarország nem jutott ki az első VB-re!")
        break
    i += 1
else:
    print("Magyarország sosem jutott ki VB-re!")

# 8. Feladat:
file = open("legtobbszor.txt", "w", encoding="UTF-8")
for cs in csapatok:
    if(cs.reszvetelekSzama >= 10):
        file.write(f"{cs.orszag} {cs.elsoOtaEltelEv}\n") # Nyit egy txt-t és ha egy csapat részvételeinek száma >10 beleírja az Országot és az első olimpia óta eltelt időt
file.close()

print("\n8. Feladat: legtobbszor.txt kész!")