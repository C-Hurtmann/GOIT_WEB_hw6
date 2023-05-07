SELECT COUNT(g.grade) as grades_qty, su.title, st.fullname
FROM grades as g
JOIN subjects as su ON g.subject_id = su.id
JOIN students as st ON g.student_id = st.id
WHERE st.fullname = "Mary Foster"
GROUP BY su.title
ORDER BY grades_qty DESC;