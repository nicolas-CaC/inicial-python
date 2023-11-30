def valores_por_defecto(num1=5, num2=10):
    return num1 + num2
    
# var1 = valores_por_defecto(num2=3)
# print(var1)

def variadicas_1(*args):
    for arg in args:
        print(arg)
        
# variadicas_1(1,2,3)
# variadicas_1(5,6,7,78,89,9,90)


def variadicas_2(*argumentos):
    total=0
    for arg in argumentos:
        total += arg
    print(f'La suma total de {argumentos.__str__()} es {total}')
    
# variadicas_2(1,2)
# variadicas_2(1,2,3,4)


def variadicas_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'clave: {key}, valor: {value}')
        
# variadicas_kwargs(nombre='Juan', apellido='Lopez')
# variadicas_kwargs(raza='Chihuahua',animal='Perro',edad=14)


def recursiva(numero):
    
    if numero == 1:
        return numero
    else:
        numero += recursiva(numero - 1)
        return numero
    
    
# print(recursiva(8))


def recursiva_2(texto):
    
    if len(texto) == 1:
        print('Es palíndromo/capicúa')
        return
    
    if texto[0].lower() == texto[-1].lower():
        recursiva_2(texto[1:-1])
    else:
        print('NO es capicúa/palindromo')


# recursiva_2(input('Ingrese su texto: '))
  
  
    
def depurar(texto):
    tabla = texto.maketrans('áéíóú','aeiou','., ')
    return texto.translate(tabla) 
    
    
palindromo = 'Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida.'

palindromo_depurado = depurar(palindromo)

recursiva_2(palindromo_depurado)
