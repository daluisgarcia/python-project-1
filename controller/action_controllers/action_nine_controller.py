from controller.action_controller import ActionController


class ActionNineController(ActionController):
    
    def execute(self):
        counts = self._get_count_by_age_group()

        print('Juniors ('+str(counts['juniors'])+'): | '+'*'*counts['juniors'])
        print('Seniors ('+str(counts['seniors'])+'): | '+'*'*counts['seniors'])
        print('Masters ('+str(counts['masters'])+'): | '+'*'*counts['masters'])