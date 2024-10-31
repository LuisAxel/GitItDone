SELECT *
FROM Products
UNPIVOT (
  price FOR store IN (
    store1 AS 'store1',
    store2 AS 'store2',
    store3 AS 'store3'
  )
);
