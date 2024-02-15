-- Create and switch to the database
CREATE DATABASE IF NOT EXISTS CS_Capstone;
USE CS_Capstone;

-- Create the users table
CREATE TABLE IF NOT EXISTS users (
	user_id int primary key,
    username varchar(64) unique
);

-- Create the items table
CREATE TABLE IF NOT EXISTS items (
	item_id int primary key,
    seller_id int,
    highest_bidder_id int,
    item_title varchar(64),
    date_of_listing datetime,
    date_of_closing datetime,
    item_description varchar(5000),
    current_price int
);