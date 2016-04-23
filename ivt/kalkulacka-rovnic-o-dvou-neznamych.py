# Výpočet kvadratické rovnice

def vypoctiRci():
    print("***************************************************************")
    print("Zadejte rovnici o dvou neznámých  podle vzoru ax+by=c; dx+ey=f.")
    print("***************************************************************")
    a=osetriVstup(input("Zadejte hodnotu a: "))
    b=osetriVstup(input("Zadejte hodnotu b: "))
    c=osetriVstup(input("Zadejte hodnotu c: "))
    d=osetriVstup(input("Zadejte hodnotu d: "))
    e=osetriVstup(input("Zadejte hodnotu e: "))
    f=osetriVstup(input("Zadejte hodnotu f: "))
    print(vratReseni(a, b, c, d, e, f))

"""
    Vypočítá kořeny
"""
def vypoctiKoreny(a, b, c, d, e, f):
    y = (a*f-d*c) / (a*e-d*b)
    if not a == 0:
        x = (c-b*y) / a
    else:
        x = (f-e*y) / d
    return [x, y]

"""
    Vrátí řešení kvadratické rovnice
"""
def vratReseni(a, b, c, d, e, f):
    if (a*f-d*c) == 0 and (a*e-d*b) == 0:
        return("Tato rovnice má nekonečně mnoho řešení.")
    elif (a*f-d*c) == 0 or (a*e-d*b) == 0:
        return("Tato rovnice nemá řešení.")
    else:
    	return("x=" + str(koreny[0]) + " y=" + str(koreny[1]))

"""
    Ověří, zda je uživatelský vstup číselná hodnota, která je nenulová
"""
def osetriVstup(string):
    while not jeCislo(string):
        string = input("Hodnota musí být číslo. Zadejte novou hodnotu: ")
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
