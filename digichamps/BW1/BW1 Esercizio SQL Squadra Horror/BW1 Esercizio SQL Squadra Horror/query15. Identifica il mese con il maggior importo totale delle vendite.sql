#query.15 Identifica il mese con il maggior importo totale delle vendite.
SELECT Date_format(datatransazione, '%m-%Y') AS mese,
       Sum(importotransazione)               AS importototalevendite
FROM   transazioni
GROUP  BY mese
ORDER  BY importototalevendite DESC
LIMIT  1; 
