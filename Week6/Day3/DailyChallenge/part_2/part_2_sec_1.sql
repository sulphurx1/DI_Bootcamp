CREATE TABLE book (
	book_id SERIAL PRIMARY KEY,
	title CHARACTER VARYING (200) NOT NULL,
	author CHARACTER VARYING (200) NOT NULL
)