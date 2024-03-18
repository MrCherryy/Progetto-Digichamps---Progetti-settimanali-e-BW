studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]
nomi_posizione_pari = []
nomi_posizione_dispari = []
i = 0
for i in range (len(studenti)):
    if i % 2 == 0: # calcolo per vedere se l'indice è divisibile per 2
        nomi_posizione_pari.append(studenti[i])
    else:
        nomi_posizione_dispari.append(studenti[i])
print ("Nomi_posizione_pari:", nomi_posizione_pari)
print ("Nomi_posizione_dispari:", nomi_posizione_dispari)