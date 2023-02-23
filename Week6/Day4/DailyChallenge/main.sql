CREATE TABLE product_order(
	product_id SERIAL,
	product_name VARCHAR(80) NOT NULL,
	PRIMARY KEY (product_id)
);

CREATE TABLE items(
	items_id SERIAL,
	items_price DECIMAL NOT NULL,
	fk_product_id INTEGER NOT NULL,
	PRIMARY KEY (items_id),
	CONSTRAINT fk_product_id FOREIGN KEY (product_id) REFERENCES product_order (product_id)
);

CREATE or REPLACE FUNCTION product_order_total (sn VARCHAR(50)) RETURNS DECIMAL AS $sum$
BEGIN
	RETURN(SUM(items_price) FROM items INNER JOIN items ON product_order.id = items.product_order_id
							WHERE product_order.serial_number = sn
);

END;
$sum$ LANGUAGE plpgsql;