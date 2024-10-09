SELECT player_id, MIN(TO_CHAR(event_date, 'YYYY-MM-DD')) AS first_login
FROM Activity
GROUP BY player_id
ORDER BY player_id;
