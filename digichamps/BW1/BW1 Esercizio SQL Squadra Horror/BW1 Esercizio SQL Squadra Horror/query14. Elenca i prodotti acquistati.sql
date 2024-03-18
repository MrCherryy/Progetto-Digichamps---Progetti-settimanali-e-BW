#query.14 Elenca i prodotti acquistati
SELECT c.nomecliente,
       p.nomeprodotto,
       p.categoria,
       t.quantitaacquistata,
       ( p.prezzo * t.quantitaacquistata ) AS TotaleSpeso
FROM   clienti c
       JOIN transazioni t
         ON c.clienteid = t.clienteid
       JOIN prodotti p
         ON p.prodottoid = t.prodottoid
GROUP  BY c.nomecliente,
          p.nomeprodotto,
          p.categoria,
          t.quantitaacquistata,
          totalespeso
ORDER  BY c.nomecliente,
          p.nomeprodotto; 