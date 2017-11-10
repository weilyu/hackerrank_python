SELECT SUM(population)
FROM city ci INNER JOIN country co 
ON ci.countrycode = co.countrycode
WHERE co.continent = 'Asia'