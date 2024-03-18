#query6. Identifica il cliente con il maggior valore totale di acquisti.
SELECT   c.clienteid                        AS Cliente,
         Sum(p.prezzo*t.quantitaacquistata) AS TotAcquisti
FROM     clienti c
JOIN     transazioni t
ON       t.clienteid=c.clienteid
JOIN     prodotti p
ON       p.prodottoid=t.prodottoid
GROUP BY cliente
ORDER BY totacquisti DESC;