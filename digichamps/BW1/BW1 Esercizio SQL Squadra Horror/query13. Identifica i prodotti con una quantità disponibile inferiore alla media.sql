#query13. Identifica i prodotti con una quantità disponibile inferiore alla media.
SELECT nomeprodotto,
       categoria,
       quantitadisponibile
FROM   prodotti
WHERE  quantitadisponibile < (SELECT Avg(quantitadisponibile)
                              FROM   prodotti)
ORDER  BY quantitadisponibile,
          nomeprodotto;

SELECT categoria,
       Sum(quantitadisponibile) AS quantitadisponibile
FROM   prodotti
WHERE  quantitadisponibile < (SELECT Avg (quantitadisponibile)
                              FROM   prodotti)
GROUP  BY categoria
ORDER  BY quantitadisponibile; 