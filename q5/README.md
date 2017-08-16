## SQL Programming



``` sql
SELECT *
FROM movies
WHERE GENRE = 'action';
```


``` sql
SELECT DISTINCT c.actor, c.birth_year
FROM movie_cast c
INNER JOIN movies m
ON c.movie = m.title AND c.movie_release_year = m.release_year 
WHERE m.director = 'Wes Anderson';
```


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
