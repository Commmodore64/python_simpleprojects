'''
poo_5.py
Script en Python que utilice el menu de una clase Receta dentro
de la cual habra una lista de ingredientes. Cada Ingrediente tendra
como atributos los siguientes:
    - nombre
    - cantidad
    - unidad de medida
La clase Receta ademas de contener un menu y una lista de ingredientes
debera tener un nombre y una lista de pasos o instrucciones asi como los 
siguientes comportamientos:
    - Agregar ingrediente
    - Consultar ingredientes
    - Agregar paso
    - Consultar Pasos
'''
from receta import Receta

def main():
    receta = Receta('Pizza')

    receta.menu()
    print(receta)

if __name__ == '__main__':
    main() 
