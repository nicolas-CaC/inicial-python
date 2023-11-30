from os import system
import service.files_service as files
import helper.files_helpers as helpers
import utils.files_utils as utils

system("cls")

path = input("ingrese la ruta del archivo: ")
# C:\Workspaces\Codo_a_Codo\inicial\23547\python\simulacro_conversor\users.json

data = files.load_json(path)
conversion = helpers.json_to_csv(data)
new_path = utils.convert_path(path)

files.save_csv(new_path, conversion)
print(f'Convertido! {new_path}')
