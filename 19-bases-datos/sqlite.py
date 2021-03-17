# importar módulo

import sqlite3

# conexión

conexion = sqlite3.connect('./19-bases-datos/pruebas.db')

cursor = conexion.cursor()

# instrucción con sintáxis de python
"""
cursor.execute("CREATE TABLE IF NOT EXISTS productos(" +
               "ID INTEGER PRIMARY KEY AUTOINCREMENT," +
               "Titulo varchar(255)," +
               "Descripcion text," +
               "precio int(255)" +
               ")")
"""
# alternativa con sintáxis de SQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo varchar(255),
    Descripcion text,
    precio int(255)
);
""")


# guardar los cambios
conexion.commit()

"""
cursor.execute(
    "INSERT INTO productos VALUES (null, 'Artículo 1','Descripción del artículo 1 (uno)', 235)")

conexion.commit()
"""

# borrar registros

cursor.execute("DELETE FROM productos")

registros = [
    ("ordenador portátil", "Asus", 500),
    ("teléfono móvil", "Xiaomi", 150),
    ("placa base", "Asus", 80),
    ("tablet 10\"", "Huawei", 180)
]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", registros)
conexion.commit()
# listar datos

cursor.execute("UPDATE productos SET precio=precio*2 WHERE precio<180;")


cursor.execute("SELECT * FROM productos")

productos = cursor.fetchall()



cursor.execute("SELECT * FROM productos")

articulo = cursor.fetchone()

# cerrar conexión
conexion.close()

for producto in productos:
    #print(producto[0], producto[1])
    #print(producto)
    for campo in producto:
        print(campo)
    print("\n")

print("\n")

print(articulo)