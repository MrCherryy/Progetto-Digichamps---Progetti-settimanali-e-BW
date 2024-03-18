#Query extra4: Considerando i prodotti della Categoria Abbigliamento nel periodo Primavera-Estate e Autunno-Inverno, trova la quantità totale di prodotti acquistati e totale speso, arrotondando laddove necessario (Suggerimento/N.B: il totale speso, non il totale transazione)
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