from os import system

options = [ 
           'Salir',
           'Leer los registros',
           'Crear un registro',
           'Modificar un registro',
           'Borrar un registro',
           'Despedirme de todos'
           ]

def menu():
    
    continuar = True
    
    while(continuar):
        
        system('cls')
        print('Seleccione la opción que quiera ejecutar:\n')
        
        for index, option in enumerate(options):
            print(f'{index}- {option}')
        
        select_option = int(input('\nIngrese la opción deseada: '))
        
        if(select_option >= 0 and select_option < 5):
            continuar = False
        
        