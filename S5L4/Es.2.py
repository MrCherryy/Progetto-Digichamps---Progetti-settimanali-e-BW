class Libro:
    def __init__(self, titolo, autore, anno_di_pubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.anno_di_pubblicazione = anno_di_pubblicazione
    
    def recente(self):
        anno_corrente = 2024
        if (anno_corrente - self.anno_di_pubblicazione) < 5: 
            return "Il libro è recente"
        else:
            return "Il libro non è recente"

testlibro1 = Libro ("Harry Potter e il Calice di Fuoco", "J.K.Rowling", 2001)
print("Il libro è recente?", testlibro1.recente())

        