Задание: 1

SELECT model, speed, hd
FROM PC
WHERE price < 500;

Задание: 2

SELECT DISTINCT maker
FROM Product
WHERE type = 'Printer';

Задание: 3

SELECT model, ram, screen
FROM Laptop
WHERE price > 1000;

Задание: 4

SELECT *
FROM Printer
WHERE color = 'y'

Задание: 5

SELECT model, speed, hd
FROM PC
WHERE (cd = '12x' OR cd = '24x') AND price < 600

Задание: 6

SELECT DISTINCT Product.maker, Laptop.speed
FROM Laptop
JOIN Product ON Laptop.model = Product.model
WHERE Laptop.hd >= 10;

Задание: 7

SELECT PC.model, PC.price
FROM Product
JOIN PC ON Product.model = PC.model
WHERE Product.maker = 'B'

UNION
SELECT Laptop.model, Laptop.price
FROM Product
JOIN Laptop ON Product.model = Laptop.model
WHERE Product.maker = 'B'

UNION
SELECT Printer.model, Printer.price
FROM Product
JOIN Printer ON Product.model = Printer.model
WHERE Product.maker = 'B';

Задание: 8

SELECT DISTINCT maker
FROM Product
WHERE type = 'PC'
  AND maker NOT IN (
      SELECT maker
      FROM Product
      WHERE type = 'Laptop'
  );

Задание: 9

SELECT DISTINCT Product.maker
FROM Product
JOIN PC ON Product.model = PC.model
WHERE PC.speed >= 450;

Задание: 10

SELECT model, price
FROM Printer
WHERE price = (
    SELECT MAX(price) FROM Printer
);

Задание: 11

SELECT AVG(speed) AS average_speed
FROM PC;

Задание: 12

SELECT AVG(speed) AS average_speed
FROM Laptop
WHERE price > 1000;

Задание: 13

SELECT AVG(PC.speed) AS average_speed
FROM PC
JOIN Product ON PC.model = Product.model
WHERE Product.maker = 'A' AND Product.type = 'PC';

Задание: 14

SELECT s.class, s.name, c.country
FROM ships s
LEFT JOIN classes c ON s.class = c.class
WHERE c.numGuns >= 10
Задание: 15

SELECT hd
FROM PC
GROUP BY hd
HAVING COUNT(*) >= 2;

Задание:
