create database biblioteca;
use Biblioteca;
CREATE TABLE usuarios (
    dni_usuario INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    fecha_inscripcion DATE NOT NULL
);

CREATE TABLE libros (
    id_libro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100),
    autor VARCHAR(50)
);

CREATE TABLE prestamos (
    id_prestamo INT PRIMARY KEY AUTO_INCREMENT,
    fecha_prestamo DATE,
    fecha_devolucion DATE,
    dni_usuario INT,
    id_libro INT,
    FOREIGN KEY (dni_usuario) REFERENCES usuarios(dni_usuario),
    FOREIGN KEY (id_libro) REFERENCES libros(id_libro)
);

CREATE TABLE pagos (
    id_pago INT PRIMARY KEY AUTO_INCREMENT,
    fecha_pago DATE,
    monto DECIMAL(10,2),
    dni_usuario INT,
    FOREIGN KEY (dni_usuario) REFERENCES usuarios(dni_usuario)
);