select f.product_id, f.first_year, s.quantity, s.price
from (
    select product_id, min(year) as first_year
    from Sales s
    group by product_id
  ) f join Sales s on
    s.product_id = f.product_id and
    s.year = f.first_year;
