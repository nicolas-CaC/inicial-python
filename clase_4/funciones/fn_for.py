def fn_for():
    inicio = int(input('ingrese el numero de partida: '))
    fin = int(input('ingrese el numero limite: '))
    pasos = int(input('ingrese de cuánto en cuánto vamos a recorrer esos números: '))
    
    for numero in range(inicio, fin, pasos):
        print(numero)
        
        
def fn_for_2():
    texto = "Hola a todos!"
    for letra in texto:
        print(letra)
        
        
def texto(letra_a_buscar):
    texto = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel deserunt sunt placeat officia eaque fugit quibusdam deleniti qui veritatis facilis, dolores rem ut dicta ipsum illum delectus atque illo beatae.'
    
    # total = 0
    nuevo_texto = ''
    
    for letra in texto:
        if(letra != letra_a_buscar):
            # total += 1
            nuevo_texto += letra
            
    # print(f'la letra {letra_a_buscar} se repite {total} veces')
    print(f'el nuevo texto es el siguiente:\n{nuevo_texto}')
    

def buscar_palabra(palabra_a_buscar):
    texto = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel deserunt sunt placeat officia eaque fugit quibusdam ipsum deleniti qui veritatis facilis, dolores ipsum rem ut dicta ipsum illum delectus atque illo beatae.'
    
    texto = texto.split(' ')
    total = 0
    
    for palabra in texto:
        if(palabra == palabra_a_buscar):
            total += 1
    
    print(f'La palabra {palabra_a_buscar} se repite {total} veces.')
    
