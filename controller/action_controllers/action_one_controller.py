from controller.action_controller import ActionController
from model.competitors_list import CompetitorsList


class ActionOneController(ActionController):
    
    def execute(self):
        print('_'*73)
        print(("|{:10}|{:40}|{:5}|{:4}|{:8}|".format(
            "Cédula", 
            "Nombre", 
            "Sexo", 
            "Edad",
            "Tiempo"
        )))
        print('_'*73)
        for competitor in CompetitorsList.competitors_list:
            print(str(competitor))
        print('_'*73)