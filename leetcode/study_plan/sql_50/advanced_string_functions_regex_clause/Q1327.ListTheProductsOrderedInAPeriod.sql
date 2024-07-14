select p.product_name, sum(unit) as unit
from Products p join
  Orders o on (p.product_id = o.product_id)
where to_char(o.order_date, 'YYYY-MM') = '2020-02'
group by p.product_name
having sum(unit) >= 100;
