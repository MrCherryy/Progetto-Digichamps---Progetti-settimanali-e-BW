#query7. Calcola la percentuale di spedizioni con "Consegna Riuscita".
SELECT ( Count(statusconsegna) * 100 ) / (SELECT Count(statusconsegna)
                                          FROM   spedizioni) AS
       perc_consegna_riuscita
FROM   spedizioni
WHERE  statusconsegna = 'Consegna Riuscita'; 