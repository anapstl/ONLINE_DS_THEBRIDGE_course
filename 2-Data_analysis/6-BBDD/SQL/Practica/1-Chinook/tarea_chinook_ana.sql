-- 1. Obtén los clientes de brasil

select *
from customers
where country = 'Brazil'

-- 2. Obtén los empleados que son agentes de ventas

select DISTINCT title
from employees

select *
from employees
WHERE title = 'Sales Support Agent'

-- 3. Obtén las canciones de ‘AC/DC’

select tracks.name, albums.Title, artists.name
from tracks
INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
inner join artists on albums.ArtistId = artists.ArtistId
where artists.Name LIKE '%AC/DC%'

-- 4. Obtén los campos de los clientes que no sean de USA: Nombre completo, ID, País
-- != funciona
-- customerid || ' ' || lastname 

SELECT CONCAT(firstname, ' ' ,lastname) AS FullName, customerid, country
FROM customers
WHERE NOT Country = 'USA'

-- 5. Obtén los empleados que son agentes de ventas: Nombre completo, Dirección
-- (Ciudad, Estado, País) y email

select concat(lastname, ' ', firstname) as FullName, concat(city, ', ', state, ', ', country) as Direction, email
from employees
WHERE LOWER(title) = LOWER('Sales Support Agent')

-- 6. Obtén una lista con los países no repetidos a los que se han emitido facturas
select DISTINCT country
from customers
RIGHT join invoices on customers.CustomerId = invoices.CustomerId

-- 7. Obtén una lista con los estados de USA no repetidos de donde son los clientes y
-- cuántos clientes en cada uno.

SELECT state, count(customerid) as no_customers
from customers
where country='USA'
GROUP by state
ORDER BY no_customers DESC

-- 8. Cuántos artículos tiene la factura 37

select count(*)
from invoice_items
where invoice_items.InvoiceId = 37

-- 9. Cuántas canciones tiene ‘AC/DC’

select COUNT(*)   -- recomendado NO usar * en consultas; hilar mejor 
from tracks
INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
inner join artists on albums.ArtistId = artists.ArtistId
where artists.Name LIKE '%AC/DC%'

-- 10. Cuántos artículos tiene cada factura

select invoiceid, count(*) as NoArticles        -- mejor con SUM ya que acyualmente hay q = 1 x 4, pero si cambiamos la q de una ya no nos valdría
from invoice_items
GROUP by invoiceid

--sum(q)

-- 11. Cuántas facturas hay de cada país

select billingcountry, count(invoiceid)
from invoices
group by billingcountry

-- 12. Cuántas facturas ha habido en 2009 y 2011
select count(invoiceid) AS n_invoices_2009_2011
from invoices
where (invoicedate between '2009-01-01' and '2009-12-31') 
OR (invoicedate between '2011-01-01' and '2011-12-31') 

select strftime('%Y', invoicedate) as anio, count(invoiceid)
from invoices
where anio LIKE '2009' or anio LIKE '2011'
group by anio       -- es equivalente con la pos de la col que es 1

-- 13. Cuántas facturas ha habido entre 2009 y 2011

select count(*)
from invoices
where invoicedate BETWEEN '2009-01-01' and '2011-12-31'
-- where strftime('Y%', InvoiceDate) BETWEEN '2009' and '2011'

-- 14. Cuántas clientes hay de España y de Brasil

select country, count(*) as no_customers_per_country
from customers
where country='Brazil' or country='Spain' -- country IN ('Spain', 'Brazil')
Group by country

-- 15. Obtén las canciones que su título empieza por ‘You’

SELECT *
FROM tracks
where name like 'You%'

-- SEGUNDA PARTE
-- 1. Facturas de Clientes de Brasil, Nombre del cliente, Id de factura, fecha de la
-- factura y el país de la factura

SELECT concat(customers.FirstName, ' ', customers.LastName) as ClientName, invoices.InvoiceId, invoices.InvoiceDate, invoices.BillingCountry
FROM customers
inner join invoices on customers.CustomerId = invoices.CustomerId
where BillingCountry = 'Brazil'

-- 2. Obtén cada factura asociada a cada agente de ventas con su nombre completo

select concat(employees.lastname, ' ', employees.firstname) as FullName, invoices.*
from employees
Inner join customers on employees.EmployeeId = customers.SupportRepId
inner join invoices on customers.CustomerId = invoices.CustomerId
WHERE title = 'Sales Support Agent'   -- podria faltar ya que los que estan relacionados a traves de customer ya son los agentes

-- 3. Obtén el nombre del cliente, el país, el nombre del agente y el total

select concat(customers.LastName, ' ', customers.FirstName) as ClientName, customers.Country, concat(employees.LastName, ' ', employees.FirstName) as AgentName, invoices.Total
from employees
inner join customers on employees.EmployeeId = customers.CustomerId
inner join invoices on customers.CustomerId = invoices.CustomerId

select concat(customers.LastName, ' ', customers.FirstName) as ClientName, customers.Country, concat(employees.LastName, ' ', employees.FirstName) as AgentName, invoices.Total
from customers
join employees on customers.SupportRepId = employees.EmployeeId
join invoices on customers.CustomerId = invoices.CustomerId

-- 4. Obtén cada artículo de la factura con el nombre de la canción

SELECT invoice_items.*, tracks.Name
from invoice_items
inner join tracks on invoice_items.TrackId = tracks.TrackId

-- 5. Muestra todas las canciones con su nombre, formato, álbum y género

select tracks.Name,
        media_types.Name as MediaFormat,
        albums.Title as Album,
        genres.Name as Genre
from tracks
inner join media_types on media_types.MediaTypeId = tracks.MediaTypeId
inner join albums on albums.AlbumId =tracks.AlbumId
inner join genres on genres.GenreId = tracks.GenreId

-- 6. Cuántas canciones hay en cada playlist

select count(trackid), playlist_track.playlistid, pls.Name
from playlists
inner join playlist_track on playlists.PlaylistId = playlist_track.PlaylistId
group by playlist_track.playlistid

-- 7. Cuánto ha vendido cada empleado

select concat(employees.FirstName, ' ', employees.LastName), sum(total) as 'Total'
from employees
INNER join customers on employees.employeeid = customers.supportrepid
INNER join invoices on invoices.customerid = customers.customerid
group by employees.employeeid

-- 8. ¿Quién ha sido el agente de ventas que más ha vendido en 2009?

select *, max(total) from
(select employees.*, sum(total) as 'Total'
from employees
INNER join customers on employees.employeeid = customers.supportrepid
INNER join invoices on invoices.customerid = customers.customerid
where invoices.InvoiceDate BETWEEN '2009-01-01' and '2009-12-31'
group by employees.employeeid)


-- 9. ¿Cuáles son los 3 grupos que más han vendido?
SELECT artists.name, sum(TotalPerAlbum) as Total
FROM
    (select albums.AlbumId, sum(TotalPerTrack) as TotalPerAlbum, albums.ArtistId
    FROM
        (SELECT tracks.trackid, sum(invoice_items.unitprice) as TotalPerTrack, tracks.AlbumId
        from invoice_items
        inner join tracks on tracks.TrackId = invoice_items.TrackId
        group by tracks.trackid) s
    inner join albums ON s.AlbumId = albums.AlbumId
    group by s.AlbumId) q
inner join artists ON artists.ArtistId = q.ArtistId
group by artists.ArtistId
ORDER BY Total DESC
limit 3

