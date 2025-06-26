-- script to count number of records per score in sec_table
SELECT score, COUNT (*) AS number
FROM second_table
GROUP BY score 
ORDER BY number DESC;
