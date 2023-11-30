class Customer:

    id = 0

    def __init__(self, nombre, apellido, edad):
        Customer.id += 1
        self.id = Customer.id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def description(self):
        print(f"\nLos datos son:\n") 
        print(f"id:{self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
    