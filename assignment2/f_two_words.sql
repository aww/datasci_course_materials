SELECT count(*)
FROM (
  SELECT docid, count(*)
  FROM frequency
  WHERE term = "transactions" OR term = "world"
  GROUP BY docid
  HAVING count(*) > 1
);
