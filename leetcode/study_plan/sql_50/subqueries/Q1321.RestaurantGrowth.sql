select to_char(week.day2, 'YYYY-MM-DD') as visited_on,
  sum(amount) as amount,
  round(sum(amount) / 7, 2) as average_amount
from (
    select distinct d1.visited_on as day1, d2.visited_on as day2
    from Customer d1 join
      Customer d2 on d1.visited_on = d2.visited_on - 6
  ) week join
    Customer c on c.visited_on between week.day1 and week.day2
group by week.day1, week.day2
order by 1;
