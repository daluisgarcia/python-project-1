from datetime import time
from exceptions.incorrect_column_count import IncorrectColumnCount


class CompetitorInfo:
    '''
    Competitor info container
    '''
    def __init__(self, competitor_info_str: str) -> None:
        competitor_info_list = competitor_info_str.split(',')
        if len(competitor_info_list) != 10:
            raise IncorrectColumnCount()

        self.id = int(competitor_info_list[0])
        self.first_lastname = competitor_info_list[1]
        self.second_lastname = competitor_info_list[2]
        self.first_name = competitor_info_list[3]
        self.second_name_intitial = competitor_info_list[4]
        self.sex = competitor_info_list[5]
        self.age = int(competitor_info_list[6])
        # self.hour = int(competitor_info_list[7])
        # self.minutes = int(competitor_info_list[8])
        # self.seconds = int(competitor_info_list[9])
        self.time = time(
            int(competitor_info_list[7]), 
            int(competitor_info_list[8]), 
            int(competitor_info_list[9])
        )

    def __str__(self) -> str:
        # TODO Implement
        pass