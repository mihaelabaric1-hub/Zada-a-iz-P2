'''
Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada.
'''

def okreni_string(tekst):
    if len(tekst) <= 1:
        return tekst
    else:
        return tekst[-1] + okreni_string(tekst[:-1])
rezultat = okreni_string("mostar")
print(rezultat)
