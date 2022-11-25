DROP TABLE centers;
DROP TABLE orders;


CREATE TABLE centers (
	center_id integer PRIMARY KEY,
	city_code VARCHAR,
	region_code VARCHAR,
	center_type VARCHAR,
	op_area VARCHAR
);

CREATE TABLE orders (

        id INTEGER PRIMARY KEY,
        week INTEGER,
        center_id INTEGER,
        meal_id INTEGER,
        checkout_price FLOAT,
        base_price FLOAT,
        email_for_promotion BOOLEAN,
        homepage_featured BOOLEAN,
        num_orders INTEGER
);