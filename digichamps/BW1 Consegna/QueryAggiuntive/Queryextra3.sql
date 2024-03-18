#Query extra 3: Trova il nome del prodotto, la data di transazione e la data di spedizione degli ultimi dieci prodotti acquistati. Elenca anche quanti giorni siano trascorsi dalla data di transazione a quella di spedizione
SELECT P.nomeprodotto,
       Date_format(T.datatransazione, '%Y-%m-%d')         AS DataTransazione,
       Date_format(S.dataspedizione, '%Y-%m-%d')          AS DataSpedizione,
       Abs(Datediff(T.datatransazione, S.dataspedizione)) AS GiorniPassati
FROM   spedizioni AS S
       INNER JOIN transazioni AS T
               ON S.spedizioneid = T.spedizioneid
       INNER JOIN prodotti AS P
               ON T.prodottoid = P.prodottoid
WHERE  S.statusconsegna <> 'consegnato'
       AND S.statusconsegna = 'in consegna'
ORDER  BY T.datatransazione DESC
LIMIT  10;