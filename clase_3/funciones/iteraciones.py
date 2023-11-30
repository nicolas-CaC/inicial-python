def iteracion_array():
    lista = [1,2,3,2,1]
    for valor in lista:
        print(valor * 10)
        

def iteracion_pasos(): 
    for valor in range(1, 10, -1):
        print(valor)
        

dic = {
    'nombre': 'Juan',
    'apellido': 'Lopez',
    'edad': 32
}

def iteracion_dic():
    
    for clave in dic.keys():
        print(f'Este campo se llama {clave}')
    
    for valor in dic.values():
        print(f'valor: {valor}')
        
    for clave, valor in dic.items():
        print(f'La clave {clave} contiene el valor {valor}')
    

def obtener_dato():
    print(dic['nombre'])
    print(dic.get('nombre'))
    
def modificar_valores():
    dic['nombre'] = 'Roberto'
    print(dic)
    dic['dni'] = 1234
    print(dic)