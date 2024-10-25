WITH Distinct_products AS (
  SELECT DISTINCT
    TO_CHAR(sell_date, 'YYYY-MM-DD') AS sell_date,
    product
  FROM Activities
)

SELECT
  sell_date,
  COUNT(*) AS num_sold,
  LISTAGG(ALL product, ',')
    WITHIN GROUP (ORDER BY product) AS products
FROM Distinct_products
GROUP BY sell_date
ORDER BY sell_date;
