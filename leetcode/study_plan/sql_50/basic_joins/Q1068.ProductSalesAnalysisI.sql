select p.product_name, s.year, s.price
from sales s, product p
where p.product_id = s.product_id;
