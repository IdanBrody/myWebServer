-- Create a stored procedure to create the database if it doesn't exist
DELIMITER //
CREATE PROCEDURE IF_NOT_EXISTS_CREATE_DB()
BEGIN
    DECLARE db_count INT;
    SELECT COUNT(*) INTO db_count FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'shoe_store';
    IF db_count = 0 THEN
        CREATE DATABASE shoe_store;
    END IF;
END //
DELIMITER ;

-- Call the stored procedure to create the database if needed
CALL IF_NOT_EXISTS_CREATE_DB();

-- Use the 'shoe_store' database
USE shoe_store;

-- Create the 'products' table if it doesn't exist
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    product_link VARCHAR(255) NOT NULL,
    vendor VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    gender VARCHAR(10) NOT NULL
);

-- Insert data into the 'products' table if it is empty
INSERT IGNORE INTO products (product_name, product_link, vendor, category, price, gender)
VALUES
    ('Air force 1', 'https://m.media-amazon.com/images/I/81uiWMk9dnL._AC_UX575_.jpg', 'Nike', 'Sneakers', 80, 'Male'),
    ('killshot 2', 'https://m.media-amazon.com/images/I/71bEY0bfGTL._AC_UX575_.jpg', 'Nike', 'Sneakers', 93, 'Male'),
    ('Superstar', 'https://m.media-amazon.com/images/I/61nldK7Iq6L._AC_UX575_.jpg', 'Adidas', 'Sneakers', 99, 'Male'),
    ('Gazelle', 'https://m.media-amazon.com/images/I/61yoU96dTEL._AC_UX575_.jpg', 'Adidas', 'Sneakers', 100, 'Male'),
    ('Superstar', 'https://m.media-amazon.com/images/I/61vMViXZX9L._AC_UX575_.jpg', 'Adidas', 'Sneakers', 99, 'Female'),
    ('Grand Court', 'https://m.media-amazon.com/images/I/71qdoDlEOpL._AC_UX575_.jpg', 'Adidas', 'Sneakers', 70, 'Female'),
    ('Manoa', 'https://m.media-amazon.com/images/I/71jddXtQvQL._AC_UX575_.jpg', 'Nike', 'Boots', 129, 'Male'),
    ('Tanjun', 'https://m.media-amazon.com/images/I/51ATvWJ-V0L._AC_UX575_.jpg', 'Nike', 'Boots', 89, 'Female'),
    ('Air Max', 'https://m.media-amazon.com/images/I/51kYlPPJfOL._AC_UX575_.jpg', 'Nike', 'Sport', 147, 'Male'),
    ('Air Zoom Pegasus', 'https://m.media-amazon.com/images/I/61nAuWkqZjL._AC_UX575_.jpg', 'Nike', 'Sport', 139, 'Female')
    ;

-- Create the 'users' table if it doesn't exist
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL
);

-- Insert data into the 'users' table if it is empty
INSERT IGNORE INTO users (username, password, email, created_at)
VALUES
    ('Idan', '$5$rounds=535000$YI6rCb5EpHSNBCzJ$70ubu9rJpcT12sa03iUW5nPir/suPwl54cx0AnykY8B', 'idanbrody8@gmail.com', '2023-06-23 00:08:15'),
    ('ben', '$5$rounds=535000$3FvUfe6UK.I8x28z$A6FWUCZJmVcWipX5h/O2LrcNqKeqUFUR974f3rLOmLD', 'Bensocho10@gmail.com', '2023-06-23 16:34:18')
    ;



    
