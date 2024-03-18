#query.19 Trova la percentuale di spedizioni con "in consegna" rispetto al totale
SELECT Count(*) * 100.0 / (SELECT Count(*)
                           FROM   spedizioni) AS Percentuale
FROM   spedizioni
WHERE  statusconsegna = 'in consegna'; 