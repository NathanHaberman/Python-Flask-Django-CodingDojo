#1
-- SELECT customer.first_name, customer.last_name, customer.email, address.address
-- FROM customer
-- JOIN address ON customer.address_id = address.address_id
-- WHERE address.city_id = 312

#2
-- SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS 'category'
-- FROM film
-- JOIN film_category on film.film_id = film_category.film_id
-- JOIN category on film_category.category_id = category.category_id
-- WHERE category.category_id = 5

#3
-- SELECT actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year
-- FROM film
-- JOIN film_actor ON film.film_id = film_actor.film_id
-- JOIN actor ON film_actor.actor_id = actor.actor_id
-- WHERE actor.actor_id = 5

#4
-- SELECT customer.first_name, customer.last_name, customer.email, address.address
-- FROM customer
-- JOIN address ON customer.address_id = address.address_id
-- WHERE address.city_id = 1 OR 42 OR 312 OR 459 AND customer.store_id = 1

#5
-- SELECT film.title, film.description, film.release_year, film.rating, film.special_features
-- FROM film
-- JOIN film_actor ON film_actor.film_id = film.film_id
-- JOIN actor ON actor.actor_id = film_actor.actor_id
-- WHERE film.rating = 'G' AND actor.actor_id = 15 AND film.special_features LIKE '%Behind the Scenes'

#6
-- SELECT film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name
-- FROM film
-- JOIN film_actor ON film.film_id = film_actor.film_id
-- JOIN actor ON film_actor.actor_id = actor.actor_id
-- WHERE film.film_id = 369

#7
-- SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS 'category'
-- FROM film
-- JOIN film_category ON film_category.film_id = film.film_id
-- JOIN category ON category.category_id = film_category.category_id
-- WHERE film.rental_rate = 2.99 AND category.category_id = 7

#8
-- SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS 'category', actor.first_name, actor.last_name
-- FROM film
-- JOIN film_category ON film_category.film_id = film.film_id
-- JOIN category ON category.category_id = film_category.category_id
-- JOIN film_actor ON film_actor.film_id = film.film_id
-- JOIN actor ON actor.actor_id = film_actor.actor_id
-- WHERE actor.first_name = 'SANDRA' AND actor.last_name = 'KILMER' AND category.category_id = 1
