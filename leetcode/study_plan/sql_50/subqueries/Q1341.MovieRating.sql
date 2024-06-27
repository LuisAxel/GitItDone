select q.name as results
from (
    select u.name, count(*)
    from MovieRating mr join
      Users u on
      u.user_id = mr.user_id
    group by u.name
    order by 2 desc, 1 asc
  ) q
where rownum = 1
union all
select q.title as results
from (
    select m.title, avg(mr.rating)
    from MovieRating mr join
    Movies m on
        mr.movie_id = m.movie_id
    where to_char(mr.created_at, 'YYYY-MM') = '2020-02'
    group by m.title
    order by 2 desc, 1 asc
  ) q
where rownum = 1;
