from time import sleep
from exceptions.incorrect_column_count import IncorrectColumnCount
from exceptions.incorrect_file_extension import IncorrectFileExtension
from model.competitors_list import CompetitorsList
from model.file_reader import FileReader
from view.view_rendering import ViewRendering


class FileView(ViewRendering):

    def __init__(self) -> None:
        self.file_name = 'competencia.txt'
    
    def render_view(self):
        while True:
            self.clean_screen()
            print('MENÚ ARCHIVO')
            print('*'*60)
            print('1. Cargar Archivo')
            print('2. Salir')
            print('*'*60)
            option_selected = input('Ingrese una opción: ')

            if option_selected == '1':
                print('*'*60)
                print()

                file_name = input('Ingrese el nombre del archivo (el nombre por defecto es "competencia.txt"): ')
                if file_name:
                    self.file_name = file_name

                try: 
                    file_reader = FileReader(self.file_name)
                    CompetitorsList.competitors_list = file_reader.read_file()
                    print('Archivo subido correctamente, en breve será redirigido al menú principal...')
                    break
                
                except FileNotFoundError:
                    self.clean_screen()
                    print("Archivo no encontrado, intente de nuevo")

                except PermissionError:
                    self.clean_screen()
                    print("No cuenta con permisos para leer el archivo, verifique e intente de nuevo")

                except FileExistsError:
                    self.clean_screen()
                    print("No cuenta con permisos para leer el archivo, verifique e intente de nuevo")

                except IncorrectColumnCount as e:
                    self.clean_screen()
                    print(f'{e}')

                except IncorrectFileExtension as e:
                    print(f'{e}')

                except Exception as e:
                    self.clean_screen()
                    print(f'Error inesperado: {e}')

                finally:
                    sleep(8)
                
            elif option_selected == '2':
                break
                
            else:
                self.clean_screen()
                print('Opción inválida, intente de nuevo')
                sleep(5)
