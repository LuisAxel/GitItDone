WITH Manager_id AS (
  SELECT managerId
  FROM Employee
  GROUP BY managerId
  HAVING COUNT(*) >= 5
)

SELECT e.name
FROM Employee e JOIN
  Manager_id m ON (e.id = m.managerId)
