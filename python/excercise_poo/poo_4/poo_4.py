'''
poo_4.py
Script en Python que cree y asigne valor a los atributos de un
objeto tipo Ingrediente. Los ingredientes seran modelados dentro
de una clase en un modulo separado y tendran los siguientes atributos:
    - nombre
    - cantidad
    - unidad de medida
Ademas la clase Ingrediente podra recibir como argumentos los valores
iniciales para sus actributos a traves del metodo constructor.
'''
from ingrediente import Ingrediente

def main():
    ingrediente = Ingrediente('Papa', 3, 'Kilos')

    print(ingrediente)

if __name__ == '__main__':
    main()
