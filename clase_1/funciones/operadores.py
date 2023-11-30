def aritmeticos():
    a = 3
    b = 2
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)
    print(a ** b)
    print(a // b)
 
    
def relacionales():
    a = 3
    b = 2
    print(a > b)
    print(a < b)
    print(a >= b)
    print(a <= b)
    print(a == b)
    print(a != b)
    

def logicos(bool1: bool, bool2: bool) -> None:
    '''Acá vemos los operadores lógicos'''
    if(bool1 or bool2):
        print('Al menos uno de los dos valores es Verdadero')
    
    if(bool1 and bool2):
        print('Ambos valores son verdaderos')
        
    if(bool1):
        print('El primer valor es verdadero')
        
    if(not bool1):
        print('El primer parámetro no es verdadero')
        
    if(bool1 == bool2):
        print('Ambos argumentos tienen el mismo valor')
    else:
        print('Los argumentos no poseen el mismo valor')    
    
    if(2 < 1):
        print('Dos es menor que uno')
    elif (4 > 3):
        print('Cuatro es menor a tres')
    elif (10 < 2):
        print('Diez es menor a dos')
    else:
        print('Ninguna comparación de esta cadena de elifs da verdadero')
    
    
def asignacion():
    variable = 3
    print(variable) # 3
    variable += 10
    print(variable) # 13
    variable -= 5
    print(variable) # 8
    variable *= 2
    print(variable) # 16
    variable /= 2 # 8.0
    print(variable)
    variable %= 2 # 0.0
    print(variable)
    
    variable = 2
    variable **= 3
    print(variable) # 8
    variable //= 2
    print(variable) # 4
    
    
def pertenencia():
    variable = [1, 2, 3, 4, 5]
    print(2 in variable)
    print(6 in variable)
    print(2 not in variable)
    print(6 not in variable)
    
    
    