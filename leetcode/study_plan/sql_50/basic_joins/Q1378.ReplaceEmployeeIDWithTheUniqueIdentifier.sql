select e2.unique_id, e1.name
from EmployeeUNI e2, Employees e1
where e2.id(+) = e1.id;
