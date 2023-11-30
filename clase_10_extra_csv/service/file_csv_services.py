import csv


def load_csv(path):

    data = []

    with open(path, newline='') as file:

        rows = csv.reader(file, delimiter=';')

        for row in rows:
            data.append(row)

    return data


'''

'''


def save_csv(path, data):

    with open(path, mode='w', newline='') as file:
        csv_file = csv.writer(file, delimiter=';')
        csv_file.writerows(data)
