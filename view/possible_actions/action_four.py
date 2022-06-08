from controller.action_controllers.action_four_controller import ActionFourController
from view.view_rendering import ViewRendering


class ActionFour(ViewRendering):

    def render_view(self):
        ViewRendering.clean_screen()
        print('*'*60)
        print('Cantidad de participantes por sexo')
        print('*'*60)

        controller = ActionFourController()
        controller.execute()
        
        self.view_pause()