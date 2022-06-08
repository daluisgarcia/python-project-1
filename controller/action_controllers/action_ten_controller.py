from datetime import timedelta
from controller.action_controller import ActionController
from model.competitors_list import CompetitorsList


class ActionTenController(ActionController):
    
    def execute(self):
        male_total_seconds = 0
        fem_total_seconds = 0

        junior_total_seconds = 0
        senior_total_seconds = 0
        master_total_seconds = 0

        for competitor in CompetitorsList.competitors_list:
            competitor_seconds = (competitor.final_time.hour * 3600) + (competitor.final_time.minute * 60) + competitor.final_time.second

            # Sex validation
            if competitor.sex == 'F':
                fem_total_seconds += competitor_seconds

            elif competitor.sex == 'M':
                male_total_seconds += competitor_seconds

            # Ethnic group validation
            if competitor.age <= 25:
                junior_total_seconds += competitor_seconds

            elif competitor.age > 25 and competitor.age <= 40:
                senior_total_seconds += competitor_seconds

            else:
                master_total_seconds += competitor_seconds

        age_group_count = self._get_count_by_age_group()
        sex_counts = self._get_count_by_sex()

        print('Promedio de tiempos en Juniors: '+str(timedelta(seconds=junior_total_seconds/age_group_count['juniors'])))
        print('Promedio de tiempos en Seniors: '+str(timedelta(seconds=senior_total_seconds/age_group_count['seniors'])))
        print('Promedio de tiempos en Masters: '+str(timedelta(seconds=master_total_seconds/age_group_count['masters'])))
        print()
        print('Promedio de tiempos en hombres: '+str(timedelta(seconds=male_total_seconds/sex_counts['male'])))
        print('Promedio de tiempos en mujeres: '+str(timedelta(seconds=fem_total_seconds/sex_counts['fem'])))
        