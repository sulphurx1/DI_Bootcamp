CREATE TABLE customer_profile(
	id INTEGER NOT NULL,
	isLoggedIn BOOLEAN NOT NULL DEFAULT FALSE,
	PRIMARY KEY(id),
	CONSTRAINT customer_id FOREIGN KEY (id) REFERENCES customer (id)
);

CREATE TABLE customer(
	id SERIAL PRIMARY KEY,
	first_name CHARACTER VARYING (100),
	last_name CHARACTER VARYING (100) NOT NULL
);