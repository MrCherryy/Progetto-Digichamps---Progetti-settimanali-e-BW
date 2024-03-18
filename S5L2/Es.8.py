Numero = input("Inserisci un numero: ") 
Numero = int(Numero)

Divisori = []
for i in range(2, Numero+1): 
    if Numero % i == 0: Divisori.append(i)
print(Divisori)