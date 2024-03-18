Nunmero_potenze = int(input("Inserisci il numero di potenze da calcolare: "))
Numero_base = int(input("Inserisci il numero di base: "))

potenze = []
for i in range(1, Nunmero_potenze+1):
    potenza = Numero_base ** i
    potenze.append(potenza)

print("Le prime", Nunmero_potenze, "potenze di", Numero_base, "sono:")
print(potenze)