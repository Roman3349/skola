# Výpočet lineární rovnice

def vypoctiRci():
    print("**************************")
    print("Řeším rovnici typu ax+b=0.")
    print("**************************")
    a=osetriVstup(input("Zadejte a: "), True)
    b=osetriVstup(input("Zadejte b: "))
    print(vratReseni(a, b))

"""
    Vypočítá kořen lineární rovnice
"""
def vratReseni(a, b):
    return("Výsledek je x=" + str(-b/a))

"""
    Ověří, zda je uživatelský vstup číselná hodnota, která je nenulová
"""
def osetriVstup(string, notZero = False):
    while not jeCislo(string):
        string = input("Hodnota musí být číslo. Zadejte novou hodnotu: ")
    while notZero and string == str(0):
        string = osetriVstup(input("Hodnota musí být nenulová. Zadejte novou hodnotu: "), notZero)
    return(float(string))

"""
    Zkontroluje, zda textový řetězec obsahuje číselnou hodnotu
"""
def jeCislo(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

while True:
    vypoctiRci()
