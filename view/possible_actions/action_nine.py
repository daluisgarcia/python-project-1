from controller.action_controllers.action_nine_controller import ActionNineController
from view.view_rendering import ViewRendering


class ActionNine(ViewRendering):

    def render_view(self):
        ViewRendering.clean_screen()
        print('*'*60)
        print('Histograma de participante por grupo etario')
        print('*'*60)

        controller = ActionNineController()
        controller.execute()
        
        self.view_pause()