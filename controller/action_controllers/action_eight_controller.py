from controller.action_controller import ActionController
from model.competitor_info import CompetitorInfo
from model.competitors_list import CompetitorsList


class ActionEightController(ActionController):
    
    def execute(self):
        competitors_list = CompetitorsList.competitors_list
        competitors_list.sort(key=lambda comp: comp.final_time)
        winner: CompetitorInfo = competitors_list[0]
        
        print(f'El ganador general es: {winner.get_full_name()} con un tiempo de: {winner.final_time}')