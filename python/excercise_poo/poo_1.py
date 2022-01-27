'''
poo_1.py
Script en Python que implemente una clase Figura que como atributo
tenga la cantidad de lados.

Una vez creada la clase crear dos figuras (objetos) y mostrar
su cantidad de lados.
'''

class Figura:
    def __init__(self):
        self._lados = None

    @property #getter : Regresa el valor asociado a la cantdad de lados
    def lados(self):
        return self._lados

    @lados.setter #Permite asignarle valor al atributo lados
    def lados(self, valor):
        if valor < 3:
            print('El valor debe ser mayor que 3')
            self._lados = None
        else:
            self._lados = valor
    
    @lados.deleter
    def lados(self):
        del self._lados

def main():
    triangulo = Figura()
    cuadrado = Figura()

    triangulo.lados = -3
    cuadrado.lados = 4

    print(f'El triangulo tiene {triangulo.lados} lados.')
    print(f'El cuadrado tiene {cuadrado.lados} lados.')

if __name__ == '__main__':
    main()
