USE CS_Capstone;

-- Add test data to the user table
INSERT INTO users (username) VALUES
	('Alice'), 
    ('Bob'),
    ('Catherine'),
    ('Daniel');
    
-- Add test data into the items table
INSERT INTO items (seller_id, highest_bidder_id, item_title, date_of_listing, date_of_closing, item_description, current_price) VALUES
	(1, NULL, 'Shoes', '2020-01-01 00:00:00', '2020-02-01 00:00:00', 'A pair of running shoes', 3000),
    (1, 3, 'Shirt', '2020-01-01 00:00:00', '2020-02-01 00:00:00', 'A vintage T-Shirt', 4000),
    (2, 4, 'Pants', '2020-01-01 00:00:00', '2020-02-01 00:00:00', 'A pair of used jeans', 6000),
    (4, NULL, 'Socks', '2020-01-01 00:00:00', '2020-02-01 00:00:00', '10 pairs of pink socks', 1500);
    
select * FROM items;