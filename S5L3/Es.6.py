def tre_numeri_piu_grandi(lista):
    if len(lista) < 3:
        print("La lista è troppo corta")
        return
    numeri_piu_grandi = [lista[0], lista[1], lista[2]]
    lista.sort(reverse=True)
    if numeri_piu_grandi[0] == numeri_piu_grandi[1]:
        print("Ci sono numeri uguali tra i primi tre")
        return
    elif numeri_piu_grandi[0] == numeri_piu_grandi[2]:
        print("Ci sono numeri uguali tra i primi tre")
        return
    elif numeri_piu_grandi[1] == numeri_piu_grandi[2]:
        print("Ci sono numeri uguali tra i primi tre")
        return

    return numeri_piu_grandi

lista = [10, 5, 4, 1]
risultato = tre_numeri_piu_grandi(lista)
if risultato:
    print("I tre numeri più grandi sono:", risultato)