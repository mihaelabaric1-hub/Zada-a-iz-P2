"""Napisati program koji generira kvadratnu matricu dimenzija 7x7.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na rubovima matrice.
"""
import random
matrica = []
for i in range(7):
    redak = []
    for j in range(7):
        redak.append(random.randint(1, 9))
    matrica.append(redak)
for redak in matrica:
    for broj in redak:
        print(broj, end=" ")
    print()
zbroj_rubova = 0
for i in range(7):
    for j in range(7):
        if i == 0 or i == 6 or j == 0 or j == 6:
            zbroj_rubova += matrica[i][j]
print("-" * 20)
print("Zbroj rubova:", zbroj_rubova)
