DELETE FROM Person
WHERE id IN (
    SELECT d.id
    FROM Person o JOIN
      Person d ON (o.email = d.email AND o.id < d.id)
  );
