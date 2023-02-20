-- SELECT * FROM students;
-- SELECT * FROM students WHERE id = 2;
-- SELECT * FROM students WHERE last_name LIKE '%Benichou%' AND first_name LIKE '%Marc%';
-- SELECT * FROM students WHERE first_name LIKE '%a%';
-- SELECT * FROM students WHERE first_name LIKE 'A%';
-- SELECT * FROM students WHERE first_name LIKE '%a';
-- SELECT * FROM students WHERE first_name NOT LIKE 'A%';
-- SELECT * FROM students WHERE (id = 1) OR (id = 3);
SELECT * FROM students WHERE birth_date >= '01/01/2000';
