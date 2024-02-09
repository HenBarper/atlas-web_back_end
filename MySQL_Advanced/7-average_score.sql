-- Write a SQL script that creates a stored procedure
-- ComputeAverageScoreForUser that computes and store
-- the average score for a student. Note: An average
-- score can be a decimal
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE num_corrections INT;
    DECLARE avg_score FLOAT;

    SELECT SUM(score) INTO total_score FROM corrections WHERE user_id = user_id;
    SELECT COUNT(*) INTO num_corrections FROM corrections WHERE user_id = user_id;
    IF num_corrections > 0 THEN
        SET avg_score = total_score / num_corrections;
    ELSE
        SET avg_score = 0;
    END IF;

    UPDATE users SET average_score = avg_score WHERE id = user_id;
END;
//

DELIMITER ;