select d.name as Department, e.name as Employee, e.salary as Salary
from Department d join
  Employee e on (d.id = e.departmentId)
where 3 > (
    select count(distinct aux.salary)
    from Employee aux
    where aux.salary > e.salary and
      e.departmentId = aux.departmentId
  );
