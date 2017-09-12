#1:
-- SELECT countries.name, languages.language, languages.percentage
-- 	FROM countries
--     JOIN languages ON countries.code = languages.country_code 
--     WHERE languages.language = "Slovene"
--     ORDER BY languages.percentage DESC

#2
-- SELECT countries.name, COUNT(cities.name) AS 'number_of_cities'
-- FROM countries
-- JOIN cities ON countries.code = cities.country_code
-- GROUP BY countries.code
-- ORDER BY COUNT(cities.name) DESC

#3
-- SELECT countries.name, cities.name AS 'city_name'
-- FROM countries
-- JOIN cities ON countries.code = cities.country_code
-- WHERE countries.code = 'MEX' AND cities.population > 500000
-- ORDER BY cities.population DESC

#4
-- SELECT countries.name, languages.language, languages.percentage
-- FROM countries
-- JOIN languages ON countries.code = languages.country_code
-- WHERE languages.percentage > 89
-- ORDER BY languages.percentage DESC

#5 
-- SELECT name, surface_area, population
-- FROM countries
-- WHERE surface_area < 501 AND population > 100000

#6
-- SELECT name, government_form, capital, life_expectancy
-- FROM countries
-- WHERE government_form = 'constitutional monarchy' AND capital > 200 AND life_expectancy > 75

#7
-- SELECT countries.name, cities.name, cities.district, cities.population
-- FROM countries
-- JOIN cities ON countries.id = cities.country_id
-- WHERE countries.id = 9 AND cities.district = 'Buenos Aires' and cities.population > 500000

#8
-- SELECT region, COUNT(name) AS 'number of countries'
-- FROM countries
-- GROUP BY region
-- ORDER BY COUNT(name) DESC