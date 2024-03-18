def massimo (primo, secondo, terzo=0):
    m = primo
    if secondo > m:
        m = secondo
    if terzo > m:
        m = terzo
    return m

print (massimo(10, 20, 40))
print (massimo(terzo=10, primo=40, secondo=50))
print (massimo("c", terzo="a", secondo="b"))
print (massimo (10, 20))
print (massimo(-10, -20))

print ("Questo", "è", "un", "output")
print ("Questo", "è,", "un", "output", sep="*")
print ("Questo", "è", "un", "output", sep="XXX", end="")
print ("Questo", "è", "un", "altro", "output", sep="*")
