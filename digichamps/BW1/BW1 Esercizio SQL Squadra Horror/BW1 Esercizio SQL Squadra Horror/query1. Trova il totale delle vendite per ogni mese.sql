#query1. Trova il totale delle vendite per ogni mese
SELECT monthname(DataTransazione) AS Mese, sum(p.Prezzo*t.QuantitaAcquistata) as SommaTransazione
FROM prodotti p
JOIN transazioni t ON p.ProdottoID=t.ProdottoID
group by Mese
order by SommaTransazione
DESC;