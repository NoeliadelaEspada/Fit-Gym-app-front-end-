from conexion import Conexion   
from cliente import Cliente 



class ClienteDAO: 
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'   
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
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor() 
            cursor.execute(cls.SELECCIONAR)  
            registros = cursor.fetchall() 
                                        
            clientes = []
            for registro in registros: 
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente) 
            return clientes
        except Exception as e:
            print(f'Ha sucedido un error al seleccionar los datos: {e}')

        finally: 
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion) 
        
    @classmethod
    def insertar(cls, cliente): #Este método recibe un objeto de tipo cliente
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresía) 
            cursor.execute(cls.INSERTAR, valores) 
            conexion.commit() 
            return cursor.rowcount 
        
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

    
    clientes = ClienteDAO.seleccionar()     
    for cliente in clientes:
        print(cliente)

