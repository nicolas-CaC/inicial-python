from data.db import db_customers
from model.Customer import Customer
from helpers.customer_helpers import get_data


def create_element():
    nombre, apellido, edad = get_data()
    customer = Customer(nombre, apellido, edad)
    customer.description()
    db_customers.append(customer.__dict__)


def read_elements():
    for customer in db_customers:
        print(customer)


def modify_element():
    exist = False
    id = int(input('Ingrese el id: ')) 
     
    for customer in db_customers:
        if customer['id'] == id:
            exist = True
            nombre, apellido, edad = get_data()
            customer['nombre'] = nombre
            customer['apellido'] = apellido
            customer['edad'] = edad
            break
    
    if not exist:
        print('No se encontró un cliente con ese id.')
  

def delete_element():
    exist = False
    id = int(input('Ingrese el id: '))
    
    for index, customer in enumerate(db_customers):
        if customer['id'] == id:
            del db_customers[index]
            
    if not exist:
        print('No se encontró un cliente con ese id.')
            
    

customer_service = {
    1: create_element,
    2: read_elements,
    3: modify_element,
    4: delete_element
}