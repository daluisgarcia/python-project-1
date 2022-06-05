from time import sleep
import traceback
from controller.competitors_info_controller import CompetitorsInfoController

from view.actions_view import ActionsView
from view.file_view import FileView
from view.view_rendering import ViewRendering


def main_function():
    while True:
        ViewRendering.clean_screen()
        print('MENÚ PRINCIPAL')
        print('*'*60)
        print('1. Archivo')
        print('2. Acciones')
        print('3. Salir')
        print('*'*60)
        option_selected = input('Ingrese una opción: ')
        
        if option_selected == '1':
            file_view = FileView()
            file_view.render_view()
            
        elif option_selected == '2':
            if not CompetitorsInfoController.competitors_list:
                ViewRendering.clean_screen()
                print('No hay competidores registrados, por favor ingrese un archivo')
                sleep(5)
                continue

            action_view = ActionsView()
            action_view.render_view()

        elif option_selected == '3':
            break
            
        else:
            print('Opción inválida')


if __name__ == '__main__':
    try:
        main_function()
    except Exception as e:
        print(f'Error inesperado: {e}')
        traceback.print_exc() # TODO Remove before release