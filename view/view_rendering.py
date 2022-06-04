from abc import ABC, abstractmethod


class ViewRendering(ABC):
    '''
    Abstract class for view rendering.
    '''
    @abstractmethod
    def render_view(self):
        pass