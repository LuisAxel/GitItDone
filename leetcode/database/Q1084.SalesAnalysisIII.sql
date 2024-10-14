SELECT p.product_id, p.product_name
FROM Product p JOIN
  Sales s ON (p.product_id = s.product_id)
GROUP BY p.product_id, p.product_name
HAVING MAX(TO_CHAR(s.sale_date, 'YYYY-MM-DD')) <= '2019-03-31' AND
  MIN(TO_CHAR(s.sale_date, 'YYYY-MM-DD')) >= '2019-01-01';
