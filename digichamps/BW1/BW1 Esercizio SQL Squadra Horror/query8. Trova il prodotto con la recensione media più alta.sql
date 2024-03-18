#query8. Trova il prodotto con la recensione media più alta.
SELECT   prodotti.categoria,
         Avg(ratings_dataset.rating) AS media_rating
FROM     prodotti
JOIN     ratings_dataset
ON       prodotti.prodottoid = ratings_dataset.productid
GROUP BY categoria
ORDER BY media_rating DESC limit 1;