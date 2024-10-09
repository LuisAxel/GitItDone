WITH
  Requests_per_day AS (
    SELECT t.request_at, count(*) as requests
    FROM Trips t JOIN
      Users c ON (t.client_id = c.users_id) JOIN
      Users d ON (t.driver_id = d.users_id)
    WHERE c.banned != 'Yes' AND
      d.banned != 'Yes' AND
      t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
    GROUP BY t.request_at
  ),
  Cancells_per_day AS (
    SELECT t.request_at, count(*) as cancelled
    FROM Trips t JOIN
      Users c ON (t.client_id = c.users_id) JOIN
      Users d ON (t.driver_id = d.users_id)
    WHERE c.banned != 'Yes' AND
      d.banned != 'Yes' AND
      SUBSTR(t.status,1,9) = 'cancelled' AND
      t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
    GROUP BY t.request_at
);

SELECT rpd.request_at AS "Day",
  ROUND(NVL(cpd.cancelled, 0)/rpd.requests,2) AS "Cancellation Rate"
FROM Requests_per_day rpd LEFT OUTER JOIN
  Cancells_per_day cpd ON (rpd.request_at = cpd.request_at);
