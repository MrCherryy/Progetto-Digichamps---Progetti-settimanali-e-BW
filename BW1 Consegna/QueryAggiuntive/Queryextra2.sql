#Query extra2: Restituisci il nome del prodotto, la quantità disponibile e il metodo di spedizione per tutte le spedizioni non ancora consegnate. Elenca i dieci prodotti meno disponibili
SELECT P.nomeprodotto,
       P.quantitadisponibile,
       S.metodospedizione
FROM   spedizioni AS S
       INNER JOIN transazioni AS T
               ON S.spedizioneid = T.spedizioneid
       INNER JOIN prodotti AS P
               ON T.prodottoid = P.prodottoid
WHERE  S.statusconsegna <> 'consegnato'
ORDER  BY quantitadisponibile ASC
LIMIT  10;