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