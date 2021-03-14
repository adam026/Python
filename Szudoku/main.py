# Tóth Ádám
# adamtoth4@gmail.com

from pathlib import Path
import math
import random

feladvanyok = []


class Feladvany:
    def __init__(self, sor):
        self.kezdo = sor
        self.meret = math.sqrt(len(sor))


    def kirajzol(self):
        i = 0
        while i < len(self.kezdo):
            if self.kezdo[i] == "0":
                print(".", end="")
            else:
                print(self.kezdo[i], end="")
            if i % self.meret == self.meret - 1:
                print()
            i += 1





sudoku = Path("feladvanyok.txt").open()
for sor in sudoku:
    feladvanyok.append(Feladvany(sor.strip()))

print(f"3. Feladat: Beolvasva {len(feladvanyok)} feladvány")

hossz = []

sz = 0
ism = False
while sz not in range(4,10) and ism == False:
    sz = int(input("4. Feladat: Kérem a feladvány méretét (4-9): "))
    if 4 <= sz <= 9:
        ism = True

hossz = []
for f in feladvanyok:
    if f.meret == sz:
        hossz.append(f)
print(f"A kiválasztott {sz}X{sz} feladatból {len(hossz)} db van!")

# Nem nullák számát az egész hosszal

kiv = random.choice(hossz)
print(f"5. Feladat: A kiválaszott feladvány: \n{kiv.kezdo}")
x = 0
for num in kiv.kezdo:
    if num != "0":
        x += 1
print(f"6. Feladat: A feladvány kitöltöttsége: {int((x * 100) / (kiv.meret ** 2))} százalék")
print(f"7. Feladat: A feladvány kirajzolva: ")
kiv.kirajzol()

fajl = open(f"sudoku{sz}.txt","w")
listToStr = '\n'.join([str(sor.kezdo) for sor in hossz])
fajl.write(listToStr)
fajl.close()

print(f"8. Feladat: sudoku{sz}.txt állomány {len(hossz)} darab feladvánnyal létrehozva")







