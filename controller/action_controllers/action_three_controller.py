from controller.action_controller import ActionController


class ActionThreeController(ActionController):
    
    def execute(self):
        print('_'*23)
        print(("|{:10}|{:10}|".format(
            "Grupo", 
            "Cantidad"
        )))
        print('_'*23)

        counts = self._get_count_by_age_group()
        
        print(("|{:10}|{:10}|".format(
            "Juniors", 
            counts['juniors']
        )))
        print(("|{:10}|{:10}|".format(
            "Seniors", 
            counts['seniors']
        )))
        print(("|{:10}|{:10}|".format(
            "Masters", 
            counts['masters']
        )))
        print('_'*23)
