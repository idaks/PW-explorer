SELECT pw, COUNT(x3) FROM rel_3 where x3 == """><""" 
GROUP BY pw ORDER BY COUNT(x3) /*ASC LIMIT 5*/;
SELECT pw, COUNT(x3) FROM rel_3 where x3 == """<""" or x3 ==""">""" 
GROUP BY pw ORDER BY COUNT(x3) /*ASC LIMIT 5*/;
SELECT pw, COUNT(x3) FROM rel_3 
WHERE x3 == """><""" OR x3 ==""">""" OR x3 =="""<""" 
GROUP BY pw ORDER BY COUNT(x3) /*ASC LIMIT 5*/;