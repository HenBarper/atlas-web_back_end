-- creates a table users
-- With these attributes: id, email, name
CREATE TABLE IF NOT EXISTS Persons (
    id INT NOT NULL,
    email VARCHAR(255) NOT NULL AUTO_INCREMENT UNIQUE,
    name VARCHAR(255),
);