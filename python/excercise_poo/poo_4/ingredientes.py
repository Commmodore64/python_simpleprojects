'''
ingrediente.py
Modelo sencillo para un ingrediente.
Atributos:
    nombre -- Nombre del ingrediente.
    cantidad -- Cantidad necesaria del ingrediente.
    unidad -- Unidad de medida para el ingrediente.
'''

class Ingrediente:
    def __init__(self, nombre='', cantidad=None, unidad=''):
        self._nombre = nombre
        self._cantidad = cantidad
        self._unidad = unidad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,valor):
        self._nombre = valor
    
    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self,valor):
        self._cantidad = valor

    @cantidad.deleter
    def cantidad(self):
        del self._cantidad

    @property
    def unidad(self):
        return self._unidad

    @unidad.setter
    def unidad(self,valor):
        self._unidad = valor

    @unidad.deleter
    def unidad(self):
        del self._unidad

    def __str__(self):
        return f'''Nombre: {self.nombre}
Cantidad: {self.cantidad} {self.unidad}'''
