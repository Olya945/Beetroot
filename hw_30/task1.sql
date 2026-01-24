CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
);

ALTER TABLE students RENAME TO university_students;
ALTER TABLE university_students ADD COLUMN email TEXT;
INSERT INTO university_students (name, age, email)
VALUES ('Антон', 25, 'anton@example.com');
VALUES ('Марія', 22, 'maria@example.com')