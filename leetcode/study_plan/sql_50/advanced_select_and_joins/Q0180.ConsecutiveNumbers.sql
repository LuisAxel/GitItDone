select distinct l1.num as consecutiveNums
from Logs l1 join
  Logs l2 on
    l1.id = l2.id - 1 and l1.num = l2.num join
  Logs l3 on
    l1.id = l3.id - 2 and l1.num = l3.num;
