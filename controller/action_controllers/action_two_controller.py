from controller.action_controller import ActionController
from model.competitors_list import CompetitorsList


class ActionTwoController(ActionController):
    
    def execute(self):
        print(f'Cantidad total de participantes: {len(CompetitorsList.competitors_list)}')
