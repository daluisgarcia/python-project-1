from time import sleep
from view.view_rendering import ViewRendering


class ActionOne(ViewRendering):

    def render_view(self):
        print('ActionOne')
        sleep(10)