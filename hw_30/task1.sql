CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
);

ALTER TABLE students RENAME TO university_students;

ALTER TABLE university_students ADD COLUMN email TEXT;

INSERT INTO university_students (name, age, email)
VALUES ('Антон', 25, 'anton@example.com');

INSERT INTO university_students (name, age, email)
VALUES ('Марія', 22, 'maria@example.com');

INSERT INTO university_students (name, age, email)
VALUES ('Іван', 23, 'ivan@example.com');

INSERT INTO university_students (name, age)
VALUES ('Оля', 38);

UPDATE university_students
SET age = 23
WHERE name = 'Марія';

UPDATE university_students
SET email = 'olya@example.com'
WHERE name = 'Оля';

DELETE FROM university_students
WHERE name = 'Марія';

DELETE FROM university_students
WHERE name = 'Іван';

SELECT * FROM university_students;
