from testdata.library import base_library
import csv


class CreateAccountDt:
    def __init__(self, username):
        self.username = username


def get_csv_data(file_name, cre):
    file_path = base_library.create_file_path_input(file_name)
    rows = []
    csv_data = open(str(file_path))
    content = csv.reader(csv_data)

    # skip header line
    next(content, None)

    # add rows to list
    for row in content:
        rows.append(row)
    # convert row to object
    objs = []
    for r in rows:
        objs.append(cre(r[0]))

    return objs


def get_data(file_name):
    file_path = base_library.create_file_path_input(file_name)
    # create an empty list to store rows
    rows = []
    # open the CSV file
    data_file = open(str(file_path))
    # create a CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader, None)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
