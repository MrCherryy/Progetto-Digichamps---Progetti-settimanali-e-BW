guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50]
somma = 0
i = 0

while i < len(guadagni):
    somma += guadagni[i]
    i += 1

media = somma / len(guadagni)
print("La media dei guadagni è:", media)