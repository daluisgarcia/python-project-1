from itertools import count
from controller.action_controller import ActionController
from model.competitors_list import CompetitorsList


class ActionFourController(ActionController):
    
    def execute(self):
        counts = self._get_count_by_sex()
        
        print('Cantidad de mujeres: '+str(counts['fem'])+' y cantidad de hombres: '+str(counts['male']))
