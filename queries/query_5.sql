SELECT su.title, t.fullname
FROM teachers as t
JOIN subjects as su ON t.subject_id = su.id
WHERE su.title = "Architecture";