**Biblioteca**

**Esquema: DB**

`BIBLIOTECA<usuario,libro,prestamo,pago>`

### Paso 1: Determinar las Dependencias Funcionales (DFs)
A partir del enunciado se puede deducir llas siguientes dependdencias funcionales.

1. **idUsuario -> nombreUsuario,apellidoUsuario**: Del usuario se necesitan los datos `nombre` y `apellido`, que dependeran funcionalmente de `idUsuario`.
2. **idLibro -> nombreLibro,autor,descripcion,categoria**: De los libros se necesitan los datos `nombre`,`autor`,`descripcion` y `categoria`, que dependeran funcionalmente de `idLibro`.
3. **idPrestamo -> usuario,libro,fechaPrestamo,fechaDevolucion**: El prestamo debe registrar al usuario que pide el prestamo y al libro que se presta, tambien debe registrar la fecha del prestamo y la devolucion para el calculo de la multa por lo tanto los atributos `usuario`,`libro`,`fechaPrestamo`,`fechaDevolucion` dependen de `idPrestamo`.
4. **idPago,usuario -> monto,mesPago**: Se necesita registrar los pagos de las cuotas mensuales de cada usuario, por lo que los atributos `montoPago` y `mesPago` dependen de `idPago` y `usuario`.
5. **idUsuario -> multa** Se debe calcular la multa a partir de un prestamo de un usuario, por lo que el atributo `multa` es funcionalmente dependiente de `idUsuario`.

### Paso 2: Determinar claves candidatas
Para determinar las **claves candidatas**, necesitamos encontrar un conjunto de atributos que puedan identificar de manera única a cada fila de las tablas `Libro`,`Usuario`,`Pagos` y `Prestamo`.

En este caso, podemos ver que:
- La combinacion de las claves `dniUsuario`,`idLibro`,`idPrestamo`,`idPago` es suficiente para identificar de forma unica cada registro de cada tabla:
  - `dniUsuario` identifica de manera unica a cada usuario.
  - `idPrestamo` identifica de manera unica cada prestamo y la combinacion entre `dniUsuario` y `idPrestamo` identifica cada prestamo tomado por un usuario.
  - `idPago` identifica de manera unica cada pago y la combinacion entre `dniUsuario` y `idPago` identifica cada pago hecho por un usuario.
  - `idLibro` identifica de manera unica a cada libro existente en la biblioteca.

Por lo tanto, la **clave candidata** es:
- (`dniUsuario`,`idLibro`,`idPago`,`idPrestamo`)
  
Esta combinación asegura que cada registro en la tabla sea único y no haya duplicados.


### Paso 3: Diseño de la tercera forma normal (3FN)

Se dividió la tabla original en cuatro tablas (`Usuario`, `Libro`, `Prestamo`, `Pago`) para eliminar dependencias transitivas y garantizar que cada atributo no clave dependa únicamente de la clave primaria completa.

1. **Tabla `Usuario`**
   - `dniUsuario` (clave primaria)
   - `nombre`
   - `apellido`

2. **Tabla `Libro`**
   - `idLibro` (clave primaria)
   - `nombre`
   - `autor`
   - `descripcion`

3. **Tabla `Prestamo`**
   - `idPrestamo` (clave primaria)
   - `dniUsuario` (clave foranea que referencia a Usuario)
   - `idLibro` (clave foranea que referencia a Libro)
   - `fechaPrestamo`
   - `fechaDevolucion`

4. **Tabla `Pago`**
    - `idPago` (clave primaria)
    - `dniUsuario`(clave foranea que referencia a Usuario)
    - `monto`
    - `mes`
    - `año`
    - `estado`