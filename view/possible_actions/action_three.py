from controller.action_controllers.action_three_controller import ActionThreeController
from view.view_rendering import ViewRendering


class ActionThree(ViewRendering):

    def render_view(self):
        ViewRendering.clean_screen()
        print('*'*60)
        print('Cantidad de participantes por grupo etario')
        print('*'*60)

        controller = ActionThreeController()
        controller.execute()
        
        self.view_pause()