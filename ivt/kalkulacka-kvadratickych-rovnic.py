# Výpočet kvadratické rovnice

def vypoctiRci():
    print("*****************************************************")
    print("Zadejte kvadratickou rovnici podle vzoru ax^2+bx+c=0.")
    print("*****************************************************")
    a=osetriVstup(input("Zadejte hodnotu a: "), True)
    b=osetriVstup(input("Zadejte hodnotu b: "))
    c=osetriVstup(input("Zadejte hodnotu c: "))
    print(vratReseni(a, b, c))

"""
    Vypočítá diskriminant
"""
def vypoctiD(a, b, c):
    return(b**2-4*a*c)

"""
    Vypočítá kořeny kvadratické rovnice
"""
def vypoctiKoreny(a, b, c, D):
    if(D == 0):
        return(str((-b-D**0.5)/(2*a)))
    else:
        return(str((-b+D**0.5)/(2*a)) + ", " + str((-b-D**0.5)/(2*a)))

"""
    Vrátí řešení kvadratické rovnice
"""
def vratReseni(a, b, c):
    D = vypoctiD(a, b, c)
    if(D < 0):
        return("Tato rovnice nemá v oboru reálných čísel řešení.")
    elif(D == 0):
        return("Tato rovnice má dvojnásobný kořen: " + vypoctiKoreny(a, b, c, D) + ".")
    else:
        return("Tato rovnice má dva kořeny: " + vypoctiKoreny(a, b, c, D) + ".")
"""
    Ověří zda js uživatelský vstup číselná hodnota, která je nenulová
"""
def osetriVstup(string, notZero = False):
    while not jeCislo(string):
        string = input("Hodnota musí být číslo. Zadejte novou hodnotu: ")
    while notZero and string == str(0):
        string = osetriVstup(input("Hodnota musí být nenulová. Zadejte novou hodnotu: "), notZero)
    return(float(string))
"""
    Zkontroluje, zda řetězec obsahuje číselnou hodnotu
"""
def jeCislo(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

while True:
    vypoctiRci()
