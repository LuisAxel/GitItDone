select e.employee_id
from Employees e left outer join
  Employees m on e.manager_id = m.employee_id
where e.salary < 30000 and
  e.manager_id is not null and
  m.employee_id is null
order by 1;
