from typing import List
from os import system

system('cls')


def ingresar_numeros() -> List[int]:

    numeros = []

    continuar = True

    while continuar:
        numero = input('Ingrese un número (ingrese "q" para terminar): ')

        if numero == 'q':
            continuar = False
        else:
            try:
                numero = int(numero)
                numeros.append(numero)
            except:
                print('Valor inválido. Ingrese sólo números.')
                continue

    return numeros


def promediar_numeros(numeros: List[int]):

    total = 0

    min_value = 10000000000000000000000
    max_value = 0

    count_min_value = 0
    count_max_value = 0

    for numero in numeros:
        total += numero

        if numero > max_value:
            max_value = numero
            count_max_value += 1

        if numero < min_value:
            min_value = numero
            count_min_value += 1

    promedio = ((max_value - min_value) / 2) + min_value

    return total, promedio, min_value, max_value, count_min_value, count_max_value


def tendencia(min: int, max: int):
    if min > max:
        return 'Tiende a ingresar números más bajos'
    else:
        return 'Tiende a ingresar números más altos'


numeros = ingresar_numeros()

(total,
 promedio,
 min_value,
 max_value,
 count_min_value,
 count_max_value
 ) = promediar_numeros(numeros)

print(f'\ntotal: {total}, menor valor: {min_value}, máximo valor: {max_value}')
print(f'promedio: {promedio}, {tendencia(count_min_value, count_max_value)}')
print(
    f'cantidad mínimos: {count_min_value}, cantidad máximos: {count_max_value}')
