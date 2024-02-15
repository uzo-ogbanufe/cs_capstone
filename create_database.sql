-- Create and switch to the database
CREATE DATABASE IF NOT EXISTS CS_Capstone;
USE CS_Capstone;

-- Create the users table
CREATE TABLE IF NOT EXISTS users (
	user_id INT PRIMARY KEY,
    username VARCHAR(64) UNIQUE NOT NULL
);

-- Create the items table
CREATE TABLE IF NOT EXISTS items (
	item_id INT PRIMARY KEY,
    seller_id INT NOT NULL,
    highest_bidder_id INT,
    item_title VARCHAR(64) NOT NULL,
    date_of_listing DATETIME NOT NULL,
    date_of_closing DATETIME NOT NULL,
    item_description VARCHAR(5000),
    current_price INT NOT NULL,
    
    -- Add the constraints to the table
    FOREIGN KEY (seller_id) REFERENCES users(user_id),
    FOREIGN KEY (highest_bidder_id) REFERENCES users(user_id)
);