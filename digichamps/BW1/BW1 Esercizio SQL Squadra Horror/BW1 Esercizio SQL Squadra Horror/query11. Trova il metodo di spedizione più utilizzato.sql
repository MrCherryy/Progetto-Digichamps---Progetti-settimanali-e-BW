#query11. Trova il metodo di spedizione più utilizzato
SELECT   metodospedizione,
         Count(metodospedizione) AS NumeroSpedizioni
FROM     spedizioni
GROUP BY metodospedizione
ORDER BY numerospedizioni DESC;