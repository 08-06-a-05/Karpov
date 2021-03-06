UPDATE cars
	SET year = substr(year,1,4)
--Год до применения команды выше был указан в формате YYYY-MM-DD, но т.к. для автомобиля в основном важен год, то он был преобразован в формат YYYY
SELECT name_of_customer, MAX(id_order) AS 'last_user' FROM orders
SELECT year FROM cars GROUP BY year
SELECT COUNT(*) as 'cars_total' FROM cars
SELECT avg(year) from cars where year>=substr(CURRENT_DATE,1,4)-'1'