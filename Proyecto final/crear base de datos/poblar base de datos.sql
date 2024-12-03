use biblioteca;
INSERT INTO libros (titulo, autor,descripcion)
VALUES
  ('El Señor de los Anillos', 'J.R.R. Tolkien','Libro de fantasia'),
  ('Harry Potter y la Piedra Filosofal', 'J.K. Rowling','Libro de fantasia'),
  ('1984', 'George Orwell','Novela de politica de ficcion distopica'),
  ('Crimen y Castigo', 'Fyodor Dostoevsky','Libro de crimen'),
  ('Orgullo y Prejuicio', 'Jane Austen','Novela de amor ysociedad'),
  ('El Principito', 'Antoine de Saint-Exupéry','Cuento de fantasia'),
  ('Don Quijote de la Mancha', 'Miguel de Cervantes','Satira politica y parodia'),
  ('Moby Dick', 'Herman Melville','Novela de suspenso'),
  ('Hamlet', 'William Shakespeare','Obra de teatro'),
  ('Frankenstein', 'Mary Shelley','Novela de terror y ciencia ficcion');
  
INSERT INTO prestamos (fecha_prestamo, fecha_devolucion, dni_usuario, id_libro)
VALUES
  ('2023-11-20', '2023-11-27', 1, 1),
  ('2023-11-22', '2023-11-30', 2, 2),
  ('2023-11-25', '2023-12-03', 4, 3),
  ('2023-12-01', '2023-12-08', 1, 4),
  ('2023-12-02', '2023-12-10', 3, 5),
  ('2023-12-03', '2023-12-11', 5, 6),
  ('2023-12-04', '2023-12-12', 7, 7),
  ('2023-12-05', '2023-12-13', 5, 8),
  ('2023-12-06', '2023-12-14', 9, 9),
  ('2023-12-07', '2023-12-15', 10, 10);
