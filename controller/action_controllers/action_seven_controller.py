from datetime import time
from controller.action_controller import ActionController
from model.competitor_info import CompetitorInfo
from model.competitors_list import CompetitorsList


class ActionSevenController(ActionController):

    '''
    Gets the winners and prints the table
    '''
    def __print_winners_table(self, junior_list: list[CompetitorInfo], senior_list: list[CompetitorInfo], master_list: list[CompetitorInfo]):
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

        junior_list.sort(key=lambda comp: comp.final_time)
        senior_list.sort(key=lambda comp: comp.final_time)
        master_list.sort(key=lambda comp: comp.final_time)

        print(("|{:10}{:73}".format(
            "Juniors", 
            str(junior_list[0])
        )))

        print(("|{:10}{:73}".format(
            "Seniors", 
            str(senior_list[0])
        )))

        print(("|{:10}{:73}".format(
            "Masters", 
            str(master_list[0])
        )))

        print('_'*84)
    
    
    '''
    Execute parent method
    '''
    def execute(self):
        # Getting the female winners by age group
        fem_list = self._filter_by_sex('F')

        junior_list = self._filter_by_age_group('juniors', fem_list)
        senior_list = self._filter_by_age_group('seniors', fem_list)
        master_list = self._filter_by_age_group('masters', fem_list)

        print('Ganadoras femeninas: ')
        self.__print_winners_table(junior_list, senior_list, master_list)

        print()
        print()

        # Getting the male winners by age group
        male_list = self._filter_by_sex('M')

        junior_list = self._filter_by_age_group('juniors', male_list)
        senior_list = self._filter_by_age_group('seniors', male_list)
        master_list = self._filter_by_age_group('masters', male_list)

        print('Ganadores masculinos: ')
        self.__print_winners_table(junior_list, senior_list, master_list)