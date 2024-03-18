#query.18, Calcola il totale vendite per ogni anno
SELECT Year(datatransazione)                AS Anno,
       Sum(p.prezzo * t.quantitaacquistata) AS TotVendite
FROM   transazioni t
       JOIN prodotti p
         ON p.prodottoid = t.prodottoid
GROUP  BY anno
ORDER  BY totvendite DESC; 