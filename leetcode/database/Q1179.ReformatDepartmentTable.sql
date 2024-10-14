SELECT *
FROM Department
PIVOT(
  SUM(revenue) Revenue FOR month IN (
    'Jan' Jan, 'Feb' Feb, 'Mar' Mar, 'Apr' Apr, 'Jun' Jun, 'May' May,
    'Jul' Jul, 'Aug' Aug, 'Sep' Sep, 'Oct' Oct, 'Nov' Nov, 'Dec' Dec)
);
