#query18. Calcola il totale delle vendite per ogni anno.
SELECT YEAR(DataTransazione) as Anno, sum(p.Prezzo*t.QuantitaAcquistata) as TotVendite
FROM transazioni t
JOIN prodotti p ON p.ProdottoID=t.ProdottoID
GROUP BY Anno
ORDER BY TotVendite DESC;