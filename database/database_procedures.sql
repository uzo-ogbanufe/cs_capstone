USE CS_Capstone;

-- Procedure to add a user to the database
DROP PROCEDURE IF EXISTS addUser;
DELIMITER //
CREATE PROCEDURE addUser(
    IN new_username VARCHAR(64)
)
BEGIN
    -- Declare an error handler that returns false if an error occurs
    DECLARE EXIT HANDLER FOR SQLEXCEPTION SELECT FALSE;
    
    -- Add the user to the database
    INSERT INTO users (username) VALUES (new_username);
    
    -- Return true on success
    SELECT TRUE;
END //
DELIMITER ;

-- Procedure to add an item to the database
DROP PROCEDURE IF EXISTS addItem;
DELIMITER //
CREATE PROCEDURE addItem(
    IN new_title VARCHAR(64),
    IN new_description VARCHAR(5000),
    IN new_seller_username VARCHAR(64),
    IN new_current_price INT,
    IN new_date_of_listing DATETIME,
    IN new_date_of_closing DATETIME
)
BEGIN
	-- Declare a variable to get the seller ID from the username
    DECLARE new_seller_id VARCHAR(64) DEFAULT -1;
    
    -- Declare an error handler that returns false if an error occurs
    DECLARE EXIT HANDLER FOR SQLEXCEPTION SELECT FALSE;
    
    -- Find the user_id associated with the given username
    SELECT user_id INTO new_seller_id FROM users WHERE username = new_seller_username;
    
    -- Add the item to the database
    INSERT INTO items (item_title, date_of_closing, current_price, item_description, seller_id, date_of_listing) 
    VALUES (new_title, new_date_of_closing, new_current_price, new_description, new_seller_id, new_date_of_listing);
    
    -- Return true on success
    SELECT TRUE;
END //
DELIMITER ;

-- Procedure to find items from a given seller or by title
DROP PROCEDURE IF EXISTS findItems;
DELIMITER //
CREATE PROCEDURE findItems(
    IN search_text VARCHAR(64)
)
BEGIN
	-- Declare a variable to get the seller ID from the username
    DECLARE found_username VARCHAR(64) DEFAULT -1;
    DECLARE found_id VARCHAR(64) DEFAULT -1;

	-- Declare an error handler that returns NULL if an error occurs
    DECLARE EXIT HANDLER FOR SQLEXCEPTION SELECT NULL;
    
    -- Get the desired values from the item table
    SELECT items.item_title, users.username, items.current_price, items.date_of_closing
    FROM items INNER JOIN users ON items.seller_id = users.user_id
    WHERE (item_title LIKE concat("%", search_text, "%"))
    OR (item_description LIKE concat("%", search_text, "%"))
    OR (username LIKE concat("%", search_text, "%"));
END //
DELIMITER ;


