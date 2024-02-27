USE CS_Capstone;

-- Procedure to add a user to the database
DROP PROCEDURE IF EXISTS AddUser;
DELIMITER //
CREATE PROCEDURE AddUser(
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
DROP PROCEDURE IF EXISTS AddItem;
DELIMITER //
CREATE PROCEDURE AddItem(
    IN new_title VARCHAR(64),
    IN new_date_of_closing DATETIME,
    IN new_current_price INT,
    IN new_description VARCHAR(5000),
    IN new_seller_id INT,
    IN new_date_of_listing DATETIME
)
BEGIN
	-- Declare an error handler that returns false if an error occurs
    DECLARE EXIT HANDLER FOR SQLEXCEPTION SELECT FALSE;
    
    -- Add the item to the database
    INSERT INTO items (item_title, date_of_closing, current_price, item_description, seller_id, date_of_listing) 
    VALUES (new_title, new_date_of_closing, new_current_price, new_description, new_seller_id, new_date_of_listing);
    
    -- Return true on success
    SELECT TRUE;
END //
DELIMITER ;
