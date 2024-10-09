WITH lag_temperatures AS(
    SELECT id, recordDate, temperature,
    LAG(recordDate) OVER(ORDER BY recordDate ASC) AS LagDay,
    LAG(temperature) OVER(ORDER BY recordDate ASC) AS LagTemp
    FROM Weather
  );

SELECT id
FROM lag_temperatures
WHERE recordDate - 1 = LagDay AND
  LagTemp < temperature;
