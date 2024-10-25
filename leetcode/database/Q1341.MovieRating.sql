WITH
  Most_rating_user AS (
    SELECT u.name AS results
    FROM Users u JOIN
      MovieRating mr ON (u.user_id = mr.user_id)
    GROUP BY u.name
    ORDER BY COUNT(*) DESC, u.name ASC
  ),
  Most_rated_movie AS (
    SELECT m.title AS results
    FROM Movies m JOIN
      MovieRating mr ON (m.movie_id = mr.movie_id)
    WHERE TO_CHAR(mr.created_at, 'YYYY-MM') = '2020-02'
    GROUP BY m.title
    ORDER BY AVG(mr.rating) DESC, m.title ASC
  )

SELECT results
FROM Most_rating_user
WHERE ROWNUM = 1
UNION ALL
SELECT results
FROM Most_rated_movie
WHERE ROWNUM = 1;
