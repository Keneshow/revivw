# 5     Создай ENUM gender_enum со значениями: 'male', 'female', 'other'

CREATE TYPE gender_enum AS ENUM('male', 'female', 'other');

# 1     Создай таблицу students

CREATE TABLE students(
	"id" SERIAL PRIMARY KEY,
	"full_name" VARCHAR(100) NOT NULL,
	"age" INT CHECK (age > 5 AND age < 100),
	"email" VARCHAR(255) UNIQUE,
	"grade" NUMERIC(4,1) DEFAULT 4.5,
	"is_active" BOOLEAN DEFAULT TRUE,
	"enrolled_at" DATE DEFAULT CURRENT_DATE
);

DROP TABLE students;

# 2     Добавь колонку parent_contact типа TEXT

ALTER TABLE students ADD COLUMN parent_contact TEXT;

# 3     Переименуй grade в average_grade

ALTER TABLE students RENAME COLUMN grade TO average_grade;

# 4     Удали колонку parent_contact

ALTER TABLE students DROP COLUMN parent_contact;

# 6     Добавь в таблицу students колонку gender с типом gender_enum

ALTER TABLE students ADD COLUMN gender gender_enum DEFAULT 'male';

# 7     Добавь UUID-колонку student_uuid с автоматическим значением по умолчанию

ALTER TABLE students ADD COLUMN student_uuid UUID DEFAULT gen_random_uuid();