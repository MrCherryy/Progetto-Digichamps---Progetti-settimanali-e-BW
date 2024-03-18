#query9. Calcola la variazione percentuale nelle vendite rispetto al mese precedente. 
WITH trans_grouped
     AS (-- common table expression (cte)
        SELECT Sum(importotransazione) importo,
               YEAR(datatransazione)   anno,
               MONTH(datatransazione)  mese
         FROM   transazioni
         GROUP  BY YEAR(datatransazione),
                   MONTH(datatransazione)),
     analisi
     AS (-- altra common table expression
        SELECT anno,
               mese,
               importo,
               (SELECT importo
                FROM   trans_grouped g
                WHERE  g.mese = t.mese - 1)
               mese_precedente,
               Convert(importo / (SELECT importo
                                  FROM   trans_grouped g
                                  WHERE  g.mese = t.mese - 1), Decimal(10, 2))
               percentuale
         FROM   trans_grouped t
         ORDER  BY anno,
                   mese)
SELECT anno,
       mese,
       importo,
       mese_precedente,
       percentuale,
       CASE
         WHEN percentuale IS NULL THEN '▬'
         WHEN percentuale >= 1 THEN '▲'
         ELSE '▼'
       END andamento
FROM   analisi; 