def menu () -> int:
    print ("1. Aggiungi")
    print("2. Elenca")
    print("3. Esci")


def inserisci () :
    nome = input ("Nome: ")
    telefono = input ("NUmero di telefono: ")
    return nome, telefono

def rubrica ():
    print ("Rubrica telefonica")
    for nome, numero in rubrica.items():
        print(f"{nome}: {numero}")

def visualizza():
    for i in rubrica:
        print("Nome:", i["nome"], "Telefono", i["telefono"])

scelta = -1
while scelta !=0:
    scelta = menu()
    if scelta == 1:
        nome, numero = inserisci()
        rubrica.append({'nome': nome, 'telefono': numero})
    elif scelta == 2:
        visualizza()