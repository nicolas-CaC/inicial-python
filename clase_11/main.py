def suma_primitiva(nro):
    nro = nro + 10
    return nro


numero = 5
retorno = suma_primitiva(numero)

# print(retorno)  # 15
# print(numero)  # 5


def suma_colecciones(coleccion):
    for index in range(len(coleccion)):
        coleccion[index] = coleccion[index] + 10
        # lista[index] = lista[index] + 10
    return coleccion


lista = [100, 101, 102, 103]


retorno = suma_colecciones(lista)

print(retorno)  # [110, 111, 112, 113]
print(lista)  # [110, 111, 112, 113]
