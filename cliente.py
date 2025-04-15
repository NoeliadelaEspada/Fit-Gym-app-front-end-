class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresía=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresía = membresía
    
    def __str__(self):
        return f'Id: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Membresía: {self.membresía}'
