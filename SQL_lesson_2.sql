
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    email VARCHAR(100),
    age INTEGER,
    created_at TIMESTAMP
);

CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    salary INTEGER,
    is_active BOOLEAN
);

CREATE TABLE applications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    job_id INTEGER REFERENCES jobs(id),
    status VARCHAR(20),
    applied_at TIMESTAMP
);

-- Вставка данных
INSERT INTO users (id, full_name, email, age, created_at)
VALUES
(1, 'Ivan Petrov', 'ivan@mail.com', 30, NOW()),
(2, 'Anna Vlasova', 'anna@mail.com', 27, NOW()),
(3, 'Tim Cook', 'tim@apple.com', 50, NOW());

INSERT INTO jobs (id, title, salary, is_active)
VALUES
(1, 'Developer', 150000, true),
(2, 'Designer', 120000, false),
(3, 'QA', 110000, true);

INSERT INTO applications (id, user_id, job_id, status, applied_at)
VALUES
(1, 1, 1, 'submitted', NOW()),
(2, 1, 3, 'draft', NOW()),
(3, 2, 1, 'rejected', NOW());

1. Добавить нового пользователя Nikita Belov:

INSERT INTO users(id, full_name, email, age, created_at)
VALUES
(4, 'Nikita Belov', 'belov@site.com', 24, NOW());

2. Добавить 5 новых вакансий с разными названиями и зарплатами:

INSERT INTO jobs (id, title, salary, is_active)
VALUES
(4, 'Project Manager', 130000, true),
(5, 'Business Analyst', 125000, true),
(6, 'System Administrator', 115000, false),
(7, 'DevOps Engineer', 140000, true),
(8, 'Technical Writer', 90000, false);


3. Добавить заявку от пользователя с id=2 на вакансию с id=1 со статусом 'submitted':

INSERT INTO applications (id, user_id, job_id, status, applied_at)
VALUES (4, 2, 1, 'submitted', NOW());


4. Массовая вставка 3 пользователей сразу (выдуманные данные):

INSERT INTO users (id, full_name, email, age, created_at)
VALUES
(5, 'Olga Smirnova', 'olga@mail.com', 29, NOW()),
(6, 'Maxim Ivanov', 'maxim@mail.com', 35, NOW()),
(7 ,'Elena Petrova', 'elena@mail.com', 31, NOW());


5. Обновить все активные вакансии, увеличив зарплату на 10%:
UPDATE jobs
SET salary = ROUND(salary * 1.1)
WHERE is_active = TRUE;

6. Увеличь возраст всех пользователей старше 30 лет на 1 год.

UPDATE users
SET age = age + 1
WHERE age > 30;

7. Поменяй всем email с @gmail.com на @protonmail.com.

UPDATE users
SET email = REPLACE(email, '@mail.com', '@protonmail.com')
WHERE email LIKE '%@gmail.com';

8. Добавь к фамилии " (уволен)" всем пользователям старше 50 лет.

UPDATE users
SET name = CONCAT(name, ' (уволен)')
WHERE age > 50;

9. Обнули зарплату у всех вакансий, где is_active = false.

 UPDATE jobs
SET salary = 0
WHERE is_active = false;

10. Измени статус на 'archived' у всех заявок, сделанных более 30 дней назад (используй NOW())

UPDATE applications
SET status = 'archived'
WHERE applied_at < NOW() - INTERVAL '30 DAY';

11. Измени статус на 'archived' у всех заявок, сделанных более 30 дней назад (используй NOW())

ALTER TABLE users
ADD COLUMN status_level VARCHAR(10);

UPDATE users
SET status_level = CASE
    WHEN age < 25 THEN 'junior'
    WHEN age BETWEEN 25 AND 35 THEN 'middle'
    WHEN age > 35 THEN 'senior'
END;

12. Удалить всех пользователей младше 18 лет

DELETE FROM users
WHERE age < 18;

13. Удалить заявки, у которых статус 'draft'.

DELETE FROM applications
WHERE status = 'draft';

14. Удалить вакансии, у которых нет откликов
(используй WHERE id NOT IN (SELECT job_id FROM applications)).


DELETE FROM jobs
WHERE id NOT IN (
  SELECT DISTINCT job_id FROM applications
);

15. Удалить пользователей, у которых email заканчивается на .com.

DELETE FROM users
WHERE email LIKE '%.com';
