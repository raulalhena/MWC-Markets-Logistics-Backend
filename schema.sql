CREATE TABLE centers (
	id integer PRIMARY KEY,
	type VARCHAR ( 50 ) NOT NULL
);

CREATE TABLE orders (

        id integer PRIMARY KEY,
        week integer,
        center_id INTEGER,
        num_orders INTEGER
);