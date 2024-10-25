SELECT p.product_name, SUM(o.unit) AS unit
FROM Products p JOIN
  Orders o ON (p.product_id = o.product_id)
WHERE TO_CHAR(o.order_date, 'YYYY-MM') = '2020-02'
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100;
