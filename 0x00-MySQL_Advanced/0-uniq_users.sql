-- Task 0 - creating a table users with id, email and name attribute
-- the script can actually be executed on any type of database
CREATE TABLE If NOT EXISTS `users` (  
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255)
);
