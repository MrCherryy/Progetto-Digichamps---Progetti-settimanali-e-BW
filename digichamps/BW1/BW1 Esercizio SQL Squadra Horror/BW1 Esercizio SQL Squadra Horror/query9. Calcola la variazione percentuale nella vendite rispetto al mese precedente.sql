#query9. Calcola la variazione percentuale nelle vendite rispetto al mese precedente. 
WITH trans_grouped AS (
    SELECT SUM(p.Prezzo * t.QuantitaAcquistata) importo,
        YEAR(datatransazione) anno,
        MONTH(datatransazione) mese
    FROM prodotti p
    JOIN transazioni t ON p.ProdottoID = t.ProdottoID
    GROUP BY YEAR(datatransazione),
        MONTH(datatransazione)
),
analisi AS (
    SELECT anno,
        mese,
        importo,
        (
            SELECT importo
            FROM trans_grouped g
            WHERE g.mese = t.mese - 1
        ) mese_precedente,
        CONVERT(importo / (
                SELECT importo
                FROM trans_grouped g
                WHERE g.mese = t.mese - 1
            ), DECIMAL(10, 2)) percentuale
    FROM trans_grouped t
    ORDER BY anno,
        mese
)
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
FROM analisi;