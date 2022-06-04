import traceback
from model.file_reader import FileReader


def main_function():
    file_reader = FileReader('competencia.txt')
    file_reader.read_file()


if __name__ == '__main__':
    try:
        main_function()
    except Exception as e:
        print(f'Error inesperado: {e}')
        traceback.print_exc() # TODO Remove before release