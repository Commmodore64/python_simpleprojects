'''
poo_6.py
Script en Python que cree e imprima la informacion de un objeto
de tipo Persona y de otro tipo Deportista.
Las clases Deportista heredara de la clase persona, es decir que
sera un tipo particular de persona.
'''
import Persona
import Deporista

def main():
    per_1 = persona('Hector Tuga', 44)
    deportista = Deportista('Pepe Nava', 33, 'Natacion')

    print(f'''Datos de la persona:
{per_1}''')
    print('-'*30)
    print(f'''datos del deportista:
{deportista}''')

if __name__ == '__main__':
    main()
