from view.possible_actions.action_one import ActionOne
from view.view_rendering import ViewRendering


class ActionsView(ViewRendering):

    def __init__(self) -> None:
        self.possible_actions_objects: dict[str, ViewRendering] = {
            '1': ActionOne(), 
            '2': ActionOne(), 
            '3': ActionOne(), 
            '4': ActionOne(), 
            '5': ActionOne(), 
            '6': ActionOne(), 
            '7': ActionOne(), 
            '8': ActionOne(), 
            '9': ActionOne(), 
            '10': ActionOne()
        }
    
    def render_view(self):
        while True:
            self.clean_screen()
            print('MENÚ ARCHIVO')
            print('*'*60)
            print('1. Lista con la totalidad de participantes')
            print('2. Cantidad total de participantes')
            print('3. Cantidad de participantes por grupo etario')
            print('4. Cantidad de participantes por sexo')
            print('5. Ganadores por grupo etario')
            print('6. Ganadores por sexo')
            print('7. Ganadores por grupo etario y sexo')
            print('8. Ganador general')
            print('9. Histograma de participante por grupo etario')
            print('10. Promedio de tiempo por grupo etario y sexo')
            print('11. Salir')
            print('*'*60)
            option_selected = input('Ingrese una opción: ')

            if option_selected == '11':
                break

            if option_selected not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                print('Opción inválida')
                continue

            self.possible_actions_objects[option_selected].render_view()