dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"}

# Esercizio svolto con funzione is not
for auto in dizionario_auto.values():
    if auto is not "Multipla":
        print(auto)

# Esercizio più "pulito" 
print ("Esercizio più pulito")

for auto in dizionario_auto.values():
    if auto != "Multipla":
        print(auto)