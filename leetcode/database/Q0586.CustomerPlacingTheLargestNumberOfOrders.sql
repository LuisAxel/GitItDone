WITH num_orders AS (
    SELECT customer_number, COUNT(customer_number) AS num_orders
    FROM Orders
    GROUP BY customer_number
    ORDER BY num_orders DESC
);

SELECT customer_number
FROM num_orders
WHERE ROWNUM = 1;
