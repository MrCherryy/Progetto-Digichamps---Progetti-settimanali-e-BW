#query2. Identifica i tre prodotti più venduti e la loro quantità venduta
SELECT   pr.nomeprodotto            AS prodotto,
         pr.categoria                  categoria,
         Sum(tr.quantitaacquistata) AS quantitavenduta
FROM     prodotti pr
JOIN     transazioni tr
ON       pr.prodottoid=tr.prodottoid
GROUP BY prodotto,
         categoria
ORDER BY quantitavenduta DESC limit 3;