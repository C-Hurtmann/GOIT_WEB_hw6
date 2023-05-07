SELECT ROUND(AVG(g.grade)), su.title, t.fullname
FROM grades as g
JOIN subjects as su ON g.subject_id = su.id
JOIN teachers as t ON su.teacher_id = t.id
WHERE t.fullname = "Patrick Garrison"
GROUP BY su.title;