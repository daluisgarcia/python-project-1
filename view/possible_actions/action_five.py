from controller.action_controllers.action_five_controller import ActionFiveController
from view.view_rendering import ViewRendering


class ActionFive(ViewRendering):

    def render_view(self):
        ViewRendering.clean_screen()
        print('*'*60)
        print('Ganadores por grupo etario')
        print('*'*60)

        controller = ActionFiveController()
        controller.execute()
        
        self.view_pause()