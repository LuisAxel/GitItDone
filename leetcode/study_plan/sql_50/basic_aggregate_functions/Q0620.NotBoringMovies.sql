select id, movie, description, rating
from Cinema
where mod(id, 2) = 1
  and description != 'boring'
order by 4 desc;
