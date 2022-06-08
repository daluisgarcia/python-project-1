from controller.action_controllers.action_ten_controller import ActionTenController
from view.view_rendering import ViewRendering


class ActionTen(ViewRendering):

    def render_view(self):
        ViewRendering.clean_screen()
        print('*'*60)
        print('Promedio de tiempo por grupo etario y sexo')
        print('*'*60)

        controller = ActionTenController()
        controller.execute()
        
        self.view_pause()