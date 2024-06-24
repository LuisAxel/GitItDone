select round(avg(
  case when f.order_date = d.customer_pref_delivery_date then 100 else 0 end
  ), 2) as immediate_percentage
from Delivery d join (
    select min(order_date) as order_date, customer_id
    from Delivery
    group by customer_id
  ) f on
  d.customer_id = f.customer_id and
  d.order_date = f.order_date;
