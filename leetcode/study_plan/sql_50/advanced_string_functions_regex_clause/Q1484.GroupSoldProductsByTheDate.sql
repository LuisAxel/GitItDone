select to_char(sell_date, 'YYYY-MM-DD') as sell_date,
  count(product) as num_sold,
  LISTAGG(product, ',') within group(order by product) as products
from (
    Select distinct *
    from Activities
  )
group by sell_date
order by 1;
