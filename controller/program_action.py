from abc import ABC, abstractmethod


class ProgramAction(ABC):
    '''
    Abstract class for program actions.
    '''
    @abstractmethod
    def show_action(self):
        pass