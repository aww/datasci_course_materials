  SELECT sum(A.count * B.count) as similarity
  FROM frequency as A JOIN frequency as B
  ON A.term = B.term
  WHERE A.docid = "10080_txt_crude" AND B.docid = "17035_txt_earn"
  GROUP BY A.docid, B.docid;
