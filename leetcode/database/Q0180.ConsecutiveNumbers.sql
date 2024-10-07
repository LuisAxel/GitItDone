SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num, id - DENSE_RANK() OVER(PARTITION BY num ORDER BY id) AS rank
    FROM Logs
  )
GROUP BY num, rank
HAVING COUNT(rank) >= 3;
