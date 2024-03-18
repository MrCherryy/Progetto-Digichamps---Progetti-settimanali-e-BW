#Esercizio 1.
#Task 1: Fare la spesa Algoritmo:

#1) Prendi una lista vuota per gli elementi della spesa.
#2) Entra nel negozio e prendi un carrello.
#3) Scorri la lista dei prodotti necessari.
#4) Per ogni prodotto nella lista, aggiungi il prodotto al carrello.
#5) Se ci sono altri prodotti necessari, torna allo step precedente. Altrimenti prosegui.
#6) Vai alla cassa e paga per gli articoli nel carrello.
#7) Esci dal negozio con le borse della spesa contenenti gli articoli acquistati.

#Task 2: Studiare un concetto Algoritmo:

#1) Scegli il concetto che vuoi apprendere.
#2) Prendi del materiale di studio (come libri, appunti, video, ecc.).
#3) Trova un ambiente tranquillo e privo di distrazioni.
#4) Inizia con una panoramica generale del concetto per capire l'argomento principale.
#5) Leggi attentamente il materiale di studio e prendi appunti.
#6) Fai riferimento a esempi pratici o casi reali per comprendere meglio il concetto.
#7) Fai esercizi o risolvi problemi correlati al concetto per acquisire competenza pratica.
#8) Se hai domande o dubbi, cerca risposte o chiedi spiegazioni ad esperti o compagni di studio.
#9) Ripeti i passaggi 5-8 fino a quando non acquisisci una buona comprensione del concetto.
#10) Rifletti su ciò che hai imparato e cerca di applicare il concetto a situazioni reali.
#11) Ripeti periodicamente lo studio del concetto per consolidare la conoscenza.

#Task 3: Acquistare uno snack da un distributore automatico Algoritmo:

#1) Trova un distributore automatico con snack disponibili.
#2) Prepara il denaro necessario per acquistare lo snack.
#3) Avvicinati al distributore automatico.
#4) Guarda il display del distributore automatico per vedere le opzioni disponibili.
#5) Scegli lo snack desiderato premendo il pulsante corrispondente.
#6) Inserisci il denaro richiesto secondo le indicazioni del display e utilizzando uno dei metodi di pagamento a tua disposizione.
#7) Raccogli lo snack che viene erogato dal distributore automatico.
#8) Controlla che lo snack sia in buone condizioni.
#9) Se si desidera acquistare un altro snack, torna al passo 4.
#10) Se non si desidera acquistare ulteriori snack, allontanati dal distributore automatico.

#Esercizio 2.
studenti = 25

#Esercizio 3.
studenti_nuovi = 3

print (studenti)
print (studenti_nuovi) 

#Esercizio 4.

totale_studenti = studenti + studenti_nuovi
print(totale_studenti)

#Esercizio 5.
organizzazioneCorso = "Epicode"
print (organizzazioneCorso)

#Esercizio 6.
Lista = [0, 1, 2, 3, 4, 5]
print (Lista)

#Esercizio 7.
nome_scuola = "Epicode"
print (nome_scuola[0]) 

#Esercizio 8.
print (nome_scuola[0:3])

#Esercizio 9.
x = 10
x += 2  
x *= 3
print (x)

x = 10
x = x + 2 # incremento di 2
x = x * 3 # moltiplicazione per 3

print (x)

#Esercizio 10.
stringa = input("Inserisci una stringa: ") 
primi_3_caratteri = stringa[:4] 
ultimi_3_caratteri = stringa[-3:] 
output = primi_3_caratteri + "..." + ultimi_3_caratteri 
print(output)



#Esercizio 10 scritto meglio.
s = input("Inserisci una stringa: ") 
output = s[:3] + "..." + s[-3:] 
print(output)

#Esercizio 11
w = "Windows"
e ="Excel"
p = "Powerpoint"
wd = "Word"
conta_caratteri = len(w)
print (conta_caratteri)
conta_caratteri = len(e)
print (conta_caratteri)
conta_caratteri = len(p)
print (conta_caratteri)
conta_caratteri = len(wd)
print (conta_caratteri)

#Esercizio 11 bis, fatto con for in
stringhe = ["Windows", "Excel", "Powerpoint", "Word"]

for string in stringhe:
    numero_caratteri = len(string)
    if 5 <= numero_caratteri <= 8:
        print(f'La stringa "{string}" ha un numero di caratteri compreso tra 5 e 8.')
    else:
        print(f'La stringa "{string}" non ha un numero di caratteri compreso tra 5 e 8.')

#Esercizio 12.
def somma_numeri():
    primo_numero = int(input("Inserisci il primo numero: "))
    secondo_numero = int(input("Inserisci il secondo numero: "))
    somma = primo_numero + secondo_numero
    print("La somma dei due numeri è:", somma)

somma_numeri()

#Esercizio Extra Prof 1.

parola1 = input("Inserisci la prima parola: ")
parola2 = input("Inserisci la seconda parola: ")
parola3 = input("Inserisci la terza parola: ")

parola1_maiuscolo = parola1.upper()
parola2_minuscolo = parola2.lower()
parola3_maiuscola = parola3.capitalize()

print(parola1_maiuscolo[:3])
print(parola2_minuscolo[:3])
print(parola3_maiuscola[:3])

#Esercizio Extra Prof 2.

parola1 = input("Inserisci la prima parola: ")
parola2 = input("Inserisci la seconda parola: ")
parola3 = input("Inserisci la terza parola: ")

prodotto_lunghezze = len(parola1) * len(parola2) * len(parola3)

print("Il prodotto delle lunghezze delle parole è", prodotto_lunghezze)