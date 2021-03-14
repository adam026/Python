# Tóth Ádám // adamtoth4@gmail.com //

class Sportag:

    def __init__(self, args):
        self.nev = args[0]
        self.napok = args[1:len(args)]
        for i in range(len(self.napok)):
            self.napok[i] = int(self.napok[i])

datumok = [28, 29, 30, 31, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
   
sportagak = []
for sor in open("London2012.txt", encoding="UTF-8").read().splitlines():
    sportagak.append(Sportag(sor.strip().split(";")))

# 2 Feladat

i = 0
while sportagak[i].nev != "Atlétika": i += 1
c = 0
for n in sportagak[i].napok:
  if n > 0: c += 1

print(f"2. feladat:\n\tDöntős napok száma atlétika sportágban: {c} db")

# 3 Feladat

i = 0

while sportagak[i].nev != "Úszás":
    i += 1

a = 0

for n in sportagak[i].napok:
    if n > 0:
        a += n

print(f"3. Feladat:\n\tAranyérmek száma úszásban: {a} db")

# 4 Feladat

npd = sportagak[0].napok

for s in sportagak[1:len(sportagak)]:
  i = 0
  for n in s.napok:
    npd[i] += n
    i += 1

maxi = 0
for i in range(len(npd)):
  if npd[i] > npd[maxi]: maxi = i

print(f"4. feladat:\n\tA legtöbb döntő ({npd[maxi]} db) {datumok[maxi]}.-án/én volt")

# 5 Feladat

ossz = 0

for s in sportagak:
    for n in s.napok:
        ossz += n
    

print(f"5. Feladat:\n\t{ossz} aranyérmet osztottak ki az olimpián")

# 6 Feladat

kn = 29
i = 0
while (datumok[i] != kn): i += 1
f = 0
for s in sportagak:
    f += s.napok[i]

print(f"6. feladat:\n\t{kn}-án/én {f} db döntő volt")
    