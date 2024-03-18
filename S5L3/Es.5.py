def trova_min_max(lista):
    if len(lista) == 0:
        return None
    
    minimo = lista[0]
    massimo = lista[0]
    
    for numero in lista:
        if numero < minimo:
            minimo = numero
        if numero > massimo:
            massimo = numero
    
    return minimo, massimo

numeri = [50, 50.5, 1, 8, 3]
minimo, massimo = trova_min_max(numeri)
print("Il valore minimo è:", minimo)
print("Il valore massimo è:", massimo)