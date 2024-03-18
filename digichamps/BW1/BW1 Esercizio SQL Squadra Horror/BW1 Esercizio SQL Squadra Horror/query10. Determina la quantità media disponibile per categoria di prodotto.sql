#query10. Determina la quantità media disponibile per categoria di prodotto.
SELECT   categoria,
         Avg(quantitadisponibile) AS MediaCategoria
FROM     prodotti
GROUP BY categoria
ORDER BY mediacategoria DESC;