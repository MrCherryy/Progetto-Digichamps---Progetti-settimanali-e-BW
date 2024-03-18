prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"]

prezzi_dollari = []  # creo una lista vuota per memorizzare i prezzi in dollari

for prezzo_da_correggere in prezzi:
    prezzo_dollari = prezzo_da_correggere.replace("€", "$")
    prezzi_dollari.append(prezzo_dollari)

print(prezzi_dollari)