from sys import platform
import os
from abc import ABC, abstractmethod


class ViewRendering(ABC):

    '''
    Cleans the console screen
    '''
    @staticmethod
    def clean_screen():
        if platform == "linux" or platform == "linux2":
            os.system('clear')
        elif platform == "darwin":
            os.system('clear')
        elif platform == "win32":
            os.system('cls')


    def view_pause(self):
        print()
        input('Presione la tecla enter para volver al menú de acción...')


    '''
    Abstract class for view rendering.
    '''
    @abstractmethod
    def render_view(self):
        pass