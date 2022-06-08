from controller.action_controllers.action_one_controller import ActionOneController
from view.view_rendering import ViewRendering


class ActionOne(ViewRendering):

    def render_view(self):
        ViewRendering.clean_screen()
        print('*'*60)
        print('Lista con la totalidad de participantes')
        print('*'*60)

        controller = ActionOneController()
        controller.execute()

        self.view_pause()