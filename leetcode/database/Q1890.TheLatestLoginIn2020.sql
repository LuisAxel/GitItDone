WITH Logins_rn AS (
  SELECT user_id, time_stamp,
    RANK() OVER(PARTITION BY user_id ORDER BY time_stamp DESC) AS rn
  FROM Logins
  WHERE TO_CHAR(time_stamp,'YYYY') = '2020'
)

SELECT user_id, time_stamp AS last_stamp
FROM Logins_rn
WHERE rn = 1;
