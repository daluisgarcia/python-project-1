from controller.action_controllers.action_two_controller import ActionTwoController
from view.view_rendering import ViewRendering


class ActionTwo(ViewRendering):

    def render_view(self):
        ViewRendering.clean_screen()
        print('*'*60)
        print('Cantidad total de participantes')
        print('*'*60)

        controller = ActionTwoController()
        controller.execute()
        
        self.view_pause()