#query4. Calcola il valore medio di ogni transazione.
SELECT categoria                            AS Categoria,
       Avg(p.prezzo * t.quantitaacquistata) AS MediaTransazione
FROM   prodotti p
       JOIN transazioni t
         ON p.prodottoid = t.prodottoid
GROUP  BY categoria
ORDER  BY mediatransazione DESC; 