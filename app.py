
from flask import Flask, render_template, redirect, url_for            
from cliente_dao import ClienteDAO                 
from cliente import Cliente
from cliente_forma import ClienteForma


app = Flask(__name__)                               
app.config['SECRET_KEY'] = 'llave_secreta'

titulo_app = 'Zona Fit(GYM)'                            

@app.route('/')                                    
@app.route('/index.html')                          



def inicio():                                       
   app.logger.debug('Entramos al path de inicio/')  
   #return '<p>Hola mundo</p>'                                                                  
   clientes_db = ClienteDAO.seleccionar()
   cliente = Cliente()
   cliente_forma = ClienteForma(obj=cliente)
   return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma) 

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

if __name__ == '__main__':                          
   app.run(debug=True)                             
                                                   
                                                    
                                                   






