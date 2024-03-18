#query12. Calcola il numero medio di clienti registrati al mese.
SELECT Month(dataregistrazione)            Mese,
       Year(dataregistrazione)             Anno,
       Count(clienteid)                    AS ClientiRegistrati,
       Count(clienteid) / (SELECT Count(clienteid)
                           FROM   clienti) AS PercentualeSulTot
FROM   clienti
GROUP  BY mese,
          anno;

SELECT Month(dataregistrazione) Mese,
       Year(dataregistrazione)  Anno,
       Count(clienteid)         AS ClientiRegistrati,
       Count(clienteid) / 12    AS MediaClientiMese
FROM   clienti
GROUP  BY mese,
          anno; 