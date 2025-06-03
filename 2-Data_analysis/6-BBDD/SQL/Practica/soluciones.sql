-- ejercicio 1

SELECT firstname, lastname from customers where country= 'Brazil'

-- ejercicio 2

select * from employees where title= 'Sales Support Agent'

-- ejercicio 3

SELECT tracks.Name, albums.Title, artists.Name from tracks

inner join albums on tracks.AlbumId = albums.AlbumId
INNER JOIN artists ON  albums.ArtistId = artists.ArtistId

where artists.name = 'AC/DC'

-- ejercicio 4

Select customerid, firstname || ' ' || lastname as nombre, country 
from customers
where NOT country ='USA'

-- ejercicio 5

SELECT firstname || ' ' || lastname as nombre, city || ', ' || state|| ', ' || country AS direccion, email 
from employees where title = 'Sales Support Agent'

-- ejercicio 6

SELECT DISTINCT billingcountry from invoices

-- ejercicio 7

SELECT state, COUNT(customerid) as num_clientes
from customers
where country == 'USA'
GROUP by  state 
order by num_clientes DESC

-- ejercicio 8

SELECT invoiceid, SUM(quantity) as num_productos from invoice_items where invoiceid = 37

-- ejercicio 9

Select COUNT(t.trackid) as count_track
from tracks as t 
inner join albums as a on t.AlbumId = a.AlbumId
inner join artists as art on a.ArtistId = art.ArtistId
where art.Name = 'AC/DC'


-- ejercicio 10

SELECT invoiceid, SUM(quantity) as num_articulos
from invoice_items
group by invoiceid

-- ejercicio 11

SELECT count(invoiceid), billingcountry 
from invoices
group by billingcountry

-- ejercicio 12

SELECT strftime('%Y', invoicedate) as anio, 
COUNT(invoiceid) 
from invoices
where anio  in('2009', '2011')
GROUP by 1


-- ejercicio 13

SELECT strftime('%Y', invoicedate) as anio, 
COUNT(invoiceid) 
from invoices

-- ejercicio 14

select country, count(*) as num_clientes
from customers
where country in ('Spain', 'Brazil')
GROUP by country

-- ejercicio 15

select tracks.Name 
from tracks
where name like 'You%'

--PARTE 2
-- EJERCICIO 1
SELECT invoices.InvoiceId, invoices.InvoiceDate, invoices.BillingCountry, customers.FirstName, customers.LastName
from customers join invoices on customers.CustomerId = invoices.CustomerId
WHERE invoices.billingcountry = 'Brazil'

-- EJERCICIO 2
SELECT invoices.InvoiceId, employees.FirstName, employees.LastName 
from employees
join customers on employees.EmployeeId = customers.SupportRepId
join invoices on customers.CustomerId = invoices.CustomerId
where employees.Title = 'Sales Support Agent'

-- EJERCICIO 3
select customers.FirstName || ' '|| customers.LastName as nombre_cliente, customers.Country, employees.FirstName ||' '||employees.LastName as nombre_empleado, invoices.Total
from customers
join employees on customers.SupportRepId = employees.EmployeeId
join invoices on customers.CustomerId = invoices.CustomerId

-- EJERCICIO 4
select invoice_items.InvoiceId, tracks.name
from invoice_items
join tracks on invoice_items.TrackId = tracks.TrackId

-- EJERCICIO 5
SELECT tracks.Name AS nombre_canción, media_types.Name as formato, albums.Title as Album, genres.Name as genero 
from tracks
join albums on tracks.AlbumId = albums.AlbumId
join media_types on tracks.MediaTypeId = media_types.MediaTypeId
join genres on  tracks.GenreId = genres.GenreId

-- EJERCICIO 6
SELECT playlists.Name, playlist_track.playlistid, count(playlist_track.TrackId)
from playlist_track
join playlists on playlist_track.PlaylistId = playlists.PlaylistId
GROUP by playlists.PlaylistId

-- EJERCICIO 7
SELECT e.firstname || ' ' || e.lastname as nombre_empleado, sum(i.total)
from invoices as i
join customers as c on i.CustomerId = c.CustomerId
join employees as e on c.SupportRepId = e.EmployeeId
group by e.employeeid

-- EJERCICIO 8
SELECT e.firstname ||' '||e.lastname as nombre_empleado, sum(i.Total) as total
from invoices i
join customers c on i.CustomerId = c.CustomerId
join employees e on c.SupportRepId = e.EmployeeId
where strftime('%Y', i.InvoiceDate) = '2009'
GROUP by e.employeeid
ORDER by total DESC 
limit 1

-- EJERCICIO 9

select ar.artistid, ar.Name as nombre, sum(i.Total) as ventas
from invoices i
join invoice_items ii on i.InvoiceId = ii.InvoiceId
join tracks t on ii.TrackId = t.TrackId
join albums a on t.albumid = a.AlbumId
join artists ar on a.ArtistId = ar.ArtistId
GROUP by 1
order by 3 desc

-- y la otra
select artists.name as nombre, SUM(invoice_items.UnitPrice* invoice_items.Quantity) as ventas
from invoice_items
join tracks on invoice_items.TrackId = tracks.TrackId
join albums on tracks.AlbumId = albums.AlbumId
join artists on albums.ArtistId = artists.ArtistId
GROUP by artists.ArtistId
order by ventas DESC limit 3