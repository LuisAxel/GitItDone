WITH User_id AS (
  SELECT requester_id AS id
  FROM RequestAccepted
  UNION ALL
  SELECT accepter_id AS id
  FROM RequestAccepted
)

SELECT *
FROM (
  SELECT id, COUNT(*) AS num
  FROM User_id
  GROUP BY id
  ORDER BY num DESC)
WHERE ROWNUM = 1;
