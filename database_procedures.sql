USE CS_Capstone;

-- Procedure to add a user to the database
DROP PROCEDURE IF EXISTS add_user;
DELIMITER //
CREATE PROCEDURE add_user(
    IN new_username VARCHAR(64)
)
BEGIN
	-- Check if the user is in the database already
    SELECT IF (NOT EXISTS (SELECT username FROM users where username = new_username ), TRUE, FALSE);
    -- Add the user to the database
    INSERT IGNORE INTO users (username) VALUES (new_username);
END //
DELIMITER ;