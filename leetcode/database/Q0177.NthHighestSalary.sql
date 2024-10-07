CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */

    SELECT salary INTO result
    FROM (
        SELECT salary, RANK() OVER (ORDER BY salary DESC) AS rank
        FROM Employee
        GROUP BY salary
      )
    WHERE rank = N;

    RETURN result;

END;
