SELECT * FROM e_commerce.transazioni;
#primo esercizio#
SELECT MONTH(DataTransazione) AS Mese, YEAR(DataTransazione) AS Anno, SUM(ImportoTransazione) AS Totale_Vendite
FROM transazioni
GROUP BY Mese, Anno
ORDER BY Anno, Mese;

#2° esercizio#
SELECT p.NomeProdotto, SUM(t.QuantitaAcquistata) AS quantità_venduta
FROM prodotti AS p
INNER JOIN transazioni t ON p.ProdottoID = t.ProdottoID
GROUP BY p.NomeProdotto
ORDER BY SUM(t.QuantitaAcquistata) DESC
LIMIT 3;

#3° esercizio#
SELECT c.NomeCliente, COUNT(t.TransazioneID) as numero_acquisti
FROM clienti c
JOIN transazioni t ON c.ClienteID = t.ClienteID
GROUP BY c.NomeCliente
ORDER BY numero_acquisti DESC
LIMIT 1;

#quarto esercizio#
SELECT Categoria as Categoria, AVG(ImportoTransazione) AS MediaTransazione
FROM prodotti p
JOIN transazioni t ON p.ProdottoID=t.ProdottoID
Group by Categoria
Order BY MediaTransazione;

#quinto esercizio#
SELECT Categoria as Categoria, SUM(QuantitaAcquistata) AS QNTTOT
FROM prodotti p
JOIN transazioni t ON p.ProdottoID=t.ProdottoID
GROUP by Categoria
ORDER BY QNTTOT DESC;

#Sesto esercizio#
SELECT c.NomeCliente AS Cliente, SUM(ImportoTransazione) AS TotAcquisti
FROM clienti c
JOIN transazioni t ON t.ClienteID=c.ClienteID
group by Cliente
Order by TotAcquisti DESC
LIMIT 1;

#Settimo Esercizio#
SELECT (COUNT(StatusConsegna) * 100) / (SELECT COUNT(StatusConsegna) FROM spedizioni) AS perc_consegna_riuscita
FROM spedizioni
WHERE StatusConsegna = 'Consegna Riuscita';

#ottavo esercizio#

SELECT prodotti.Categoria, AVG(ratings_dataset.rating) as media_rating
FROM prodotti
JOIN ratings_dataset ON prodotti.ProdottoID = ratings_dataset.ProductID
GROUP BY Categoria
ORDER BY media_rating
DESC LIMIT 1;

#Nono esercizio usando LAG#

SELECT DATE_FORMAT(t1.DataTransazione, '%Y-%m') AS Mese_corrente, 
    SUM(t1.ImportoTransazione) AS vendite_correnti, 
    LAG(SUM(t1.ImportoTransazione)) OVER (ORDER BY DATE_FORMAT(t1.DataTransazione, '%Y-%m') DESC) AS vendite_precedenti, 
    ((SUM(t1.ImportoTransazione) - LAG(SUM(t1.ImportoTransazione)) OVER (ORDER BY DATE_FORMAT(t1.DataTransazione, '%Y-%m') DESC)) / LAG(SUM(t1.ImportoTransazione)) OVER (ORDER BY DATE_FORMAT(t1.DataTransazione, '%Y-%m') DESC)) * 100 AS variazione_percentuale 
FROM transazioni AS t1 
GROUP BY Mese_corrente 
ORDER BY Mese_corrente DESC 
LIMIT 0, 1000;


with trans_grouped as ( -- common table expression (cte)
	select sum(importotransazione) importo
		, year(datatransazione) anno
        , month(DataTransazione) mese
		from transazioni 
		group by year(datatransazione), month(datatransazione)
), 
analisi as ( -- altra common table expression
select 
    anno, 
    mese, 
    importo,
	(select importo 
		from trans_grouped g 
        where g.mese = t.mese -1
	) mese_precedente,
    convert(importo / (select importo 
		from trans_grouped g 
        where g.mese = t.mese -1
	), decimal(10,2)) percentuale
from trans_grouped t 
order by anno, mese
)
select anno, mese, importo, mese_precedente, percentuale, 
case when percentuale is null then '▬' when percentuale >= 1 then '▲' else '▼' end andamento 
from analisi; 

#Esercizio 10, quantità media disponibile per categoria prodotto#
SELECT p.Categoria, AVG(p.QuantitaDisponibile) AS QuantitaMediaDisponibile
FROM prodotti p
GROUP BY p.Categoria
ORDER BY QuantitaMediaDisponibile;

#Esercizio 11, trova il metodo di spedizione più utilizzato#
SELECT MetodoSpedizione, COUNT(MetodoSpedizione) AS NumeroSpedizioni
FROM spedizioni
GROUP BY MetodoSpedizione
ORDER BY NumeroSpedizioni DESC; 

#Esercizio 12 Calcola il numero medio di clienti registrati al mese#
SELECT DATE_FORMAT(DataRegistrazione, '%Y, %m') AS Mese, AVG(ClienteID) AS MediaClientiRegistrati
FROM clienti
GROUP BY DATE_FORMAT(DataRegistrazione, '%Y, %m')
ORDER BY Mese; 
#Esercizio 12 più pulito#
SELECT MONTH(DataRegistrazione) AS Mese, YEAR (DataRegistrazione) AS Anno, AVG(ClienteID) AS MediaClientiRegistrati
FROM clienti
GROUP BY Mese, Anno
ORDER By Anno, Mese;

#Esercizio 13 Identifica i prodotti con una quantità disponibile inferiore alla media#
SELECT *
FROM prodotti
WHERE QuantitaDisponibile < (SELECT AVG(QuantitaDisponibile) FROM prodotti)
Order by QuantitaDisponibile;

#Esercizio 14 Elenca i prodotti acquistati#
SELECT c.NomeCliente, p.NomeProdotto, p.Categoria, t.QuantitaAcquistata, (p.Prezzo * t.QuantitaAcquistata) AS TotaleSpeso 
FROM clienti c 
JOIN transazioni t ON c.ClienteID = t.ClienteID 
JOIN prodotti p ON p.ProdottoID = t.ProdottoID 
GROUP BY c.NomeCliente, p.NomeProdotto, p.Categoria, t.QuantitaAcquistata, TotaleSpeso 
ORDER BY c.NomeCliente, p.NomeProdotto;

#Esercizio 15, Identifica il mese con il maggior importo totale delle vendite.#
SELECT DATE_FORMAT(DataTransazione, '%m-%Y') AS Mese, SUM(ImportoTransazione) AS ImportoTotaleVendite
FROM transazioni
GROUP BY Mese
ORDER BY ImportoTotaleVendite DESC
LIMIT 1;

#Esercizio 16, Trova la quantità totale di prodotti disponibili in magazzino#
SELECT SUM(QuantitaDisponibile) AS TotaleProdottiDisponibili
FROM prodotti;

#Esercizio 17, Identifica i clienti che non hanno effettuato alcun acquisto#
SELECT c.ClienteID, c.NomeCliente, c.Email, c.DataRegistrazione
FROM clienti c
LEFT JOIN transazioni t ON c.ClienteID = t.ClienteID
WHERE t.TransazioneID IS NULL;

SELECT COUNT(*) AS TotalCount
FROM (
    SELECT c.ClienteID, c.NomeCliente, c.Email, c.DataRegistrazione
    FROM clienti c
    LEFT JOIN transazioni t ON c.ClienteID = t.ClienteID
    WHERE t.TransazioneID IS NULL
) AS Result;

#Esercizio 18, Calcola il totale vendite per ogni anno#
SELECT YEAR(DataTransazione) AS Anno, SUM(ImportoTransazione) AS TotaleVendite
FROM transazioni
GROUP BY YEAR(DataTransazione);

#Esercizio 19#
SELECT COUNT(*) * 100.0 / (SELECT COUNT(*) FROM spedizioni) AS Percentuale
FROM spedizioni
WHERE StatusConsegna = 'in consegna';


#EXTRA#
#1 EXTRA, Query per ottenere l'elenco dei clienti che hanno effettuato una transazione nello stesso giorno di registrazione#
SELECT c.NomeCliente, c.DataRegistrazione, t.DataTransazione 
FROM clienti c
INNER JOIN transazioni t ON c.ClienteID = t.ClienteID
WHERE DATE(c.DataRegistrazione) = DATE(t.DataTransazione);



