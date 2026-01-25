-- task1.sql
-- Task 1: Joins on hr.db

-- 1. Вивести first_name, last_name, department_id та department_name для кожного працівника
SELECT 
    e.first_name,
    e.last_name,
    e.department_id,
    d.department_name
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id;

-- 2. Вивести first_name, last_name, department, city, state_province для кожного працівника
SELECT
    e.first_name,
    e.last_name,
    d.department_name,
    l.city,
    l.state_province
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id
JOIN locations l
    ON d.location_id = l.location_id;

-- 3. Вивести first_name, last_name, department_id, department_name для працівників з департаментів 40 або 80
SELECT
    e.first_name,
    e.last_name,
    e.department_id,
    d.department_name
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id
WHERE e.department_id IN (40, 80);

-- 4. Вивести всі департаменти, включно з тими, де немає працівників
SELECT
    d.department_id,
    d.department_name,
    e.employee_id
FROM departments d
LEFT JOIN employees e
    ON d.department_id = e.department_id;

-- 5. Вивести first_name працівників разом з іменем їх менеджера
SELECT
    e.first_name AS employee_first_name,
    m.first_name AS manager_first_name
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.employee_id;

-- 6. Вивести job_title, повне ім'я (first + last name) працівника, та різницю між max salary для цієї посади і salary працівника
SELECT
    j.job_title,
    e.first_name || ' ' || e.last_name AS full_name,
    j.max_salary - e.salary AS salary_difference
FROM employees e
JOIN jobs j
    ON e.job_id = j.job_id;

-- 7. Вивести job_title та середню зарплату працівників
SELECT
    j.job_title,
    ROUND(AVG(e.salary), 2) AS avg_salary
FROM employees e
JOIN jobs j
    ON e.job_id = j.job_id
GROUP BY j.job_title;

-- 8. Вивести повне ім'я (first + last) та salary працівників, які працюють у департаментах, розташованих у London
SELECT
    e.first_name || ' ' || e.last_name AS full_name,
    e.salary
FROM employees e
JOIN departments d
    ON e.department_id = d.department_id
JOIN locations l
    ON d.location_id = l.location_id
WHERE l.city = 'London';

-- 9. Вивести department_name та кількість працівників у кожному департаменті
SELECT
    d.department_name,
    COUNT(e.employee_id) AS num_employees
FROM departments d
LEFT JOIN employees e
    ON d.department_id = e.department_id
GROUP BY d.department_name;
