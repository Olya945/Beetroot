-- 1. Вивести імена працівників (first_name, last_name)
-- з псевдонімами "First Name" та "Last Name"
SELECT
    first_name AS "First Name",
    last_name AS "Last Name"
FROM employees;

-- 2. Отримати унікальні ID відділів з таблиці employees
SELECT DISTINCT
    department_id
FROM employees;

-- 3. Отримати всі дані про працівників,
-- відсортувавши за іменем у спадному порядку
SELECT *
FROM employees
ORDER BY first_name DESC;

-- 4. Вивести імена, зарплату та PERCENT усіх працівників
-- PERCENT розраховується як 12% від зарплати
SELECT
    first_name,
    last_name,
    salary,
    salary * 0.12 AS PERCENT
FROM employees;

-- 5. Отримати максимальну та мінімальну зарплату
-- з таблиці employees
SELECT
    MAX(salary) AS max_salary,
    MIN(salary) AS min_salary
FROM employees;

-- 6. Вивести місячну зарплату кожного працівника,
-- округлену до 2 знаків після коми
SELECT
    first_name,
    last_name,
    ROUND(salary / 12.0, 2) AS monthly_salary
FROM employees;
