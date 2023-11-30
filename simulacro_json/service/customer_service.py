from data.db import db_customers
from model.Customer import Customer
from helpers.customer_helpers import get_data
import service.files_service as file

path = "./data/users.json"


def create_element():
    nombre, apellido, edad = get_data()
    customer = Customer(nombre, apellido, edad)
    customer.description()
    users = file.load_json(path)
    users.append(customer.__dict__)
    file.write_json(path, users)
    # db_customers.append(customer.__dict__)


def read_elements():
    interval = 10
    users = file.load_json(path)
    for index, user in enumerate(users):
        print(user)
        if index % interval == 0:
            char = input(
                f"\nPresione ENTER para ver los siguientes {interval} resultados o ingrese 'q' y ENTER para salir..."
            )
            if char == "q":
                break
        # print(user["id"])
        # print(f'first name: {user["first_name"]}')
        # print(f'last name: {user["last_name"]}')
        # print(f'username: {user["username"]}')
        # print(f'telefono: {user["phone_number"]}')
        # print(f'email: {user["email"]}')
        print("\n")
    # for customer in db_customers:
    #     print(customer)


def modify_element():
    exist = False
    id = int(input("Ingrese el id: "))
    users = file.load_json(path)

    for customer in users:
        if customer["id"] == id:
            exist = True
            nombre, apellido, edad = get_data()
            customer["nombre"] = nombre
            customer["apellido"] = apellido
            customer["edad"] = edad
            file.write_json(path, users)
            break

    if not exist:
        print("No se encontró un cliente con ese id.")


def delete_element():
    exist = False
    id = int(input("Ingrese el id: "))  # 2
    users = file.load_json(path)

    for index, customer in enumerate(users):
        if customer["id"] == id:
            del users[index]
            file.write_json(path, users)
            exist = True

    if not exist:
        print("No se encontró un cliente con ese id.")


customer_service = {
    1: create_element,
    2: read_elements,
    3: modify_element,
    4: delete_element,
}
