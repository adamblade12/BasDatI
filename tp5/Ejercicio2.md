** Ejercicio: Estadias **

**Esquema en BD:**
`ESTADIA<dniCliente, codHotel, cantidadHabitaciones, direccionHotel, ciudadHotel,dniGerente, nombreGerente, ciudadCliente,fechaInicioHospedaje, cantDiasHospedaje, #Habitacion>`

**Restricciones:**
a. Existe un único gerente por hotel(`dniGerente`). Un gerente podría gerenciar más de un hotel.
b. Un cliente (`dniCliente`) puede realizar la estadía sobre más de una habitación del hotel en la misma fecha. Para cada habitación puede reservar diferentes cantidades de días.
c. (`cantidadHabitaciones`) indica la cantidad de habitaciones existentes en un hotel.
d. El código de hotel (`codHotel`) es único y no puede repetirse en diferentes ciudades.
e. Un cliente puede realizar reservas en diferentes hoteles (`codHOtel`) para la misma fecha.
f. #Habitacion se puede repetir en distintos hoteles.
g. En la misma (`direccionHotel`) de una ciudadHotel puede haber más de un hotel funcionando.

### Paso 1: Determinar dependencias funcionales (DFs)

A partir del esquema de la base de datos y las restricciones dadas podemos determinar las siguientes dependencias funcionales:

1. **codHotel -> dniGerente , nombreGerente**  existe un unico gerente por hotel, lo cual implica que los atributos `dniGerente` y `nombreGerente` dependen funcionalmente de `codHotel`.
2. **codHotel -> direccionHotel, ciudadHotel** en la misma `direccionHotel` de una `ciudadHotel` puede haber mas de un hotel funcionando, lo que indica que `ciudadHotel` y `direccionHotel` dependen funcionalmente de `codHotel`.
3. **codHotel -> #habitacion** `#habitacion` se puede repetir en distintos hoteles, por lo tanto depende funcionalmente de `codHotel`.
4. **codHotel -> cantidadHabitaciones** `cantidadHabitaciones` indica la cantidad de habitaciones en un hotel, por lo tanto `cantidadHabitaciones` depende funcionalmente de `codHotel`.
5. **codHotel, dniCliente -> idReserva,#habitacion** las reservas pueden definirse con una `idReserva` y `#habitacion` que depende funcionalmente de `codHotel` y `dniCliente`.

### Paso 2: Determinar claves candidatas

Para determinar las **claves candidatas**, necesitamos encontrar un conjunto de atributos que puedan identificar de manera única a cada fila de la tabla `ESTADIA`.

-La combinacion de las claves **`codHotel`, `dniCliente`** basta para identificar de forma unica cada registro de la tabla,ya que:
    -`codHotel` identifica al hotel.
    -`dniCliente` identifica al cliente del hotel.

Por lo tanto, la **clave candidata** es:
-(`codHotel`,`dniGerente`,`dniCliente`)

Esta combinacion asegura que cada registro sea unico y no haya duplicados.

### Paso 3: Diseño de la tercera forma normal

Para llevar el esquema a la **Tercera Forma Normal (3FN)**, necesitamos eliminar dependencias transitivas y asegurarnos de que cada atributo no clave dependa únicamente de la clave primaria completa. Esto implica dividir la tabla en varias tablas relacionadas para reducir la redundancia y asegurar la integridad de los datos.

Se dividio la tabla `ESTADIAS` en las tablas(`Estadias`,`Hotel`,`Gerente`,`Cliente`,`Reservas`,`Habitacion`) para eliminar dependencias transitorias y garantizar que cada atributo no clave dependa unicamente de la clave primaria completa.

El nuevo diseño seria el siguiente:
1. **Tabla `Estadias`**
   -`codHotel` (Clave foranea que referencia a `Hotel`)
   -`dniCliente` (Clave foranea que referencia a `Cliente`)
   -`fechaInicioHospedaje`
   -`cantDiasHospedaje`
   Clave primaria compuesta (`codHotel`,`dniCliente`)

2. **Tabla `Hotel`**
   -`codHotel` (Clave primaria que identifica al hotel)
   -`dniGerente` (Clave foranea que identifica al Gerente del hotel)
   -`cantidaHabitaciones`
   -`direccionHotel`
   .`ciudadHotel`

3. **Tabla `Gerente`**
   - `dniGerente` (Clave primaria)
   - `nombreGerente`

4. **Tabla `Cliente`**
   - `dniCliente` (Clave primaria)
   - `nombreCliente`
   - `diudadCliente`

5. **Tabla `Habitacion`**
   - `#habitacion` (Clave primaria)
   - `codHotel` (Clave foranea que referencia a `Hotel`)

6. **Tabla `Reservas`**
   - `idReservas` (Clave primaria)
   - `dniCliente` (Clave foranea que referencia a`Cliente`)
   - `codHotel` (Clave foranea que referencia a `Hotel`)
   - `#habitacion`
   - `cantDIasHospedaje`