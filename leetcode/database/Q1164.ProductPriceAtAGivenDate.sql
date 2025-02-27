WITH Change_before_date AS (
    SELECT product_id, MAX(change_date) AS last_change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)

SELECT product_id, new_price AS price
FROM Products
WHERE (product_id, change_date) IN (
    SELECT product_id, last_change_date
    FROM Change_before_date
  )
UNION ALL
SELECT product_id, 10 AS price
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16';
