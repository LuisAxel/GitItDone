WITH uk_employee_dpt AS (
  SELECT employee_id
  FROM Employee
  GROUP BY employee_id
  HAVING COUNT(*) = 1
)

SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y' OR
  employee_id IN (
    SELECT *
    FROM uk_employee_dpt
  );
