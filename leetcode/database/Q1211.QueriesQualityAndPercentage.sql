SELECT query_name,
  ROUND(AVG(rating / position), 2) AS quality,
  ROUND(AVG(CASE WHEN rating < 3 THEN 100 ELSE 0 END), 2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name;
