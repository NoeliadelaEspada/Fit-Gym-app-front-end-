from conexion import Conexion   #Importamos la clase Conexion
from cliente import Cliente #Importamos la clase Cliente



class ClienteDAO: # Esta clase podrá interactuar con el objeto cliente 
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'   #con ORDER BY id ordenamos los valores de la tabla por el id
    SELECCIONAR_ID = 'SELECT * FROM cliente WHERE id=%s'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresía) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresía=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar_por_id(cls, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            valores = (id,)
            cursor = conexion.cursor() 
            cursor.execute(cls.SELECCIONAR_ID, valores)  
            registro = cursor.fetchone() 
            cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
            return cliente
        except Exception as e:
            print(f'Ha sucedido un error al seleccionar los datos: {e}')
        finally: 
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion) 
        


    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion() # Creamos un objeto conexión y con la ayuda de la clase Conexión, usamos el método obtener conexión
                                                    # Una vez creado esto, sabemos que el bloque finally si se ejecuta ya que si que existe una conexión.
            cursor = conexion.cursor() #creamos un objeto cursor y con la ayuda de la conexión creamos un cursor.
            cursor.execute(cls.SELECCIONAR)  #con ayuda del cursor que utiliza el método execute, ejecutamos la constante de clase seleccionar.
            registros = cursor.fetchall() #hacemos que todos los registros se procesen y almacenen en esta variable
                                         # no solo haremos eso, sino que por cada registro que recuperemos crearemos un objeto de tipo cliente (que proviene de la clase Cliente)
            # MAPEO de clase-tabla cliente
            clientes = []
            for registro in registros: # Con un bucle for creamos un objeto cliente por cada fila y en él almacenaremos los registros 0, 1, 2, 3 [id, nombre, apellido y membresía]
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente) # Agregamos a nuestra lista clientes todos los objetos clientes
            return clientes
        except Exception as e:
            print(f'Ha sucedido un error al seleccionar los datos: {e}')

        finally: # este finally revisará si el objeto conexión es distinto a None. Si lo es, eso implica que ya se utilizó y por lo tanto hay que liberarlo.
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion) #Con ayuda de la clase Conexión, llamamos al método cerrar conexión y la cerramos
        

    @classmethod
    def insertar(cls, cliente): #Este método recibe un objeto de tipo cliente
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresía) #añadimos los valores
            cursor.execute(cls.INSERTAR, valores) #llamamos a la constantede clase ELIMINAR y ofrecemos los valores como parámetro
            conexion.commit() #Guardamos los datos en la base de datos
            return cursor.rowcount # Esto nos devuelve los valores insertados
        
        except Exception as e:
            print(f'Ha ocurrido un error insertando los datos: {e}')

        finally:
            if Conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresía, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Sucedió un error a la hora de actualizar los datos: {e}')
        finally:
            if Conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,) #Al ser una tupla siempre se debe de añadir una coma
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Se ha producido un error al eliminar los datos: {e}')

        finally:
            if Conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    """
    # Insertar cliente:

    cliente1 = Cliente(nombre='Daniel', apellido='Garcia', membresía=350) #insertamos clientes
    clientes_insertados = ClienteDAO.insertar(cliente1) #llamamos a la clase clienteDAO con el método insertar e insertamos el nuevo cliente
    print(f'Clientes insertados: {clientes_insertados}')
    """

    """ 
    # Insertar cliente:

    cliente_actualizar = Cliente(3, 'Marta', 'Garcia', 400) #actualizamos el cliente
    cliente_actualizado = ClienteDAO.actualizar(clienteactualizar)
    print(f'Clientes actualizados: {clienteactualizado}')
    """

    # Eliminar cliente:
    """
    cliente_eliminar = Cliente(id=3)
    cliente_eliminado = ClienteDAO.eliminar(cliente_eliminar)
    print(f'Se ha eliminado el siguiente cliente: {cliente_eliminado}')
"""

    # Mostrar información de la base de datos:
    clientes = ClienteDAO.seleccionar()     #creamos un objeto de tipo cliente y seleccionamos a los clientes
    for cliente in clientes: #Por cada uno de los objetos de tipo cliente que tenemos en nuestra lista, lo iteramos e imprimimos.
        print(cliente)

