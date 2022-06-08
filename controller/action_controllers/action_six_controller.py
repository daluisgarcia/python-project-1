from controller.action_controller import ActionController


class ActionSixController(ActionController):
    
    def execute(self):
        print('_'*84)
        print(("|{:10}|{:40}|{:5}|{:4}|{:8}|".format(
            "Cédula", 
            "Nombre", 
            "Sexo", 
            "Edad",
            "Tiempo"
        )))
        print('_'*84)

        male_list = self._filter_by_sex('M')
        male_list.sort(key=lambda comp: comp.final_time)

        fem_list = self._filter_by_sex('F')
        fem_list.sort(key=lambda comp: comp.final_time)

        print(str(fem_list[0]))

        print(str(male_list[0]))

        print('_'*84)