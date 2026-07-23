""" Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
 Prebrojati u rječnik koliko ima kojih ocjena.
 Izračunati postotak prolaznosti. (sve ocjene veće od 1)"""
import random

imena = ["Miro", "Stjepan", "Josip", "Toni", "Robert", "Marko", "Ljubo", "Josipa", "Magdalena", "Ivana",
         "Stipe", "Emanuel", "Petar", "Ivan", "Luka", "Filip", "Lara", "Laura", "Mario", "Ana",
         "Marija", "Nikolina", "Andrija", "Slaven", "Sebastian", "Marko", "Frano", "Stipan", "Eugen",
         "Toni", "Dražan", "Matej", "Nives", "Nemanja", "Sara", "Ružica", "Gabrijel", "Darian", "Ivana",
         "Ivan Stjepan", "Kristian", "Josip", "Tomislav", "Jovan", "Gabrijel", "Mia", "Ante", "Josip",
         "Ante", "Josip", "Danijel", "Goran", "Zoran Ivan", "Franjo Francisko", "Sergej", "Matej",
         "Marin", "Sara", "Josip", "Stjepan", "Iva", "Marko", "Sara", "Krešimir", "Magdalena", "Marko",
         "Mirko", "David", "Ema", "Paul", "Sven", "Natalija", "Petar", "Emanuel", "Helena", "Antonio", "Petar"]

brojac_ocjena = {}
prošli = 0
ukupno_studenata = 0

for ime in imena:
    ocjena = random.randint(1, 5)
    ukupno_studenata += 1
    
    if ocjena in brojac_ocjena:
        brojac_ocjena[ocjena] += 1
    else:
        brojac_ocjena[ocjena] = 1
        
    if ocjena > 1:
        prošli += 1

postotak_prolaznosti = (prošli / ukupno_studenata) * 100
print("Broj ocjena po kategorijama:")
for ocjena, broj in brojac_ocjena.items():
    print("Ocjena", ocjena, ":", broj)
print("postotak prolaznosti:", postotak_prolaznosti, "posto")
