#query3. Trova il cliente che ha effettuato il maggior numero di acquisti.
SELECT   c.clienteid          AS cliente,
         Count(transazioneid) AS quantitaacquistata
FROM     clienti c
JOIN     transazioni t
ON       t.clienteid=c.clienteid
GROUP BY cliente
ORDER BY quantitaacquistata DESC limit 1;