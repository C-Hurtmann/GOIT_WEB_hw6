SELECT st.fullname, gr.title
FROM students as st
JOIN groups as gr ON st.group_id = gr.id
WHERE gr.title = "Alpha"