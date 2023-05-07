SELECT ROUND(AVG(g.grade)), t.fullname
FROM grades as g
JOIN subjects as su ON g.subject_id = su.id
JOIN teachers as t ON su.teacher_id = t.id
WHERE t.fullname = "Caleb Lambert";