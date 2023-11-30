import config.data as data
import helpers.option_helpers as helpers

def option_service():
    
    main_option = helpers.menu(data.options, 'main')
    
    if(main_option == 1):
        data.selections[1] = helpers.menu(data.options, 'customers')
    
    if(main_option == 2):
        data.selections[2] = helpers.menu(data.options, 'products')