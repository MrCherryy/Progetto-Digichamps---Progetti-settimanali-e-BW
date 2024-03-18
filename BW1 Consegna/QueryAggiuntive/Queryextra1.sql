#Query extra1: Trova i clienti che hanno effettuato transazioni per prodotti con un rating superiore a 1 e che le hanno eseguite il 2022-12-16
SELECT c.nomecliente
FROM   clienti c
       JOIN transazioni t
         ON c.clienteid = t.clienteid
       JOIN ratings_dataset r
         ON t.prodottoid = r.productid
WHERE  r.rating > 1
       AND t.datatransazione = '2022-12-16';