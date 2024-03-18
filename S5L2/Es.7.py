def visualizza_caratteri(stringa):
    if len(stringa) < 6:
        print("La stringa che hai inserito è inferiore a sei caratteri, mi spiace! Avevi inserito " + stringa)
    else:
        primi_caratteri = stringa[:3]
        ultimi_caratteri = stringa[-3:]
        print(primi_caratteri + "..." + ultimi_caratteri)

input_stringa = input("Inserisci una stringa. Nell'output vedrai i primi 3 caratteri, seguiti da ... e gli ultimi 3 caratteri: ")
visualizza_caratteri(input_stringa)