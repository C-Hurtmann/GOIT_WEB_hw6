SELECT ROUND(AVG(g.grade),2) as average_grade, st.fullname, su.title
FROM grades as g
JOIN subjects as su ON g.subject_id = su.id
JOIN students as st ON g.student_id = st.id
WHERE su.title = "Law"
GROUP BY st.fullname
ORDER BY average_grade DESC
LIMIT 1;