WITH rank_department_salaries AS (
    SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary,
      DENSE_RANK() OVER(PARTITION BY d.id ORDER BY e.salary DESC) AS Rank
    FROM Department d JOIN
      Employee e ON (d.id = e.departmentID)
  );

SELECT Department, Employee, Salary
FROM rank_department_salaries
WHERE Rank <= 3;
