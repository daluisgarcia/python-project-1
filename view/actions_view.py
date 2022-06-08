from time import sleep
from view.possible_actions.action_eight import ActionEight
from view.possible_actions.action_five import ActionFive
from view.possible_actions.action_four import ActionFour
from view.possible_actions.action_nine import ActionNine
from view.possible_actions.action_one import ActionOne
from view.possible_actions.action_seven import ActionSeven
from view.possible_actions.action_six import ActionSix
from view.possible_actions.action_ten import ActionTen
from view.possible_actions.action_three import ActionThree
from view.possible_actions.action_two import ActionTwo
from view.view_rendering import ViewRendering


class ActionsView(ViewRendering):

    def __init__(self) -> None:
        self.possible_actions_objects: dict[str, ViewRendering] = {
            '1': ActionOne(), 
            '2': ActionTwo(), 
            '3': ActionThree(), 
            '4': ActionFour(), 
            '5': ActionFive(), 
            '6': ActionSix(), 
            '7': ActionSeven(), 
            '8': ActionEight(), 
            '9': ActionNine(), 
            '10': ActionTen()
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
                self.clean_screen()
                print('Opción inválida, intente de nuevo')
                sleep(5)
                continue

            self.possible_actions_objects[option_selected].render_view()