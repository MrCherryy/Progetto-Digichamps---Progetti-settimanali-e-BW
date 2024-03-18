def media_numeri(lista, K):
    numeri_maggiori = [n for n in lista if n >= K]
    if numeri_maggiori:
        media = sum(numeri_maggiori) / len(numeri_maggiori)
        return media
    else:
        print("Non ci sono numeri maggiori o uguali a K nella lista.")

# Esempio di utilizzo della funzione
lista_numeri = [12, 10, 8, 15, 7, 9]
K = 50
risultato = media_numeri(lista_numeri, K)
if risultato is not None:
    print("La media dei numeri maggiori o uguali a", K, "è", risultato)