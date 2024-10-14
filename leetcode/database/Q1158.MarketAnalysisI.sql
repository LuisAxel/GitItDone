SELECT u.user_id AS buyer_id, TO_CHAR(u.join_date, 'YYYY-MM-DD') AS join_date, COUNT(o.order_id) AS "orders_in_2019"
FROM Users u LEFT JOIN
  Orders o ON (o.buyer_id = u.user_id AND TO_CHAR(o.order_date, 'YYYY') = '2019')
GROUP BY u.user_id, u.join_date;
