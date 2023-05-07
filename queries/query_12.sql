SELECT g.grade, st.fullname, gr.title, su.title, g.on_date
FROM grades as g
JOIN subjects as su ON g.subject_id = su.id
JOIN students as st ON g.student_id = st.id
JOIN groups as gr ON st.group_id = gr.id
WHERE gr.title = "Gamma"
AND su.title = "Computer Science"
AND g.on_date = (SELECT MAX(g.on_date) FROM grades as g);