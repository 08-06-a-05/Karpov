UPDATE cars
	SET year = substr(year,1,5)
SELECT name_of_customer, MAX(id_order) AS 'last_user' FROM orders
SELECT year FROM cars GROUP BY year
SELECT id_car, COUNT(*) as 'cars_total' FROM cars