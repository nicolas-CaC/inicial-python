import service.file_csv_services as csv


path = './files/personas.csv'
persona = ['Luisa', 'Gutierrez', '444444', '60', 'luisa@mail.net']
mail = 'sara@mail.com'
nuevos_datos = ['Sarita', 'Montiel', '987654', '10']


# % READ (cRud)


def read_data(path):

    data = csv.load_csv(path)

    for row in data:
        print(row)


# read_data(path)


'''

'''

# % CREATE (Crud)


def create_data(path, user):

    data = csv.load_csv(path)
    data.append(user)

    csv.save_csv(path, data)
    print('\nLos nuevos datos del archivo son:\n')
    read_data(path)


# create_data(path, persona)


'''

'''

# % UPDATE (crUd)


def modify_data(path, mail, user):

    data = csv.load_csv(path)

    for row in data:
        if row[-1] == mail:
            row[0] = user[0]
            row[1] = user[1]
            row[2] = user[2]
            row[3] = user[3]

    csv.save_csv(path, data)


modify_data(path, mail, nuevos_datos)

'''

'''

# % DELETE (cruD)


def delete_data(path, mail):

    data = csv.load_csv(path)

    for index, row in enumerate(data):
        if row[-1] == mail:
            del data[index]

    csv.save_csv(path, data)


# delete_data(path, mail)
