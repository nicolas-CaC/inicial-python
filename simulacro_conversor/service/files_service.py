import json
import csv


def load_json(path_file):
    with open(path_file, "r") as file:
        return json.load(file)


def write_json(path_file, data):
    with open(path_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_csv(path):
    data = []
    with open(path, newline="") as file:
        rows = csv.reader(file, delimiter=";")
        for row in rows:
            data.append(row)
    return data


def save_csv(path, data):
    with open(path, mode="w", newline="") as file:
        csv_file = csv.writer(file, delimiter=";")
        csv_file.writerows(data)
