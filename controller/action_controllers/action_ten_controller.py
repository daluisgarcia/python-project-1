from datetime import timedelta
from controller.action_controller import ActionController


class ActionTenController(ActionController):
    
    def execute(self):
        male_list = self._filter_by_sex('M')
        fem_list = self._filter_by_sex('F')

        junior_list = self._filter_by_age_group('juniors')
        senior_list = self._filter_by_age_group('seniors')
        master_list = self._filter_by_age_group('masters')

        male_times = [(comp.final_time.hour * 3600) + (comp.final_time.minute * 60) + comp.final_time.second for comp in male_list]
        male_total_seconds = sum(male_times)

        fem_times = [(comp.final_time.hour * 3600) + (comp.final_time.minute * 60) + comp.final_time.second for comp in fem_list]
        fem_total_seconds = sum(fem_times)

        junior_times = [(comp.final_time.hour * 3600) + (comp.final_time.minute * 60) + comp.final_time.second for comp in junior_list]
        junior_total_seconds = sum(junior_times)

        senior_times = [(comp.final_time.hour * 3600) + (comp.final_time.minute * 60) + comp.final_time.second for comp in senior_list]
        senior_total_seconds = sum(senior_times)

        master_times = [(comp.final_time.hour * 3600) + (comp.final_time.minute * 60) + comp.final_time.second for comp in master_list]
        master_total_seconds = sum(master_times)

        age_group_count = self._get_count_by_age_group()
        sex_counts = self._get_count_by_sex()

        print('Promedio de tiempos en Juniors: '+str(timedelta(seconds=junior_total_seconds/age_group_count['juniors'])))
        print('Promedio de tiempos en Seniors: '+str(timedelta(seconds=senior_total_seconds/age_group_count['seniors'])))
        print('Promedio de tiempos en Masters: '+str(timedelta(seconds=master_total_seconds/age_group_count['masters'])))
        print()
        print('Promedio de tiempos en hombres: '+str(timedelta(seconds=male_total_seconds/sex_counts['male'])))
        print('Promedio de tiempos en mujeres: '+str(timedelta(seconds=fem_total_seconds/sex_counts['fem'])))
        