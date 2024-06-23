select query_name,
  round(avg(rating / position),2) as quality,
  round(avg(case when rating < 3 then 100 else 0 end), 2) as poor_query_percentage
from Queries
where query_name is not null
group by query_name;
