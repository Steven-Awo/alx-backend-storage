-- Task 10: This creates a function called SafeDiv that helps
-- divides (and returns) which is the first by the second number
-- or to return 0 if actually the second number is actually
-- equal to 0
DELIMITER |
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
    DECLARE result FLOAT;
    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;
    RETURN result;
END;
|
