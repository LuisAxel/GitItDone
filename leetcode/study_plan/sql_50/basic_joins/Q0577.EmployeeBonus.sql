select e.name, b.bonus
from Employee e, Bonus b
where e.empId = b.empId(+)
  and (b.bonus is null or b.bonus < 1000);
