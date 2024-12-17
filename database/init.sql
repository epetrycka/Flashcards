CREATE TABLE testTableUsers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  lastName VARCHAR(255) NOT NULL
);

INSERT INTO testTableUsers (name, lastName) VALUES ('Marcin', 'Wolder');