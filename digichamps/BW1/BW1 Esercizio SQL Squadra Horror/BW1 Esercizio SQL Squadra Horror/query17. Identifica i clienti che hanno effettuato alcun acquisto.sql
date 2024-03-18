#query.17 Identifica i clienti che non hanno effettuato alcun acquisto
SELECT c.clienteid,
       c.nomecliente,
       c.email,
       c.dataregistrazione
FROM   clienti c
       LEFT JOIN transazioni t
              ON c.clienteid = t.clienteid
WHERE  t.transazioneid IS NULL;

SELECT Count(*) AS NumeroClientiSenzaTransazione
FROM   (SELECT c.clienteid,
               c.nomecliente,
               c.email,
               c.dataregistrazione
        FROM   clienti c
               LEFT JOIN transazioni t
                      ON c.clienteid = t.clienteid
        WHERE  t.transazioneid IS NULL) AS Result; 