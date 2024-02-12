-- Write a SQL script that creates a function SafeDiv that divides
-- (and returns) the first by the second number or returns 0 if
-- the second number is equal to 0.
DELIMITER //
CREATE FUNCTION SafeDiv
RETURNS INT
BEGIN
    DECLARE result INT;

    IF b = 0
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;
END;
//

DELIMITER ;