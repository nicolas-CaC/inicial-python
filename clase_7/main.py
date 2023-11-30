from service.customer_service import customer_service
from service.product_service import product_service
from service.menu_service import menu_service
from config.data import selections

def main():
    
    while True:
        menu_service()
        
        if(selections[0] == 1):
            customer_service[selections[1]]()
            
        if(selections[0] == 2):
            product_service[selections[2]]()
            
        input('\nPresiona una tecla para continuar...')
        