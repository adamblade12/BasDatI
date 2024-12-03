CREATE FUNCTION calcular_multa(id_prestamo integer)
RETURNS decimal(10,2)
BEGIN
	DECLARE fecha_prestamo date;
	declare fecha_devolucion date;
	declare dias_retraso integer;
	declare cuota decimal;
	SELECT fecha_prestamo, fecha_devolucion INTO fecha_prestamo, fecha_devolucion
	FROM prestamos
	WHERE id_prestamo = $1;

  -- Obtener la cuota correspondiente (aquí debes ajustar según tu lógica de cálculo de cuota)
  SELECT monto_cuota INTO cuota
  FROM pagos
  WHERE id_usuario = (SELECT id_usuario FROM prestamos WHERE id_prestamo = $1)
  ORDER BY mes_pago DESC
  LIMIT 1;

  IF dias_retraso > 0 THEN
    RETURN dias_retraso * 0.03 * cuota;
  ELSE
    RETURN 0;
  END IF;
END
