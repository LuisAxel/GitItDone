WITH first_login AS (
  SELECT player_id, MIN(event_date) as first_login
  FROM ACTIVITY
  GROUP BY player_id
);

SELECT ROUND(
    SUM(CASE WHEN d1.first_login + 1 = d2.event_date THEN 1 ELSE 0 END) /
    COUNT(DISTINCT d1.player_id)
  , 2) AS fraction
FROM first_login d1 JOIN
  Activity d2 ON (d1.player_id = d2.player_id);
