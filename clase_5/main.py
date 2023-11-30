from clase_5.funciones.leer_archivos import load_pdf, load_txt, write_txt, write_json

dic = {
    "nombre": "Pepe",
    "edad": 2
}

def clase_5():
    # load_pdf('./clase_5/data/principito.pdf')
    # load_txt('./clase_5/data/texto.txt')
    # write_txt('./clase_5/data/texto2.txt', 'Estamos terminando!')
    write_json('./clase_5/data/db2.json', dic)