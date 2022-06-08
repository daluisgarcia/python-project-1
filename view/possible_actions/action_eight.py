from controller.action_controllers.action_eight_controller import ActionEightController
from view.view_rendering import ViewRendering


class ActionEight(ViewRendering):

    def render_view(self):
        ViewRendering.clean_screen()
        print('*'*60)
        print('Ganador general')
        print('*'*60)

        controller = ActionEightController()
        controller.execute()
        
        self.view_pause()