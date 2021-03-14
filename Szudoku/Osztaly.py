import math


class Feladvany:
    def __init__(self, sor):
        self.kezdo = sor
        self.meret = math.sqrt(len(sor))

    def kirajzol(self):
        i = 0
        while i < len(self.kezdo):
            if self.kezdo[i] == 0:
                print(".", end="")
            else:
                print(self.kezdo[i], end="")
            if i % self.meret == meret - 1:
                print()
            i += 1