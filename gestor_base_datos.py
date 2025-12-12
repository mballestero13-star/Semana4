import sqlite3

# Conexión a SQLite (se crea el archivo si no existe)
conn = sqlite3.connect("databaseLeccion5.db")
cursor = conn.cursor()

# Eliminar tablas si ya existen (para ejecutar limpio)
cursor.execute("DROP TABLE IF EXISTS ventas;")
cursor.execute("DROP TABLE IF EXISTS productos;")
cursor.execute("DROP TABLE IF EXISTS clientes;")

# Tabla clientes
cursor.execute("""
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT UNIQUE NOT NULL
);
""")

# Tabla productos
cursor.execute("""
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL CHECK(precio >= 0)
);
""")

# Tabla ventas (relación con clientes y productos)
cursor.execute("""
CREATE TABLE ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL CHECK(cantidad > 0),
    fecha TEXT NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id),
    FOREIGN KEY(producto_id) REFERENCES productos(id)
);
""")

# Insertar datos de prueba
cursor.execute("INSERT INTO clientes(nombre, correo) VALUES('Ana', 'ana@example.com');")
cursor.execute("INSERT INTO clientes(nombre, correo) VALUES('Luis', 'luis@example.com');")

cursor.execute("INSERT INTO productos(nombre, precio) VALUES('Café', 3.50);")
cursor.execute("INSERT INTO productos(nombre, precio) VALUES('Pan', 1.20);")

cursor.execute("INSERT INTO ventas(cliente_id, producto_id, cantidad, fecha) VALUES(1, 1, 2, '2025-01-01');")
cursor.execute("INSERT INTO ventas(cliente_id, producto_id, cantidad, fecha) VALUES(2, 2, 3, '2025-01-02');")

conn.commit()
conn.close()

print("✅ Base de datos creada con éxito: databaseLeccion5.db")
