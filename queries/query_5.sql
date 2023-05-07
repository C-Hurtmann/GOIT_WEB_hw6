SELECT su.title, t.fullname
FROM subjects as su
JOIN teachers as t ON su.teacher_id = t.id
WHERE t.fullname = "Michele Harrison";