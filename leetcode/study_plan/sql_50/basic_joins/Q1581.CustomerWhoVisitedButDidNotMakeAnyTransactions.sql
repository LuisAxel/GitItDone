select v.customer_id, count(*) as count_no_trans
from Visits v, Transactions t
where v.visit_id = t.visit_id(+)
  and t.visit_id is null
group by v.customer_id;