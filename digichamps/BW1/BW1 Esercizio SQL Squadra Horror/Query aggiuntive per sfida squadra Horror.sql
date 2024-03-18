#Query extra1: Trova i clienti che hanno effettuato transazioni per prodotti con un rating superiore a 1 e che le hanno eseguite il 2022-12-16
SELECT c.nomecliente
FROM   clienti c
       JOIN transazioni t
         ON c.clienteid = t.clienteid
       JOIN ratings_dataset r
         ON t.prodottoid = r.productid
WHERE  r.rating > 1
       AND t.datatransazione = '2022-12-16';

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

#Query extra4: Considerando i prodotti della Categoria Abbigliamento nel periodo Primavera-Estate e Autunno-Primavera, trova la quantità totale di prodotti acquistati e totale speso, arrotondando laddove necessario (Suggerimento/N.B: il totale speso, non il totale transazione)
SELECT CASE
         WHEN Month(datatransazione) IN ( 10, 11, 12, 1, 2 ) THEN
         'Autunno-Inverno'
         WHEN Month(datatransazione) IN ( 3, 4, 5, 6,
                                          7, 8, 9 ) THEN 'Primavera-Estate'
       end                                            AS Periodo,
       p. categoria                                   AS Categoria,
       Sum(quantitaacquistata)                        AS TotaleQuantita,
       Round(Sum(p.prezzo * t.quantitaacquistata), 0) AS TotaleSpeso
FROM   transazioni AS t
       INNER JOIN prodotti AS p
               ON t.prodottoid = p.prodottoid
WHERE  p.categoria LIKE '%abbigliamento%'
GROUP  BY periodo,
          p.categoria
ORDER  BY totalespeso DESC
LIMIT  0, 1000; 