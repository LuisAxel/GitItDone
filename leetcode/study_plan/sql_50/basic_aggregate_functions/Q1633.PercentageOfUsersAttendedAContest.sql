select r.contest_id,
  round(count(*) * 100 / (
    select count(*)
    from Users u)
  , 2) as percentage
from Register r
group by r.contest_id
order by 2 desc, 1 asc;
