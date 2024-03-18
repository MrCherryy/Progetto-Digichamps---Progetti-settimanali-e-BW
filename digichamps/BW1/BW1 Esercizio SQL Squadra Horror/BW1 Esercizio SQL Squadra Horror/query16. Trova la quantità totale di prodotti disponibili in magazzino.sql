#query.16 Trova la quantità totale di prodotti disponibili in magazzino
SELECT Sum(quantitadisponibile) AS TotaleProdottiDisponibili
FROM   prodotti; 