SELECT g.grade, st.fullname, gr.title, su.title
FROM grades as g
JOIN students as st ON g.student_id = st.id
JOIN groups as gr ON st.group_id = gr.id
JOIN subjects as su ON g.subject_id = su.id
WHERE gr.title = "Beta"
AND su.title = "Economics";
