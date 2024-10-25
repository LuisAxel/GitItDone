WITH
  DailyIncome AS (
    SELECT
      TO_CHAR(visited_on, 'YYYY-MM-DD') AS visited_on,
      SUM(AMOUNT) AS amount
    FROM Customer
    GROUP BY visited_on
  ),
  Result AS (
    SELECT
      ROW_NUMBER() OVER (ORDER BY visited_on) AS row_num,
      visited_on,
      SUM(amount) OVER(ORDER BY visited_on ASC ROWS 6 PRECEDING) AS amount,
      ROUND(SUM(amount) OVER(ORDER BY visited_on ASC ROWS 6 PRECEDING) / 7, 2) AS average_amount
    FROM DailyIncome
)

SELECT visited_on, amount, average_amount
FROM Result
WHERE row_num > 6;
