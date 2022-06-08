from controller.action_controllers.action_six_controller import ActionSixController
from view.view_rendering import ViewRendering


class ActionSix(ViewRendering):

    def render_view(self):
        ViewRendering.clean_screen()
        print('*'*60)
        print('Ganadores por sexo')
        print('*'*60)

        controller = ActionSixController()
        controller.execute()
        
        self.view_pause()