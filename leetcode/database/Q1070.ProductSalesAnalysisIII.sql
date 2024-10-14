WITH Min_year_product AS (
    SELECT product_id, MIN(year) AS year
    FROM Sales
    GROUP BY product_id
)

SELECT s.product_id, m.year AS "first_year", s.quantity, s.price
FROM Sales s JOIN
  Min_year_product m ON (s.year = m.year AND s.product_id = m.product_id);
