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
