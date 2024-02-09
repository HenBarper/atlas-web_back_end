-- Write a SQL script that creates a trigger that resets
-- the attribute valid_email only when the email has been changed.
DELIMITER //
CREATE TRIGGER reset_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    UPDATE users
    SET valid_email = 0
END;
//

DELIMITER ;