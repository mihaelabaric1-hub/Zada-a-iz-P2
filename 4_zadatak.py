"""#Napisati regex za provjeru validnosti unosa e-maila. E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
#Nakon toga napisati regex za provjeru eduId koji mora biti formata ime.prezimeX@sum.ba 
#X predstavlja bilo koji broj (moze ici u beskonacnost), a taj broj ne mora postojati (može biti samo ime.prezime@sum.ba).
#Od korisnika zatražiti unos maila i eduid te ispisati uspješnost."""
import re

email = input("Unesite email: ")
eduid = input("Unesite eduid: ")
regex_email = r"^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$"
regex_eduid = r"^[a-zA-Z]+\.[a-zA-Z]+\d*@sum\.ba$"
if re.match(regex_email, email):
    print("E-mail je ispravan.")
else:
    print("E-mail nije ispravan.")
if re.match(regex_eduid, eduid):
    print("eduID je ispravan.")
else:
    print("eduID nije ispravan.")
