from controller.action_controllers.action_seven_controller import ActionSevenController
from view.view_rendering import ViewRendering


class ActionSeven(ViewRendering):

    def render_view(self):
        ViewRendering.clean_screen()
        print('*'*60)
        print('Ganadores por grupo etario y sexo')
        print('*'*60)

        controller = ActionSevenController()
        controller.execute()
        
        self.view_pause()