SELECT (
    SELECT salary as SecondHighestSalary
    FROM (
        SELECT salary, RANK() OVER (ORDER BY salary DESC) as rank
        FROM Employee
        GROUP BY salary
    )
    WHERE rank = 2
  ) AS SecondHighestSalary
FROM DUAL;
