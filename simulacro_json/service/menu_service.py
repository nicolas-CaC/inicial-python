import config.data as data
import helpers.option_helpers as helpers


def menu_service():

    data.selections[0] = helpers.menu(data.options, 'main')

    if (data.selections[0] == 1):
        data.selections[1] = helpers.menu(data.options, 'customers')

    if (data.selections[0] == 2):
        data.selections[2] = helpers.menu(data.options, 'products')
