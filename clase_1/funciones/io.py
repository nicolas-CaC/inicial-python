def inputs():
    nombre = input('Ingrese su nombre: ')
    print(nombre, type(nombre))
    
    
def casting():
    # edad = int(input('Ingrese su edad: '))
    # print(edad, type(edad))

    variable = 12
    print('Soy una cadena y tengo un nro. al lado', variable)
    print(type(variable))
    
    variable = str(variable)
    print(variable, type(variable))
    
    
def formatos():
    variable1 = 20
    variable2 = 30.56789
    
    print(variable1, '<- Número')
    print('Los valores son {} y {}'.format(variable1, variable2))
    print(f'Otro formato de mostrar es {variable1} y {variable2}')
    
    print(f'formateo de variable2 {variable2:.2f}')
    print(f'formateo de variable2 {variable2:.1%}')
    print(f'formateo de variable2 {variable2:e}')