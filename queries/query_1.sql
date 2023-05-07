SELECT ROUND(AVG(g.grade),2) as average_grade, st.fullname
FROM grades as g
JOIN students as st ON g.student_id = st.id
GROUP BY st.fullname
ORDER BY average_grade DESC
LIMIT 5;