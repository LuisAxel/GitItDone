select c.name
from Customer c
where nvl(c.referee_id,0) != 2;
