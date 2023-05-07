SELECT ROUND(AVG(g.grade),2), su.title, st.fullname, t.fullname
FROM grades as g
JOIN students as st ON g.student_id = st.id
JOIN subjects as su ON g.subject_id= su.id
JOIN teachers as t ON su.teacher_id = t.id
WHERE st.fullname = "Robert Wu"
AND t.fullname = "Lisa Moody"
GROUP BY su.title;