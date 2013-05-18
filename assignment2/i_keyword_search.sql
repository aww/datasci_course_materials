SELECT max(similarity)
FROM (
  SELECT B.docid, sum(A.count * B.count) as similarity
  FROM (
    SELECT * FROM frequency
    UNION
    SELECT 'q' as docid, 'washington' as term, 1 as count
    UNION
    SELECT 'q' as docid, 'taxes' as term, 1 as count
    UNION
    SELECT 'q' as docid, 'treasury' as term, 1 as count
    ) as A,
    (
    SELECT * FROM frequency
    UNION
    SELECT 'q' as docid, 'washington' as term, 1 as count
    UNION
    SELECT 'q' as docid, 'taxes' as term, 1 as count
    UNION
    SELECT 'q' as docid, 'treasury' as term, 1 as count
    ) as B
  ON A.term = B.term
  WHERE A.docid = 'q'
  GROUP BY A.docid, B.docid
);
