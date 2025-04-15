# Creando una conexión pool
from mysql.connector import pooling 
from mysql.connector import Error #importamos este paquete para poder acceder al error de except


class Conexion:
    DATABASE = 'zona_fit_db' # Estos datos se encuentran dentro del MySQL workbench
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5   # Este es el número de cursores que queremos crear
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod # Creamos un método de clase
    def obtener_pool(cls): #Con este parámetro podemos acceder a todas las constantes y atributos de clase
        if cls.pool is None: # Si la constante de clase pool tiene el valor de none creamos el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(  # llamamos la variable constante pool y usamos el método que hemos obtenido del paquete Mysql
                    pool_name=cls.POOL_NAME, #vamos asignando las variables contantes
                    pool_size=cls.POOL_SIZE,
                    host = cls.HOST, 
                    port = cls.DB_PORT,               # Ese if solo se ejecuta si no hay objeto pool
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password= cls.PASSWORD
                )
                return cls.pool # Una vez creado el objeto, lo devolvemos.
            except Error as e: 
                print('Ocurrió un error al obtener pool: {e}')

        else:
            return cls.pool # pero si ya hay objeto pool pues solo hay que devolverlo.

    @classmethod
    def obtener_conexion(cls): #creamos más métodos de clase
        return cls.obtener_pool().get_connection() # Con esto devolvemos un objeto de tipo pool que pide devolver un objeto de tipo conexión
    

    @classmethod
    def liberar_conexion(cls, conexion): # Este método liberará la conexión
        conexion.close() # Una vez que una conexión se cierre, este objeto estará disponible para otro usuario

if __name__ == '__main__':
     # creamos un objeto pool
    pool = Conexion.obtener_pool() # Llamamos a la clase conexión y creamos un objeto de tipo pool
    print(pool)
    conexion1 = pool.get_connection() # A través del objeto pool creamos una conexión.
    print(conexion1)
    Conexion.liberar_conexion(conexion1) # Usamos de nuevo la clase conexión con el método para liberar la conexión.
    print('Se ha liberado el objeto conexión1')