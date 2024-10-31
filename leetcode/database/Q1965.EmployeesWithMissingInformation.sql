SELECT NVL(e.employee_id, s.employee_id) AS employee_id
FROM Employees e FULL OUTER JOIN
  Salaries s ON e.employee_id = s.employee_id
WHERE s.salary IS NULL OR
  e.name IS NULL
ORDER BY employee_id ASC;
