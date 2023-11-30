from os import path


def convert_path(complete_path):
    # root = path.dirname(complete_path)
    filename = path.splitext(complete_path)[0] + '.csv'
    return filename
