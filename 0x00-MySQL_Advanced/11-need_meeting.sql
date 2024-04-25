-- It creates a view called the need_meeting that the lists all the
-- students that have a score thats under 80 (strict) and then
-- no to last_meeting or to more thann 1 month
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting
AS SELECT name FROM students
WHERE score < 80 AND last_meeting is NULL
OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH);
