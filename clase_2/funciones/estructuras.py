def tuplas():
    tupla = ('hola', 3, True, 2.3)
    print(tupla)
    print(tupla[1])
    
    tupla = 'buenas', 2, False
    print(tupla)
    print(tupla[2])
    

def listas():   
    lista = ['hola', 3, True, 2.3]
    print(lista)
    print(lista[1])
    
    lista = ['buenas', 2, False]
    print(lista)
    print(lista[2])
    
    lista[1] = 49
    lista.append('Soy un str')
    lista2 = [3, 'soy una lista', True]
    lista.extend(lista2)
    lista.insert(0,34534)
    # del(lista[0])
    print(lista)
    print(lista[2:])
    print(lista[:4])
    print(lista[2:4])
    print(lista[-1])
    print(lista.index(49))
    lista.pop()
    print(lista)
    print(len(lista))

def diccionarios():
    dic = {
        'clave_1': 'a', 
        'clave_2': 3
        }
    print(dic)
    
    personaje1 = {
        'brazos': 2,
        'ojos': 'negro'
    }
    
    personaje2 = {
        'brazos': 4,
        'ojos': 'rojo'
    }
    
    print(personaje1['brazos'])
    print(personaje2['ojos'])
    
    var1, var2, var3 = 1, 2, 300
    print(var3)
