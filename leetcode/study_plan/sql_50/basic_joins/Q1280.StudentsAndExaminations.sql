select s.student_id, s.student_name,
  sb.subject_name, count(e.subject_name) as attended_exams
from Students s cross join
  Subjects sb left outer join
  Examinations e on
    s.student_id = e.student_id and
    sb.subject_name = e.subject_name
group by (s.student_id, s.student_name, sb.subject_name)
order by 1, 3;
