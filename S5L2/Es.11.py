
#trovare i codici fiscali che contengono "95", metterli in una lista, e alla fine stamparla;

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]
codici_fiscali_95 = []
i = 0
while i < len(lista_cf):
    if "95" in lista_cf[i]:
        codici_fiscali_95.append(lista_cf[i])
    i += 1
print(codici_fiscali_95)

#inoltre, per ognuno di essi, stampare a video i caratteri relativi al nome e quelli relativi al cognome.

codici_fiscali_95 = []
nomi = []
cognomi = []

for codice_fiscale in lista_cf:
    if "95" in codice_fiscale:
        codici_fiscali_95.append(codice_fiscale)
        nome = codice_fiscale[6:9] # caratteri relativi al nome
        cognome = codice_fiscale[9:12] # caratteri relativi al cognome
        nomi.append(nome)
        cognomi.append(cognome)

print("Codici fiscali con '95':", codici_fiscali_95)
print("Nomi:", nomi)
print("Cognomi:", cognomi)