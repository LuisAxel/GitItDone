SELECT user_id, name, mail
FROM Users
WHERE REGEXP_LIKE(mail, '^[A-Za-z][-_.A-Za-z0-9]*@leetcode[.]com$');
