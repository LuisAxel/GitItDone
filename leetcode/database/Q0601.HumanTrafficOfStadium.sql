WITH stadium_rnk AS (
  SELECT id, visit_date, people, id - RANK() OVER(ORDER BY id) AS island
  FROM Stadium
  WHERE people >= 100
);

SELECT id, TO_CHAR(visit_date, 'YYYY-MM-DD') AS visit_date, people
FROM stadium_rnk
WHERE island IN (
    SELECT island
    FROM stadium_rnk
    GROUP BY island
    HAVING COUNT(*) >= 3
  )
ORDER BY visit_date ASC;
