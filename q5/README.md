## SQL Programming

##### 1. List the title, release year, genre and director of all 'action' movies.

``` sql
SELECT *
FROM movies
WHERE genre = 'action';
```

##### 2. List the actors and their birth year for all movies directed by 'Wes Anderson'

``` sql
SELECT DISTINCT c.actor, c.birth_year
FROM movie_cast c
INNER JOIN movies m
ON c.movie = m.title AND c.movie_release_year = m.release_year 
WHERE m.director = 'Wes Anderson';
```

##### 3. List the title, release year, genre and director of all movies staring 'Jeff Goldblum' but not 'Bruce Willis'

``` sql
SELECT m.*
FROM movies m
INNER JOIN movie_cast c
ON c.movie = m.title AND c.movie_release_year = m.release_year
WHERE c.actor = 'Jeff Goldblum'
EXCEPT
SELECT m.*
FROM movies m
INNER JOIN movie_cast c
ON c.movie = m.title AND c.movie_release_year = m.release_year
WHERE c.actor = 'Bruce Willis'
```
