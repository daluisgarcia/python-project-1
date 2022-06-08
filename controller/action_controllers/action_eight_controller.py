from datetime import time
from controller.action_controller import ActionController
from model.competitor_info import CompetitorInfo
from model.competitors_list import CompetitorsList


class ActionEightController(ActionController):
    
    def execute(self):
        winner: CompetitorInfo = None
        best_time = time(15, 0, 0)
        for competitor in CompetitorsList.competitors_list:
            if competitor.final_time < best_time:
                best_time = competitor.final_time
                winner = competitor
        
        print(f'El ganador general es: {winner.get_full_name()} con un tiempo de: {best_time}')