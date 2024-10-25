WITH Weight_sum AS (
    SELECT person_name,
      SUM(weight) OVER(ORDER BY turn ASC) AS running_weight
    FROM Queue
    ORDER BY running_weight DESC
)

SELECT person_name
FROM Weight_sum
WHERE running_weight <= 1000 AND
  ROWNUM = 1;
