SELECT user_id,
  UPPER(substr(name,1,1)) || LOWER(substr(name,2)) AS name
FROM Users
ORDER BY user_id ASC;
