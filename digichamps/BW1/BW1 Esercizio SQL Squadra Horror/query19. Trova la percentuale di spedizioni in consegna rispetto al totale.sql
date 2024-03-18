#query.19 Trova la percentuale di spedizioni con "in consegna" rispetto al totale
SELECT (count(StatusConsegna) * 100) / (SELECT count(StatusConsegna) FROM spedizioni) AS InConsegna
FROM spedizioni
WHERE StatusConsegna='In Consegna';