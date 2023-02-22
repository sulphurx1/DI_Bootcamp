CREATE TABLE book_student AS library (
	book_fk_id ON DELETE CASCADE ON UPDATE CASCADE,
	student_id ON DELETE CASCADE ON UPDATE CASCADE,
	borrowed_date DATE NOT NULL,
	PRIMARY KEY(book_fk_id, student_id)
	FOREIGN KEY (book_fk_id) REFERENCES book(book_id) FROM book,
	FOREIGN KEY (student_fk_id) REFERENCES student(student_id) FROM student
	
)