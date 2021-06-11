import os


def create_file_path_input(file_name_excel):
    current_directory = os.path.dirname(os.path.dirname(__file__))
    input_data_directory = os.path.join(current_directory.replace("", ""), "inputData")
    file_path_excel = os.path.join(input_data_directory, file_name_excel)
    return file_path_excel


# def create_file_path_result(file_name_excel):
#     current_directory = os.path.dirname(os.path.dirname(__file__))
#     input_data_directory = os.path.join(current_directory.replace("\\src\\hexalink", ""), "report")
#     file_path_excel = os.path.join(input_data_directory, file_name_excel)
#     return file_path_excel
