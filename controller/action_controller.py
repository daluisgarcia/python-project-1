from abc import ABC, abstractmethod
from model.competitor_info import CompetitorInfo
from model.competitors_list import CompetitorsList


class ActionController(ABC):

    '''
    Returns a list with the competitors that are in the age group
    '''
    def _filter_by_age_group(self, age_group: str, competitor_list: list[CompetitorsList] = None) -> list[CompetitorInfo]:
        if not competitor_list:
            competitor_list = CompetitorsList.competitors_list
            
        if age_group == 'juniors':
            return [competitor for competitor in competitor_list if competitor.age <= 25]
        elif age_group == 'seniors':
            return [competitor for competitor in competitor_list if competitor.age > 25 and competitor.age <= 40]
        elif age_group == 'masters':
            return [competitor for competitor in competitor_list if competitor.age > 40]


    '''
    Returns a list with the competitors that have the sex given
    '''
    def _filter_by_sex(self, sex: str, competitor_list: list[CompetitorsList] = None) -> list[CompetitorInfo]:
        if not competitor_list:
            competitor_list = CompetitorsList.competitors_list
            
        return [competitor for competitor in competitor_list if competitor.sex == sex ]


    '''
    Returns the number of competitors for each sex
    '''
    def _get_count_by_sex(self, competitor_list: list[CompetitorsList] = None) -> dict[str, int]:
        if not competitor_list:
            competitor_list = CompetitorsList.competitors_list

        return {
            'male': len(self._filter_by_sex('M', competitor_list)),
            'fem': len(self._filter_by_sex('F', competitor_list))
        }

    
    '''
    Returns the number of competitors for each age group
    '''
    def _get_count_by_age_group(self, competitor_list: list[CompetitorsList] = None) -> dict[str, int]:
        if not competitor_list:
            competitor_list = CompetitorsList.competitors_list

        return {
            'juniors': len(self._filter_by_age_group('juniors', competitor_list)),
            'seniors': len(self._filter_by_age_group('seniors', competitor_list)),
            'masters': len(self._filter_by_age_group('masters', competitor_list))
        }


    @abstractmethod
    def execute(self):
        pass
