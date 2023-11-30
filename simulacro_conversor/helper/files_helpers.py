def json_to_csv(data):

    conversion = []

    for index, row in enumerate(data):

        new_row = []

        if index == 0:
            for col in row.keys():
                new_row.append(col)
            conversion.append(new_row)
            new_row = []

        for value in row.values():
            new_row.append(value)

        conversion.append(new_row)

    return conversion
