SELECT DISTINCT su.title, st.fullname, t.fullname
FROM students as st
JOIN grades as g ON st.id = g.student_id
JOIN subjects as su ON g.subject_id = su.id
JOIN teachers as t ON su.teacher_id = t.id
WHERE st.fullname = "Mary Ruiz"
AND t.fullname = "Lisa Moody";