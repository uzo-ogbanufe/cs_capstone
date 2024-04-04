USE CS_Capstone;

-- Add test data to the user table
call addUser('Alice');
call addUser('Bob');
call addUser('Catherine');
call addUser('Daniel');
    
-- Add test data into the items table
call addItem('Hat', 'A baseball cap', 'Bob', 1250, CURRENT_TIMESTAMP(), '2025-01-03 06:50:20');
call addItem('Shirt', 'A vintage t-shirt', 'Catherine', 1999, CURRENT_TIMESTAMP(), '2024-07-11 16:20:00');
call addItem('Pants', NULL, 'Alice', 3000, CURRENT_TIMESTAMP(), '2025-01-03 00:00:00');
call addItem('Shoes', 'A pair of running shoes', 'Daniel', 1500, CURRENT_TIMESTAMP(), '2026-12-25 04:50:20');