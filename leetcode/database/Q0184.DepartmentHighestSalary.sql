WITH rank_salaries AS (
  SELECT id, name, salary, departmentId,
    RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS rank
  FROM Employee
);

SELECT d.name AS Department, r.name AS Employee, r.salary AS Salary
FROM Department d JOIN
  rank_salaries r ON (d.id = r.departmentId)
WHERE r.rank = 1;
