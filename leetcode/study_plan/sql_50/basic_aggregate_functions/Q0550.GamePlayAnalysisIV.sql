select round(sum(
    case when c.event_date is null then 0 else 1 end
    ) / count(*), 2) as fraction
from (
    select player_id, min(event_date) as first_login
    from Activity
    group by player_id
  ) f left outer join
  Activity c on
  f.player_id = c.player_id and
  f.first_login + 1 = c.event_date;
