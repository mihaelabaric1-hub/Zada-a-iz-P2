"""Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena, a završava kao prvo slovo prezimena.
String mora sadržavati bar jedan broj između 0 i 5 i razmak."""

import re
unos = input("Unesite string: ")
regex_izraz = r"^I.*[0-5].*\s.*P$|^I.*\s.*[0-5].*P$"
if re.match(regex_izraz, unos):
    print("String je ispravan.")
else:
    print("String NIJE ispravan.")
