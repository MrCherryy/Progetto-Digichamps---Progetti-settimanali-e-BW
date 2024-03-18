#query5. Determina la categoria di prodotto con il maggior numero di vendite
SELECT   categoria               AS Categoria,
         Sum(quantitaacquistata) AS QNTTOT
FROM     prodotti p
JOIN     transazioni t
ON       p.prodottoid=t.prodottoid
GROUP BY categoria
ORDER BY qnttot DESC;