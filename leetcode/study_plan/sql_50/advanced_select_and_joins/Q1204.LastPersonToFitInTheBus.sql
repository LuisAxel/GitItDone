select q.person_name
from (
      select q1.person_name, sum(q2.weight) as w
      from Queue q1 join
        Queue q2 on q1.turn >= q2.turn
      group by q1.person_name
      order by 2 desc
  ) q
where q.w <= 1000 and rownum = 1;
