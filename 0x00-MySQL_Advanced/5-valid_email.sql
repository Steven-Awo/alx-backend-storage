-- Task 5: This creates a trigger that helps resets the attribute
-- valid_email only when that the email has already been changed
DELIMITER |
CREATE TRIGGER email_bool BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
    END IF;
END;
|
