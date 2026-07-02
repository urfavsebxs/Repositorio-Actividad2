USE tallerexpress;

INSERT INTO productos_categoria (nombre, descripcion, activo) VALUES
('Herramientas', 'Herramientas para hogar y taller', 1),
('Electrónica', 'Dispositivos y accesorios', 1),
('Hogar', 'Artículos para el hogar', 1),
('Deportes', 'Productos para actividad física', 1),
('Moda', 'Ropa y accesorios', 1);

INSERT INTO productos_marca (nombre, pais_origen, activo) VALUES
('TallerPro', 'Perú', 1),
('TechLine', 'China', 1),
('HomeMax', 'Perú', 1),
('SportFit', 'Brasil', 1),
('StyleWear', 'México', 1);

WITH RECURSIVE seq AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM seq WHERE n < 100
)
INSERT INTO productos_producto (nombre, descripcion, precio, stock, imagen, categoria_id, marca_id, activo, fecha_creacion, fecha_actualizacion)
SELECT
    CONCAT('Producto ', n),
    CONCAT('Descripción del producto ', n, ' para el catálogo.'),
    ROUND(15 + (n * 1.25), 2),
    (n % 20) + 5,
    '',
    CASE MOD(n - 1, 5) + 1
        WHEN 1 THEN 1
        WHEN 2 THEN 2
        WHEN 3 THEN 3
        WHEN 4 THEN 4
        ELSE 5
    END,
    CASE MOD(n - 1, 5) + 1
        WHEN 1 THEN 1
        WHEN 2 THEN 2
        WHEN 3 THEN 3
        WHEN 4 THEN 4
        ELSE 5
    END,
    1,
    NOW(),
    NOW()
FROM seq;

INSERT INTO productos_inventario (producto_id, cantidad, fecha_movimiento, tipo_movimiento)
SELECT id, (id % 15) + 3, NOW(), CASE WHEN id % 2 = 0 THEN 'Entrada' ELSE 'Salida' END
FROM productos_producto;
