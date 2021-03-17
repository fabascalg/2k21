import usuarios.conexion as conexion
import datetime
import hashlib

connect = conexion.conectar()
db = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registro(self):
        fecha = datetime.datetime.now() 
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s) "
        usuario = (self.nombre, self.apellidos,
                   self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            db.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        #cifrado
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        #datos para consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        return result



