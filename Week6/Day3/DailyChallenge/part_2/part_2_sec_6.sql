INSERT INTO library(student_id, book_id)
VALUES
	((SELECT student_id FROM student WHERE first_name = 'John'),
	 (SELECT book_id FROM book WHERE title = 'Alice In Wonderland', date = '15/02/2022')),
	 
	 ((SELECT student_id FROM student WHERE first_name = 'Bob'),
	 (SELECT book_id FROM book WHERE title = 'To kill a mockingbird', date = '03/03/2021')),
	 
	 ((SELECT student_id FROM student WHERE first_name = 'Lera'),
	 (SELECT book_id FROM book WHERE title = 'Alice In Wonderland', date = '23/05/2021')),
	 
	 ((SELECT student_id FROM student WHERE first_name = 'Bob'),
	 (SELECT book_id FROM book WHERE title = 'Harry Potter', date = '12/08/2021'));