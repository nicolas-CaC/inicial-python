import colorama
import timeit
import requests
import json

colorama.init()

# print(colorama.Fore.GREEN + 'hoa' + colorama.Style.RESET_ALL)
# print('Segunda linea')
# print(colorama.Back.CYAN + 'Tercera linea' + colorama.Style.RESET_ALL)


def funcion_1():
    return 1


def funcion_2():
    total = 0
    for nro in range(1000000):
        total += nro
    return total


# tiempo_1 = timeit.timeit(funcion_1, number=100)
# print(f'La funcion_1 tarda {tiempo_1} seg. en ejecutarse')

# tiempo_2 = timeit.timeit(funcion_2, number=100)
# print(f'La funcion_1 tarda {tiempo_2} seg. en ejecutarse')


url = 'https://pokeapi.co/api/v2/pokemon/squirtle'

# data = requests.get(url)
# info = json.dumps(data.json())
# print(info)

lista = []

libro = {
    'id': input('ingrese id: '),
    'nombre': input('ingrese nombre: '),
    'edicion': int(input('ingrese edad: ')),
}

lista.append(libro)


print(lista)
print('La base de datos se ha actualizado')
