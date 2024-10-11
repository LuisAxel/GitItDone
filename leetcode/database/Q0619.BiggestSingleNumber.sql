WITH uk_number AS (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
)

SELECT MAX(num) as num
FROM uk_number;
