import mysql.connector

def listarVehiculos(cursor):
    result = cursor.fetchall()
    print("=============================")
    print("Listado de la tabla vehículos")
    print("=============================")
    for coche in result:
        print("Coche Id: ",coche[0])
        print("Marca   : ",coche[1])
        print("Modelo  : ",coche[2])
        print("Precio  : ",coche[3])
        print("==============================\n")




# conexión
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)
database.cursor(buffered=True)

#print(database)

cursor = database.cursor()

"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

bases = cursor.fetchall()

n = 1

for base in bases:
    if base[0] == "master_python":
        print(f"{n} -> *** {base[0]} ***")
    else:
        print(f"{n} -> {base[0]}")
    n += 1

print("\n crear tabla vehículos si no existe...\n")
"""

"""
cursor.execute("" "
    CREATE TABLE IF NOT EXISTS vehiculos(
        ID int(10) auto_increment not null,
        Marca varchar(40) not null,
        Modelo varchar(40) not null,
        precio float(10,2) not null,
        CONSTRAINT pk_vehiculo PRIMARY KEY(ID)
    )
"" ")


cursor.execute("SHOW TABLES")
tablas = cursor.fetchall()
for tabla in tablas:
    print(f"Tabla -> {tabla[0]}")

"""

print("\nagregar registros a la tabla vehículos...\n")

coches = [
    ("Nissan", "AJ30", 7854),
    ("Mercedes", "S500", 20500),
    ("Ford", "Puma", 9999),
    ("Ford","F350",3800)
]

cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
database.commit()

cursor.execute("SELECT * FROM vehiculos")

listarVehiculos(cursor)

"""
cursor.execute("DELETE FROM vehiculos WHERE Marca = 'Nissan'")
print(cursor.rowcount, " borrado/s!!!\n")
database.commit()

cursor.execute("SELECT * FROM vehiculos")

listarVehiculos(cursor)
"""
print("\n============================================")
print("Se aumenta el precio de los vehículos un 25%")
print("============================================")
cursor.execute("UPDATE vehiculos SET precio=(precio*1.25);")
database.commit()
cursor.execute("SELECT * FROM vehiculos ORDER BY Marca, Modelo, Precio DESC;")
listarVehiculos(cursor)
print(f"Se han listado {cursor.rowcount} registros.")





