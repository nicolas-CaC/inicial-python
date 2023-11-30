from datetime import datetime
import os

def obtener_fecha():
    ahora = datetime.now()
    anio = ahora.year
    mes = ahora.month
    dia = ahora.day
    
    hora = ahora.hour
    minuto = ahora.minute
    segundo = ahora.second
    microsegundo = ahora.microsecond
    
    print(ahora)
    print(dia, mes, anio)
    print(hora, minuto, segundo, microsegundo)
    print(f'{dia}/{mes}/{anio}-{hora}:{minuto}:{segundo}.{microsegundo}')


def buscar_carpeta(folder):
    
    raiz = './'
    
    base = os.path.abspath(raiz)
    results = 0
    
    for root, dirs, files in os.walk(base):
        for dir in dirs:
            if(dir == folder):
                results += 1
                
    if (results == 0):
        print('No se ha encontrado la carpeta buscada')
    else:
        veces = 'vez' if results == 1 else 'veces'
        print(f'La carpeta se encontró {results} {veces} en el proyecto')


def crear_archivo_vacio(nombre):
    with open(nombre, 'w') as file:
        pass
    

def crear_archivo(clase, carpeta):
    
    ahora = datetime.now()
    fecha = f'{ahora.year}_{ahora.month}_{ahora.day}-{ahora.hour}_{ahora.minute}_{ahora.second}_{ahora.microsecond}'
    
    mi_ruta = f'./{clase}/{carpeta}'
    exist = os.path.exists(mi_ruta)
    
    if not exist:
        os.mkdir(mi_ruta)
    
    
    for numero in range(1000):
        nombre = f'{mi_ruta}/{fecha}-{numero}.txt'
        crear_archivo_vacio(nombre)
    
    
    