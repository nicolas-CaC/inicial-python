from data.db import db_products


def create_element():
    print('crear')


def read_elements():
    print('leer')


def modify_element(id: int) -> None:
    """Modifica un usuario por id

    Args:
        id (int): Id del usuario
    """
    print('modif')


def delete_element(id):
    print('del')


product_service = {
    1: create_element,
    2: read_elements,
    3: modify_element,
    4: delete_element
}
