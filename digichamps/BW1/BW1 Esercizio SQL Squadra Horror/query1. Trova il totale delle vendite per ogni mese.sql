#query 1. Trova il totale delle vendite per ogni mese
SELECT   Month(datatransazione)  AS Mese,
         Year(datatransazione)   AS Anno,
         Sum(importotransazione) AS Totale_Vendite
FROM     transazioni
GROUP BY mese,
         anno
ORDER BY anno,
         mese;