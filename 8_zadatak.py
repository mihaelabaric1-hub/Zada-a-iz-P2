'''
Definirati dvije funkcije koje kao parametar primaju ime ali vraćaju različitu poruku dobrodošlice.
Jedna neka ispisuje “Pozdrav {ime}!”, a druga “Dobrodošao {ime}!”
Jedna od funkcija neka bude definirana lambda izrazom, a druga standardnim načinom.
Zatim definiraj treću funkciju koja kao parametar prima naziv funkcije za ispis dobrodošlice i poziva je tako što pošalje vaše ime u nju.
Pozvati treću funkciju prosljeđujući joj neku od prve dvije definirane funkcije.
'''

def pozdrav_standardni(ime):
    return "Pozdrav " + ime + "!"

pozdrav_lambda = lambda ime: "Dobrodošao/la " + ime + "!"

def pozovi_dobrodoslicu(funkcija_za_ispis):
    moje_ime = "Mihaela"
    rezultat = funkcija_za_ispis(moje_ime)
    print(rezultat)
pozovi_dobrodoslicu(pozdrav_standardni)
pozovi_dobrodoslicu(pozdrav_lambda)
