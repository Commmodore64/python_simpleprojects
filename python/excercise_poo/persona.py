'''
persona.py
Modelo sencillo de una Persona.
Atributos:
    nombre
    edad
comportamientos:
    hablar(mensaje) - mensaje: el mensaje que dira la persona.
    comer(alimento) - alimento: el alimento que consume la persona.
'''

class Persona:
    def __init__(self, nombre='', edad=None):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    @nombre.deleter
    def nombre(self):
        del self._nombre
    
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,valor):
        self._edad = valor
    @edad.deleter
    def edad(self):
        del self._edad
    
    def hablar(self, mensaje):
        print(f'{self.nombre}: {mensaje}')

    def comer(self, alimento):
        print(f'{self.nombre} esta comiendo {alimento}.')
    
    def __str__(self):
        return f'''Nombre: {self.nombre}
Edad: {self.edad}'''
