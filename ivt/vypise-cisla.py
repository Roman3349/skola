# Vypíše přirozená čísla do určitého čísla

def vypisCisla():
    vratCisla(osetriVstup(input("Zadej číslo, do kterého chceš vypsat všechna přirozená čísla: ")))
    print("")

"""
    Vrátí přirozená čísla
"""
def vratCisla(x):
    for i in range(1, x+1):
        print(str(i), end = "\t")

"""
    Ověří, zda je uživatelský vstup číselná hodnota, která je nenulová
"""
def osetriVstup(string):
    while not jeCislo(string):
        string = input("Hodnota musí být přirozené číslo. Zadejte novou hodnotu: ")
    return(int(string))

"""
    Zkontroluje, zda textový řetězec obsahuje číselnou hodnotu
"""
def jeCislo(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

while True:
    vypisCisla()
