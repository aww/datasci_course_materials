SELECT value
FROM (
  SELECT A.row_num as row_num,
         B.col_num as col_num,
         A.col_num as ind,
         sum(A.value * B.value) as value
  FROM A, B
  WHERE A.col_num == B.row_num
  GROUP BY row_num, col_num
)
WHERE row_num = 2 AND col_num = 3;
