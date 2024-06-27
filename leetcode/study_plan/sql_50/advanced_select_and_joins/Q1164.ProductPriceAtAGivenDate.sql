select p.product_id, p.new_price as price
from Products p join (
    select product_id, max(change_date) as change_date
    from Products
    where change_date <= '2019-08-16'
    group by product_id
  ) p2 on
    p.product_id = p2.product_id and
    p.change_date = p2.change_date
union
select product_id, 10 as price
from (
    select product_id
    from Products
    group by product_id
    having min(change_date) > '2019-08-16'
  )
