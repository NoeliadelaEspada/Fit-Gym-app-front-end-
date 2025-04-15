
from flask import Flask, render_template, redirect, url_for            #importamos la clase flask desde el paquete de flask y el método render_Template
from cliente_dao import ClienteDAO                 #importamos la clase ClienteDAO
from cliente import Cliente
from cliente_forma import ClienteForma


app = Flask(__name__)                               #definimos la variable de app e indicamos que trabajaremoscon este archivo
app.config['SECRET_KEY'] = 'llave_secreta'

titulo_app = 'Zona Fit(GYM)'                             #añadimos una variable con el título de nuestra aplicación. 

@app.route('/')                                     #Agregamos la anotación, la cual vamos a indicar que va a procesar la petición http de / url
@app.route('/index.html')                           #esto significa que nuestra petición es url: http://localhost:5000/



def inicio():                                       #definimos el método que va a procesar esta petición, puede tener cualquier nombre y no  recibirá ningún parámetro.
   app.logger.debug('Entramos al path de inicio/')  # Mandamos a imprimir un mensaje a consola, utilizando el objeto de app, el objeto de logger y el modo debug
   #return '<p>Hola mundo</p>'                       #Esto lo que hace es mandar un mensaje a consola                                               
   clientes_db = ClienteDAO.seleccionar()
   cliente = Cliente()
   cliente_forma = ClienteForma(obj=cliente)
   return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma) #Y devolvemos una cadena con contenido html

@app.route('/guardar', methods=['POST'])
def guardar():
   cliente = Cliente()
   cliente_forma = ClienteForma(obj=cliente)
   if cliente_forma.validate_on_submit():
      cliente_forma.populate_obj(cliente)
      if not cliente.id:
         ClienteDAO.insertar(cliente)
      else:
         ClienteDAO.actualizar(cliente)
   return redirect(url_for('inicio'))

@app.route('/limpiar')
def eliminar():
   return redirect(url_for('inicio'))

@app.route('/editar/<int:id>')
def editar(id):
   cliente = ClienteDAO.seleccionar_por_id(id)
   cliente_forma = ClienteForma(obj=cliente)
   clientes_db = ClienteDAO.seleccionar()
   return render_template('index.html', titulo=titulo_app, clientes = clientes_db, forma=cliente_forma)

@app.route('/eliminar/<int:id>')
def borrar(id):
   cliente = Cliente(id=id)
   ClienteDAO.eliminar(cliente)
   return redirect(url_for('inicio'))

if __name__ == '__main__':                          #Ejecutamos nuestra app y comprobamos si estamos ejecutando desde este archivo
   app.run(debug=True)                              #utilizamos nuestro objeto app y mandamos a llamar al método run() que ejecuta nuestro servidor, se levanta el servidor de flask y está listo para recibir peticiones 
                                                    #para que los cambios se reflejen de manera automatica lo iniciamos en modo debug
                                                    #aunque podriamos utilizar el print, lo recomendable es usar el concepto de logger.

                                                    #Imagina que también queremos procesar la peticion de indexHTML. Podríamos hacerlo a través del método inicio
                                                    #Para ello añadimos otra ruta con la url de index.html
                                                    #De esta forma, estaríamos procesando el siguiente url: http://localhost:5000/index.html
                                                    
                                                    #Como vemos en el comentario, anteriormente retornamos una cadena ''hola mundo'', pero ahora utilizaremos el método render_template y especificamos el archivo que queremos retornar.
                                                   #Luego, volvemos al return, donde se encuentra el método render_template(‘index_html’) y añadimos un parámetro. Este tendrá cualquier nombre, pero al tratarse del título, lo llamaremos como tal y dentro almacenaremos la variable titulo_app.







