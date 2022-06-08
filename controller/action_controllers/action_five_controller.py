from datetime import time
from controller.action_controller import ActionController
from model.competitor_info import CompetitorInfo
from model.competitors_list import CompetitorsList


class ActionFiveController(ActionController):
    
    def execute(self):
        print('_'*84)
        print(("|{:10}|{:10}|{:40}|{:5}|{:4}|{:8}|".format(
            "Grupo", 
            "Cédula", 
            "Nombre", 
            "Sexo", 
            "Edad",
            "Tiempo"
        )))
        print('_'*84)

        juniors_list = self._filter_by_age_group('juniors')
        seniors_list = self._filter_by_age_group('seniors')
        masters_list = self._filter_by_age_group('masters')

        juniors_list.sort(key=lambda comp: comp.final_time)
        seniors_list.sort(key=lambda comp: comp.final_time)
        masters_list.sort(key=lambda comp: comp.final_time)

        print(("|{:10}{:73}".format(
            "Juniors", 
            str(juniors_list[0])
        )))

        print(("|{:10}{:73}".format(
            "Seniors", 
            str(seniors_list[0])
        )))

        print(("|{:10}{:73}".format(
            "Masters", 
            str(masters_list[0])
        )))

        print('_'*84)