'''
Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.
'''

def generator_parni(broj):
    for i in range(broj):
        if i % 2 == 0:
            yield i
def generator_neparni(broj):
    for i in range(broj):
        if i % 2 != 0:
            yield i

limit = 10
print("parni brojevi:")
for parni in generator_parni(limit):
    print(parni)
print("neparni brojevi:")
for neparni in generator_neparni(limit):
    print(neparni)
