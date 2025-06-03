Select titulo, nombre, nacionalidad
From libro
join autor on libro.id_autor = autor.id_autor
where nombre like '%Gabriel%'

Select *
From libro
where titulo LIKE '%Cien%'